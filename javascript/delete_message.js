var data = "{ }";

var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === this.DONE) {
    console.log(this.responseText);
  }
});

xhr.open("DELETE", "https://graph.microsoft.com/v1.0/me/messages/%7Bid%7D");
xhr.setRequestHeader("content-type", "application/json");

xhr.send(data);
