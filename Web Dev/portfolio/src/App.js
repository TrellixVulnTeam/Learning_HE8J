import React from "react"
import Frontpage from "./components/Frontpage"
import Navbar from "./components/Navbar"
import Aboutme from "./components/Aboutme"

const App = () => {
  return (
    <div>
      <div className="bg-gradient bg-no-repeat bg-stretch">
        <Navbar />
        <Frontpage />
      </div>
      <Aboutme />
    </div>
  )
}

export default App
