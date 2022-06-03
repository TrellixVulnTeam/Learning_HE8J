# MongoDB models
```js
const mongoose = require("mongoose")

const userSchema = new mongoose.Schema(
	{
		username: {type: String, required: true, unique: true},
		email : {type: String, required: true, unique: true},
		password: {type: String, required: true},
		isAdmin: {type: boolean, default: false}
	}, {timestamps: true}
)

module.exports = mongoose.model("User", userSchema)
```

1. remember to do the timestamps: true
2. remember to export
3. when we import remember to put the whole path!