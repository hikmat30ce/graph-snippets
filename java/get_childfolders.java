HttpResponse<String> response = Unirest.get("https://graph.microsoft.com/v1.0/me/mailFolders/%7Bid%7D/childFolders")
  .asString();
