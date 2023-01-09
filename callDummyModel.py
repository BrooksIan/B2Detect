from pprint import pprint
import json
import sys

#Dummy Response 
response = {"response":"B2Found","confidence":"99.999" , "duration":"88.88"}

jsonresponse = json.dumps(response)
print(jsonresponse)
