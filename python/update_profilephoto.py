import http.client

conn = http.client.HTTPSConnection("graph.microsoft.com")

payload = "{ }"

headers = { 'content-type': "application/json" }

conn.request("PUT", "/v1.0/me/photo/$value", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
