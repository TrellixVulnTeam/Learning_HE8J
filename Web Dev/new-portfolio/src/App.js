import React from "react"
import styled from "styled-components"
import MainSection from "./MainSection"
import NavigationBar from "./NavigationBar"
import Skills from "./Skills"
import Projects from "./Projects"
import Contact from "./Contact"
import Footer from "./Footer"
const Background = styled.div`
  background-image: url("assets/background.png");
  width: 100%;
  height: 100%;
  content: "";
  display: block;
  z-index: -1;
  position: fixed;
  top: 0;
  left: 0;
  background-size: cover;
`
const App = () => {
  return (
    <div>
      <NavigationBar />
      <MainSection />
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
        {/* <Skills /> */}
        <Background />
        <Projects />
        <Contact />
        {/* <Footer /> */}
      </div>
    </div>
  )
}

export default App
