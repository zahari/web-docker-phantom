//var page = require("webpage").create();
var buster = require("buster");
var assert = buster.referee.assert;

buster.testCase("My thing", {
    "has the foo and bar": function () {
        assert.equals("foo", "foo");
    },

    "states the obvious": function () {
        assert(true);
    }
});

/*
page.open("http://localhost", function(status) {
  // Test 1
  console.log("Status: " + status);
  if(status === "success") {
    page.render('localhost.png');
  }

  // Test 2
  var title = page.evaluate(function() {
    return document.title;
  });
  console.log("Page title is " + title);

  phantom.exit();
});
*/
