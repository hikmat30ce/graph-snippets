HttpResponse<String> response = Unirest.post("https://graph.microsoft.com/v1.0/me/drive/items/%7Bid%7D/workbook/tables(%3Cid%7Cname%3E)/rows(%3Cindex%3E)/delete")
  .header("content-type", "application/json")
  .body("{ }")
  .asString();
