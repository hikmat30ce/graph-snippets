import http.client

conn = http.client.HTTPSConnection("graph.microsoft.com")

conn.request("GET", "/v1.0/me/drive/items/%7Bid%7D/workbook/worksheets(%3Cid%7Cname%3E)/charts(%3Cname%3E)/axes/valueaxis/format/font")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
