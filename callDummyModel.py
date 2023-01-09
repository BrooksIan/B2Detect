from pprint import pprint
import json
import sys

imagePath = str(sys.argv[1])
threshold=0.95
timeTheashold = 2.5

response = {"response":"B2Found","confidence":"99.999" , "duration":"88.88"}

jsonresponse = json.dumps(response)
print(jsonresponse)
