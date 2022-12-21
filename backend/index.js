// express server
const express = require("express"); // 용도 : express 사용하기 위해
const bodyParser = require("body-parser"); // 용도 : req.body 사용하기 위해
const cookieParser = require("cookie-parser"); // 용도 : req.cookies 사용하기 위해
const history = require("connect-history-api-fallback");
const app = express();
const cors = require("cors");

// const port = process.env.PORT;
const port = 3000;

app.use(cors());
app.use(history());
app.use(express.static("dist"));
app.use(cookieParser()); // 용도 : req.cookies 사용하기 위해
app.use(bodyParser.json()); // 용도 : req.body 사용하기 위해
app.use(bodyParser.urlencoded({ extended: false })); // 용도 : req.body 사용하기 위해

app.use(express.json());

app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  next();
});

app.get("/api/getProgram", (req, res) => {
  // send zip file to client
  res.download(__dirname + "/my_computer.zip");
});

app.get("/test", (req, res) => {
  const { name } = req.cookies;

  console.log(name);

  res.cookie("name", "express");

  res.send("Cookie set");
});

// start server
app.listen(port, () => console.log(`내컴퓨터.com listening on port ${port}!`));
