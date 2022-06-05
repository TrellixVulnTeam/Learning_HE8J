
## Handling multiple inputs in one state
```jsx
<div className="addProductItem">
    <label>Description</label>
	<input
            name="desc"
            type="text"
            placeholder="description..."
            onChange={handleChange}
    />
</div>
<div className="addProductItem">
    <label>Price</label>
    <input
            name="price"
            type="number"
            placeholder="100"
            onChange={handleChange}
    />
</div>

const handleChange = (e) => {
    setInputs((prev) => {
      return { ...prev, [e.target.name]: e.target.value };
    });
  };


```

## Splitting inputs
```jsx
const handleCat = (e) => {
    setCat(e.target.value.split(","));
  };
```