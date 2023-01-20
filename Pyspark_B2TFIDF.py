# Imports
from pyspark.sql import SparkSession
from pyspark.sql import types
from pyspark.sql import DataFrame

#Init Spark
spark  = SparkSession.builder \
    .appName("B2IDFTFKMeans") \
    .enableHiveSupport() \
    .config("spark.hadoop.yarn.resourcemanager.principal", "ibrooks") \
    .config("spark.sql.warehouse.dir", "target/spark-warehouse") \
    .getOrCreate()
  
#Check Spark Version  
spark.version

#Import JSON Files 
df_WholeSetRaw = spark.read.option("multiline", "true").json("tweets*.json")
df_WholeSetRaw.cache()

#Create Table from DataFrame
#df_WholeSetRaw.createOrReplaceTempView("B2Tweets")

#Display resulting Infered schema 
df_WholeSetRaw.printSchema()
df_WholeSetRaw.take(1)

#Using Spark Feature Engineering Tools to for NLP Use Case
from pyspark.ml.feature import HashingTF, IDF, Tokenizer, RegexTokenizer, CountVectorizer, CountVectorizerModel
from pyspark.ml.classification import LogisticRegression
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType

#Tokenizer Option 1
tokenizer = Tokenizer(inputCol="tweet", outputCol="words")
tokenized = tokenizer.transform(df_WholeSetRaw)

#Tokenizer Option 2
regexTokenizer = RegexTokenizer(inputCol="tweet", outputCol="words", pattern="\\\W+")
# alternatively, pattern="\\w+", gaps(False)
regexTokenized = regexTokenizer.transform(df_WholeSetRaw)

#Count Tokens for Common Words
countTokens = udf(lambda words: len(words), IntegerType())

regexTokenized.select("tweet", "words") \
    .withColumn("tokens", countTokens(col("words"))).show(truncate=False)

#Configure CountVectorizer Model  
cvModel = CountVectorizer(inputCol="words", outputCol="rawFeatures", minDF=4,  vocabSize=100000).fit(tokenized)

#Configure HashingTF Model  
hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=400)

#Build Featured Training Sets
CVfeaturizedData = cvModel.transform(regexTokenized)
TFfeaturizedData = hashingTF.transform(regexTokenized)

#Configure IDF/TF Model
idf = IDF(inputCol="rawFeatures", outputCol="features")

#Fit IDF/TF Model to Featurized Training Setd
idfModel = idf.fit(TFfeaturizedData)
rescaledData = idfModel.transform(TFfeaturizedData)
rescaledData.select("tweet","features").show()

#rescaledData.select("features").createOrReplaceTempView("B2OutTFIDF")
#rescaledData.show(truncate=False)

#KMeans - Clustering on Hashed Tokens 
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.sql.functions import lit

#Set the number of clusters (Play around with this value)
NumberOfClusters = 128

#Create the K-Means model
kmeans = KMeans().setK(NumberOfClusters).setSeed(1).setFeaturesCol("features").setPredictionCol("prediction")

#Train the K-Means model with feature vector
model = kmeans.fit(rescaledData)

# Make predictions
predictions = model.transform(rescaledData)

# Evaluate clustering by computing Silhouette score
evaluator = ClusteringEvaluator()

silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

# Shows the Clusering results
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)
    
print("Documents by Cluster")
predictions.select("tweet","prediction").show()

#Print a clusters members out
predictions.filter("prediction =13").select("sentiment","tweet").show()

#MinHash LSH Example
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import MinHashLSH

#Set Vocab Size - Good value to play around with
vocabSize = 10000

#Build MinHash Model
mh = MinHashLSH().setNumHashTables(vocabSize).setInputCol("rawFeatures").setOutputCol("hashValues")
MHmodel = mh.fit(rescaledData)
MHmodel.transform(rescaledData).show()

#Find Valus for Keyword Search
keyVal1 = cvModel.vocabulary.index("B2")
keyVal2 = cvModel.vocabulary.index("Bomber")
keyVal3 = cvModel.vocabulary.index("bomb")

#Build Keys 
One_key = Vectors.sparse(vocabSize, [200], [1.0])
Two_key = Vectors.sparse(vocabSize, [200, 398], [1.0, 1.0])
Three_key = Vectors.sparse(vocabSize, [24, 200, 398], [1.0, 1.0, 1.0])

#Number of Search Results
k = 40

#Find Matched Documents
DF_Matched = MHmodel.approxNearestNeighbors(rescaledData, Three_key, k)
DF_Matched.cache()
DF_Matched.select("sentiment","tweet","distCol").show() #truncate=False