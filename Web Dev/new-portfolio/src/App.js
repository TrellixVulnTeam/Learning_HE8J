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

const InnerContainer = styled.div`
  height: 100vh;
  overflow-y: scroll;
  scroll-snap-type: y proximity;

  > * > * {
    scroll-snap-align: start;
  }
`
const App = () => {
  return (
    <div>
      <NavigationBar />
      <InnerContainer>
        <Background />
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
          <MainSection />
          <Projects />
          <Contact />
        </div>
      </InnerContainer>
    </div>
  )
}

export default App
