Routes - auth.js, user. js...

## Auth.js
```js
const router = require("express").Router()
const User = require ("../models/User")


router.post("/register", async(req, res) => {
	const newUser = new User({
		username: req.body.username,
		email: req.body.email,
		password: req.body.password, 
	})
	try {
		const savedUser = await newUser.save()
		res.status(201).json(savedUser)
	}catch(err) {
		res.status(500).json(err)
	}
})

module.exports = router
```

## Creating a route
1. Send a request
2. create an object
3. remember to call `newUser.save()`
4. Wrap in try-catch block
5. Send a response using the following format : `res.status(201).json(savedUser) 
6. error `res.status(500).json(err)`
7. in main app write 
```js 

const authRoute = require("./routes/auth")`
app.use("/api/auth", authRoute)

```

 `

### Promises
Since newUser.save() is a promise, we need to make it an async function so it will wait for it to finish!

## Passwords
Encrypt our passwords, even in our database, we don't store pw directly
Hash your passwords! 
Use **crypto.js**

1. `yarn add cryptojs`
2. in auth.js, `const CryptoJS = require("CryptoJS)"`
3. password: CryptoJS.AES.encrypt("password123", secret_key)
4. best if we store the secret_key in our env file
	1. in .env, `PASS_SEC` = batman
	2. password: CryptoJS.AES.encrypt("password123", process.env.PASS_SEC)

## Login
```js
// LOGIN
router.post("/login", async(req, res) => {
	try {
		const user = await User.findOne(
		{username: req.body.username})

		!user

		const hashedPasswrod = CryptoJS.AES.decrypt(user.password, process.env.PASS_SEC)
		const password = hashedPassword.toString(CryptoJS.enc.Utf8)
		
	} catch(err) {
		res.status(500).json(err)
	}

})
```
1. when returning the reponse, we don't return the whole user, just everything except password! hence we use the spread operator
2. the `user._doc` is because mongo db stores the user inside `._doc`


