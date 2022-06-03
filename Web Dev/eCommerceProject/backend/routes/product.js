const router = require("express").Router()
const Product = require("../models/Product")
const { verifyTokenAndAuthorization, verifyTokenAndAdmin } = require("./verifyToken")

// CREATE
router.post("/", verifyTokenAndAuthorization, async (req, res) => {
  const newProduct = new Product(req.body)
  try {
    const savedProduct = await newProduct.save()
    res.status(200).json(savedProduct)
  } catch (err) {
    res.status(500).json(err)
  }
})

// GET ALL
router.get("/", verifyTokenAndAdmin, async (req, res) => {
  const qNew = req.query.new
  const qCategory = req.query.category
  try {
    let products
    if (qNew) {
      products = await Product.find().sort({ createdAt: -1 }).limit(5)
    } else if (qCategory) {
      products = await Product.find({ category: { $in: [qCategory] } })
    }
    res.status(200).json(products)
  } catch (err) {
    res.status(500).json(err)
  }
})

// GET BY ID
router.get("/find/:id", verifyTokenAndAdmin, async (req, res) => {
  try {
    const product = await Product.findById(req.params.id)
    res.status(200).json(product)
  } catch (err) {
    res.status(500).json(err)
  }
})

module.exports = router
