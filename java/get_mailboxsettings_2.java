HttpResponse<String> response = Unirest.get("https://graph.microsoft.com/v1.0/me/mailboxSettings/automaticRepliesSetting")
  .asString();
