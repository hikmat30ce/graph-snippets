import http.client

conn = http.client.HTTPSConnection("graph.microsoft.com")

payload = "{ }"

headers = { 'content-type': "application/json" }

conn.request("PATCH", "/v1.0/me/drive/items/%7Bitem-id%7D/permissions/%7Bperm-id%7D", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
