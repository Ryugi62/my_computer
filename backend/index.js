// express server
const express = require("express"); // 용도 : express 사용하기 위해
const bodyParser = require("body-parser"); // 용도 : req.body 사용하기 위해
const cookieParser = require("cookie-parser"); // 용도 : req.cookies 사용하기 위해
const history = require("connect-history-api-fallback");
const app = express();
const cors = require("cors");
const mysql = require("mysql");
const AdmZip = require("adm-zip");

// const port = process.env.PORT;
const port = 3000;

// use mysql connection
const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "password",
  database: "myComputer",
});

connection.connect();
console.log("mysql connected");

// make table
connection.query(
  "CREATE TABLE IF NOT EXISTS hardware (ip varchar(30) not null, os varchar(30) not null, cpu varchar(30) not null, ram varchar(30) not null, graphic_card varchar(30) not null, bios varchar(30) not null, mainboard_manufacturer varchar(30) not null, drive_capacity varchar(30) not null) ENGINE=MYISAM CHARSET=utf8;",
  (err) => {
    if (err) throw err;
  }
);

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

app.post("/api/getProgram", (req, res) => {
  // how to send .zip file to client
  res.download(__dirname + "/my_computer.exe", "my_computer.exe");
});

app.post("/api/getHardware", (req, res) => {
  connection.query(
    "SELECT * FROM hardware WHERE ip = ?",
    [req.body.json.ip],
    (err, result) => {
      if (err) {
        console.log(err);
      } else {
        console.log(result);
        res.send(result);
      }
    }
  );
});

app.post("/api/setHardware", (req, res) => {
  console.log(req.body);

  connection.query(
    "INSERT INTO hardware (ip, os, cpu, ram, graphic_card, bios, mainboard_manufacturer, drive_capacity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    [
      req.body.ip,
      req.body.os,
      req.body.cpu,
      req.body.ram,
      req.body.graphic_card,
      req.body.bios,
      req.body.mainboard_manufacturer,
      req.body.drive_capacity,
    ],
    (err, result) => {
      if (err) {
        console.log(err);
      } else {
        console.log(result);
        res.send(result);
      }
    }
  );
});

app.get("/test", (req, res) => {
  const { name } = req.cookies;

  console.log(name);

  res.cookie("name", "express");

  res.send("Cookie set");
});

// start server
app.listen(port, () => console.log(`내컴퓨터.com listening on port ${port}!`));
