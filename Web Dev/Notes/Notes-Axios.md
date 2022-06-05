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

## Axios with token
in requestMethods. js in src
```js


import axios from "axios";

const BASE_URL = "http://localhost:5000/api/";
// const TOKEN =
//   JSON.parse(JSON.parse(localStorage.getItem("persist:root")).user).currentUser
//     .accessToken || "";

const user = JSON.parse(localStorage.getItem("persist:root"))?.user;
const currentUser = user && JSON.parse(user).currentUser;
const TOKEN = currentUser?.accessToken;

export const publicRequest = axios.create({
  baseURL: BASE_URL,
});

export const userRequest = axios.create({
  baseURL: BASE_URL,
  header: { token: `Bearer ${TOKEN}` },
});
```

To use
```js
some async funtion 

a = asynce () => 

try{
	const data = await publicRequest.get('/products')
}catch(err) {

} 
```

Remember to use try catch, and async await

Axios interceptors to refresh token

```jsx

const axiosJWT = axios.create()
axiosJWT.interceptors.request.use(
    async (config) => {
      let currentDate = new Date();
      const decodedToken = jwt_decode(user.accessToken);
      if (decodedToken.exp * 1000 < currentDate.getTime()) {
        const data = await refreshToken();
        config.headers["authorization"] = "Bearer " + data.accessToken;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );
```