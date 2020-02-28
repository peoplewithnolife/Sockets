const express = require("express");
const bodyParser = require("body-parser");

const port = 3000;

const app = express();

var getsRcvd = 0;
var postsRcvd = 0;

app.param('test', function(req,res,test) {
    console.log("Param");
    next();
});

app.get("/:test", function (req, res) {
    res.send("Get a job");
    //console.log(req);
    console.log(req.body);
    console.log(getsRcvd);
    //rsp.sendFile(__dirname + "/index.html");
    getsRcvd++;
});

app.post("/:test", function (req,res) {
   res.send("Post a job");
   //console.log(req);
   console.log(req.params);
   console.log(postsRcvd);
   postsRcvd++;
});

app.listen(port, function () {
    console.log("Running on port: " + port);
});

