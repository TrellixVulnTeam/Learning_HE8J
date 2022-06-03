const router = require("express").Router()
const User = require("../models/User")

const jwt = require("jsonwebtoken")
const CryptoJS = require("crypto-js")

// Register
router.post("/register", async (req, res) => {
  const newUser = new User({
    username: req.body.username,
    email: req.body.email,
    password: CryptoJS.AES.encrypt(req.body.password, process.env.PASS_SEC).toString(),
  })
  try {
    const savedUser = await newUser.save()
    res.status(201).json(savedUser)
  } catch (err) {
    res.status(500).json(err)
  }
})

// LOGIN
router.post("/login", async (req, res) => {
  try {
    const user = await User.findOne({ username: req.body.username })

    // if there is no user then do the right thing
    !user && res.status(401).json("Wrong Credentials")

    const hashedPassword = CryptoJS.AES.decrypt(user.password, process.env.PASS_SEC)
    const dbPassword = hashedPassword.toString(CryptoJS.enc.Utf8)

    dbPassword !== req.body.password && res.status(401).json("Wrong credentials")

    const accessToken = jwt.sign(
      {
        id: user.id,
        isAdmin: user.isAdmin,
      },
      process.env.JWT_SEC,
      { expiresIn: "3d" }
    )

    const { password, ...others } = user._doc

    // we do this such that the password is not revealed in the response
    res.status(200).json({ ...others, accessToken })
  } catch (err) {
    res.status(500).json("There is an error")
  }
})

module.exports = router
