from tools1.tools_math import multiply
import requests
response= requests.get("https: //jsonplaceholder.typecode.com/posts/1")
data = response.json()
print("Title:",data["title"])

print(multiply(4,6))