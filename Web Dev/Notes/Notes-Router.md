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
