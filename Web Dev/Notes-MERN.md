# Node

## What is node.js?

Basically it lets your run javascript in a non-browser environment.
To run an app use `node index.js`

To monitor it everytime we make a change use `nodemon index.js`

### To start a project

`yarn add express mongoose dotenv nodemon`
` nodemon index.js`
project
-models
-routes
-.env
-index.js

---

# Express

Express is a webframework, that allows u to make backend calls?

---

# Mongoose (MongoDB)

### How to start

Go to mongodb cloud, start a cluster, allow network access and allow user.
Then press connect and copy thing into code

# dotenv

To store the secrets env dependencies, like your keys, mongodb link etc

---

# Templates

---

## index.js

```
const express = require("express");
const app = express();
const mongoose = require("mongoose");
const dotenv = require("dotenv");
dotenv.config();


<!-- pass in routes -->
const userRoute = require("./routes/user");
const authRoute = require("./routes/auth");
const productRoute = require("./routes/product");
const cartRoute = require("./routes/cart");
const orderRoute = require("./routes/order");
const stripeRoute = require("./routes/stripe");
const cors = require("cors");

<!-- connect database -->
mongoose
  .connect(process.env.MONGO_URL)
  .then(() => console.log("DB Connection Successfull!"))
  .catch((err) => {
    console.log(err);
  });

<!-- use endpoints -->
app.use(cors());
app.use(express.json());
app.use("/api/auth", authRoute);
app.use("/api/users", userRoute);
app.use("/api/products", productRoute);
app.use("/api/carts", cartRoute);
app.use("/api/orders", orderRoute);
app.use("/api/checkout", stripeRoute);

app.listen(process.env.PORT || 5000, () => {
  console.log("Backend server is running!");
});


```

---

## .env

```

```

---

## routes

```
const router = require("express").Router()

// router.get("/usertest", (req, res) => {
//   res.send("user test is sucessful")
// })

// router.post("/userposttest", (req, res) => {
//   const username = req.body.username
//   res.send("your username is: " + username)
// })

```

---

# with models

```
const router = require("express").Router()
const User = require("../models/User")
// REGISTER
router.post("/register", (req, res) => {
  const newUser = new User({ username: req.body.username, email: req.body.email, password: req.body.password })
})
module.exports = router

```

## Models

```
const mongoose = require("mongoose")

const ProductSchema = new mongoose.Schema(
  {
    title: { type: String, required: true, unique: true },
    desc: { type: String, required: true },
    img: { type: String, required: true },
    category: { type: Array },
    size: { type: String },
    color: { type: String },
    price: { type: Number, required: true },
  },
  { timestamps: true }
)

module.exports = mongoose.model("Product", ProductSchema)


```
