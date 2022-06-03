we can do /user/find/1?new=true
the **new=true** is called our query

in our code we do something like
```js
let products
    if (qNew) {
      products = await Product.find().sort({ createdAt: -1 }).limit(5)
    } else if (qCategory) {
      products = await Product.find({ category: { $in: [qCategory] } })
    }
```