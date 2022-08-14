import React from "react"
import styled from "styled-components"
import MainSection from "./MainSection"
import NavigationBar from "./NavigationBar"
import Skills from "./Skills"
import Projects from "./Projects"
import Contact from "./Contact"
import Footer from "./Footer"
import { Parallax, Background } from "react-parallax"

const Background2 = styled.div`
  background-image: url("assets/background.png");
  /* background-image: url("assets/bg2.jpg"); */
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
  scroll-snap-type: y mandatory;
  background-image: url("assets/background.png");
  /* background-image: url("assets/bg2.jpg"); */
  background-size: cover;

  > * > * {
    scroll-snap-align: start;
  }
`
const App = () => {
  return (
    <div>
      <NavigationBar />

      <InnerContainer>
        {/* <Background /> */}
        {/* <Parallax style={{ width: "100%" }} bgImage="assets/bg2.jpg" strength={-100}> */}
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
          <MainSection />
          <Skills />
          <Projects />
          <Contact />
        </div>
        {/* </Parallax> */}
      </InnerContainer>
    </div>
  )
}

export default App
