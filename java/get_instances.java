HttpResponse<String> response = Unirest.get("https://graph.microsoft.com/v1.0/me/events/%7Bid%7D/instances")
  .asString();
