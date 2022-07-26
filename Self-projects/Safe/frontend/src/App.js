import React from "react"
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom"
import Form from "./pages/Form"
import Home from "./pages/Home"

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/form" element={<Form />} />
      </Routes>
    </Router>
  )
}

export default App
