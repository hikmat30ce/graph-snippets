import http.client

conn = http.client.HTTPSConnection("graph.microsoft.com")

payload = "{ }"

headers = { 'content-type': "application/json" }

conn.request("POST", "/%7Bver%7D/drive/root/workbook/worksheets/%7Bid%7D/range/resizedRange(deltarows=%7Bn%7D,", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
