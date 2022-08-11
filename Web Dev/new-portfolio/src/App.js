import React from "react"
import styled from "styled-components"
import MainSection from "./MainSection"
import NavigationBar from "./NavigationBar"
import Skills from "./Skills"
import Projects from "./Projects"
import Contact from "./Contact"
import Footer from "./Footer"

const App = () => {
  return (
    <div style={{ backgroundColor: "grey" }}>
      <NavigationBar />
      <MainSection />
      {/* <Skills /> */}
      <Projects />
      <Contact />
      <Footer />
    </div>
  )
}

export default App
