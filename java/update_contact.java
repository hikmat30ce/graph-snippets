HttpResponse<String> response = Unirest.patch("https://graph.microsoft.com/v1.0/me/contacts/%7Bid%7D")
  .header("content-type", "application/json")
  .body("{ }")
  .asString();
