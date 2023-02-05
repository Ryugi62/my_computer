// express server
const express = require("express"); // 용도 : express 사용하기 위해
const bodyParser = require("body-parser"); // 용도 : req.body 사용하기 위해
const cookieParser = require("cookie-parser"); // 용도 : req.cookies 사용하기 위해
const history = require("connect-history-api-fallback");
const app = express();
const cors = require("cors");
const mysql = require("mysql");

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

// make hardware table
// ip cpu mainboard external_vga internal_vga ram drive os
connection.query(
  "CREATE TABLE IF NOT EXISTS hardware (id int not null auto_increment, ip varchar(30) not null, cpu text not null, mainboard text not null, external_vga text not null, internal_vga text not null, ram text not null, drive text not null, os text not null, primary key(id)) ENGINE=MYISAM CHARSET=utf8;",
  (err) => {
    if (err) throw err;
  }
);

// make admin table
connection.query(
  "CREATE TABLE IF NOT EXISTS admin (id varchar(30) not null, password varchar(30) not null) ENGINE=MYISAM CHARSET=utf8;",
  (err) => {
    if (err) throw err;
  }
);

// make post table
connection.query(
  // create post table
  "CREATE TABLE IF NOT EXISTS post (id int not null auto_increment, title text not null, content text not null, date text not null, primary key(id)) ENGINE=MYISAM CHARSET=utf8;",
  (err) => {
    if (err) throw err;
  }
);

// make gameList tableㅅ
// name, cpu, drive, vga, os, ram
connection.query(
  // name, intelCpu, amdCpu, drive, external_vga, internal_vga, os, ram
  "CREATE TABLE IF NOT EXISTS gameList (id int not null auto_increment, name text not null, intelCpu text not null, amdCpu text not null, drive text not null, external_vga text not null, internal_vga text not null, os text not null, ram text not null, primary key(id)) ENGINE=MYISAM CHARSET=utf8;",
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
  res.download(__dirname + "/my_computer.zip", "my_computer.zip");
});

app.post("/api/getHardware", (req, res) => {
  console.log(req.body);
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
    "INSERT INTO hardware (ip, cpu, mainboard, external_vga, internal_vga, ram, drive, os) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    [
      req.body.ip,
      req.body.cpu,
      req.body.mainboard_manufacturer,
      req.body.external_vga,
      req.body.internal_vga,
      req.body.ram,
      req.body.full_drive,
      req.body.os,
    ],
    (err) => {
      if (err) {
        console.log(err);
      } else {
        res.send("success");
      }
    }
  );
});

app.post("/api/login", (req, res) => {
  //  get id and password
  const { id, password } = req.body.json;

  // connect to mysql and check id and password
  connection.query(
    "SELECT * FROM admin WHERE id = ? AND password = ?",
    [id, password],
    (err, result) => {
      if (err) {
        console.log(err);
      } else {
        if (result.length > 0) {
          // response.data.result = "success";
          res.send("success");
        } else {
          res.send(result);
        }
      }
    }
  );
});

app.post("/api/writePost", (req, res) => {
  connection.query(
    "INSERT INTO post (title, content, date) VALUES (?, ?, ?)",
    [req.body.title, req.body.content, new Date().toLocaleString()],
    (err, result) => {
      if (err) {
        console.log(err);
        res.send(err);
      } else {
        console.log(result);
        res.send("success");
      }
    }
  );
});

app.post("/api/editPost", (req, res) => {
  connection.query(
    "UPDATE post SET title = ?, content = ?, date = ? WHERE id = ?",
    [req.body.title, req.body.content, req.body.date, req.body.id],
    (err, result) => {
      if (err) {
        console.log(err);
      } else {
        console.log(
          req.body.title,
          req.body.content,
          req.body.date,
          req.body.id
        );
        console.log(result);
        res.send("success");
      }
    }
  );
});

// delete post
app.post("/api/deletePost", (req, res) => {
  connection.query(
    "DELETE FROM post WHERE id = ?",
    [req.body.id],
    (err, result) => {
      if (err) {
        console.log(err);
        res.send(err);
      } else {
        console.log(result);
        res.send("success");
      }
    }
  );
});

// show post list
app.post("/api/getPostList", (req, res) => {
  connection.query("SELECT * FROM post", (err, result) => {
    if (err) {
      console.log(err);
    } else {
      console.log(result);
      res.send(result);
    }
  });
});

// show post detail
app.post("/api/getPostDetail", (req, res) => {
  connection.query(
    "SELECT * FROM post WHERE id = ?",
    [req.body.id],
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

app.post("/api/setGameList", (req, res) => {
  const { name, cpu, drive, vga, os, ram } = req.body;

  connection.query(
    "INSERT INTO gameList (name, intelCpu, amdCpu, drive, external_vga, internal_vga, os, ram) VALUES (?, ?, ?, ?, ?, ?, ?)",
    [name, cpu.intel, cpu.amd, drive, vga.external, vga.internal, os, ram],
    (err, result) => {
      if (err) {
        console.log(err);
      } else {
        console.log(result);
        res.send("success");
      }
    }
  );
});

app.post("/api/getGameList", (req, res) => {
  connection.query("SELECT * FROM gameList", (err, result) => {
    if (err) {
      console.log(err);
    } else {
      // in result remove id
      result.forEach((item) => {
        delete item.id;
      });

      // cpu object in amd and intel
      result.forEach((item) => {
        item.cpu = {
          amd: item.amdCpu,
          intel: item.intelCpu,
        };
        delete item.amdCpu;
        delete item.intelCpu;
      });

      console.log(result);
      res.send(result);
    }
  });
});

// start server
app.listen(port, () => console.log(`내컴퓨터.com listening on port ${port}!`));
