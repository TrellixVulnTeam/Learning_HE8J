const express = require("express")
const app = express()
const mongoose = require("mongoose")

// can have different endpoints
const userRoute = require("./routes/user")
const authRoute = require("./routes/auth")

// so that people wouldnt get the url straight
const dotenv = require("dotenv")
dotenv.config()
mongoose
  .connect(process.env.MONGO_URL)
  .then(() => console.log("DB connection successful"))
  .catch((err) => console.log(err))

/* API RELATED */
// this allows us to pass in json object
app.use(express.json())
app.get("/api/test", () => console.log("test is sucessful"))
app.use("/api/user", userRoute)
app.use("/api/auth", authRoute)

app.listen(process.env.PORT || 8008, () => {
  console.log("Backend server is running!")
})
