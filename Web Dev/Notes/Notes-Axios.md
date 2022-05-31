# Axios

[Axios Cheatsheet](https://gist.github.com/joshuaquek/c259497db73d596517522c1820f480a6)

[Axios Free Code Camp](https://www.freecodecamp.org/news/how-to-use-axios-with-react/)

## Simillar to fetch method

```js
const reponse = await axios({
  method: 'post', //you can set what request you want to be
  url: 'https://example.com/request',
  data: {id: varID},
  headers: {
    Authorization: 'Bearer ' + varToken
  }
})
setName(response.data

```

## Axios method

```js
axios.post(
  "https://example.com/postSomething",
  {
    email: varEmail, //varEmail is a variable which holds the email
    password: varPassword,
  },
  {
    headers: {
      Authorization: "Bearer " + varToken,
    },
  }
)
```

## Axios instance

```js

let instance = axios.create({
  headers: {
    post: {        // can be common or any other method
      header1: 'value1'
    }
  }
})

another example
const client = axios.create({
  baseURL: "https://jsonplaceholder.typicode.com/posts"
});
```
