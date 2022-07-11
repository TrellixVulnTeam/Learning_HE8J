import React from "react"
import Frontpage from "./components/Frontpage"
import Navbar from "./components/Navbar"
import Skills from "./components/Skills"

const App = () => {
  return (
    <div>
      <div className="bg-gradient bg-no-repeat bg-stretch">
        <Navbar />
        <Frontpage />
      </div>
      <Skills />
    </div>
  )
}

export default App
