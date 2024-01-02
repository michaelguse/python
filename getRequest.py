import requests
import json
from types import SimpleNamespace

url = "https://api.status.salesforce.com/v1/instances"
data = requests.get(url).text

# Parse JSON into an object with attributes corresponding to dict keys.
data_in = json.loads(data)

res = list(filter(lambda x:x["key"]=="CS86",data_in))

print("Type: ", type(res[0]))
print("Len: " , len(res[0]))
print("")

output=("key", "status")
for x in output:
    print(x+":\t",res[0][x])
