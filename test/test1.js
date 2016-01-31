var page = require('webpage').create();

page.open('http://localhost', function(status) {
  console.log("Status: " + status);
  if(status === "success") {
    page.render('localhost.png');
  }
  phantom.exit();
});
