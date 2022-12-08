// express server
const express = require("express");
const app = express();
const port = process.env.PORT;

// serve static files
app.use(express.static("public"));

app.get("/", (req, res) => res.send("Hello World!"));

// start server
app.listen(port, () => console.log(`Example app listening on port ${port}!`));
