HttpResponse<String> response = Unirest.patch("https://graph.microsoft.com/v1.0/me/drive/items/%7Bid%7D/workbook/names(%3Cname%3E)/range/format")
  .header("content-type", "application/json")
  .body("{ }")
  .asString();
