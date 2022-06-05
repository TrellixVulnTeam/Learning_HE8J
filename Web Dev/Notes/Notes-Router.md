# Router

1. imports the packages
2. create pages inside src
3. in main App wrap using router
4. Wrap idvd Route inside Routes
5. if there are parameters, useNavigate, useParams
   let navigate = useNavigate(), let {whateverparams} = useParams()

---

## App.js

```js
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom"
import { Home } from "./pages/Home"
import { About } from "./pages/About"
import { Profile } from "./pages/Profile"
import { Error } from "./pages/Error"
function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/profile/Jeniffer">Profile</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/profile/:username" element={<Profile />} />
        <Route path="*" element={<Error />} />
      </Routes>
    </Router>
  )
}

export default App
```

---

## Profile.js

```js
import { useNavigate, useParams } from "react-router-dom"
export const Profile = () => {
  let navigate = useNavigate()
  let { username } = useParams()

  return (
    <div>
      This is the profile page for {username}! Profile
      <button onClick={() => navigate("/about")}>Change to about page</button>
    </div>
  )
```

## Nested routes
We need to use <Outlet/> so that it renders the nested route
[React Router 6: Nested Routes (robinwieruch.de)](https://www.robinwieruch.de/react-router-nested-routes/#:~:text=Nested%20Routes%20are%20a%20powerful,based%20on%20the%20current%20route.)

```js
// in User.js
import { Routes, Route, Link, Outlet } from 'react-router-dom';

...

const User = () => {
  return (
    <>
      <h1>User</h1>

      <nav>
        <Link to="profile">Profile</Link>
        <Link to="account">Account</Link>
      </nav>

      <Outlet />
    </>
  );
};

// in Main App file
const App = () => {
  return (
    <>
      <h1>React Router</h1>

      <nav>
        <Link to="/home">Home</Link>
        <Link to="/user">User</Link>
      </nav>

      <Routes>
        <Route index element={<Home />} />
        <Route path="home" element={<Home />} />
        <Route path="user" element={<User />}>
          <Route path="profile" element={<Profile />} />
          <Route path="account" element={<Account />} />
        </Route>
        <Route path="*" element={<NoMatch />} />
      </Routes>
    </>
  );
};

```

# Conditional 
Let's say if user is logged in, if we go "/login" we want to be redifected to the dashboard. 
```js
<Route path="/login" element={user ? <Navigate to="/" replace /> : <Login />} />
```
### Replace
Normally a call to navigate will push a new entry into the history stack so the user can click the back button to get back to the page. If you pass replace: true to navigate then the current entry in the history stack will be replaced with the new one.


# Link
Adds a clickable thing to your card!
```js
const CategoryItem = ({ item }) => {
  return (
    <Container>
      <Link to={`/products/${item.cat}`}>
        <Image src={item.img} />
        <Info>
          <Title>{item.title}</Title>
          <Button>SHOP NOW</Button>
        </Info>
      </Link>
    </Container>
  )
}

```


Either use `onClick = {()=> navigate("/about")})`
or can wrap button with `<Link> </Link>`