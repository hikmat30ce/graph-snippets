HttpResponse<String> response = Unirest.post("https://graph.microsoft.com/v1.0/me/calendar/events")
  .header("content-type", "application/json")
  .body("{ }")
  .asString();
