import http.client
import json
# Define API host and endpoint
conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
endpoint = "/posts/1"
# Make a GET request
conn.request("GET", endpoint)
# Get the response
response = conn.getresponse()
print(f"Status: {response.status}")
data = response.read().decode("utf-8")
# Parse the response (optional)
parsed_data = json.loads(data)
print(parsed_data)
# Close the connection
conn.close()



import urllib.request
import json
# API URL
url = "https://jsonplaceholder.typicode.com/posts/1"
# Make a GET request
with urllib.request.urlopen(url) as response:
    data = response.read().decode("utf-8")
# Parse the response (optional)
parsed_data = json.loads(data)
print(parsed_data)
