import { Close, Square, SquareOutlined } from "@mui/icons-material"
import React from "react"

import styled from "styled-components"
import Picture from "./assets/comp-logo.png"

const Container = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding: 60px 40px 10px 40px;
  height: 90vh;
  width: 100%;
  /* background-color: white; */
  color: black;
  border-radius: 0 0 0 0;
`
const InnerContainer = styled.div`
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 92%;
  display: flex;
  padding: 0 50px;

  flex-direction: row;
  justify-content: space-between;
  align-items: center;

  background-color: white;
`

const Text = styled.div`
  display: flex;
  height: fit-content;
  flex-direction: column;

  @media (max-width: 1024px) {
    width: 100%;
  }
`
const Image = styled.img`
  height: 40%;
  @media (max-width: 1024px) {
    visible: hidden;
  }
`
const OuterContainer = styled.div`
  width: 100%;
  height: 90%;
  max-width: 1000px;
  background-color: #383838;
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 0.2rem 0.25rem rgba(0, 0, 0, 0.2);
`

const MainSection = () => {
  return (
    <Container id="home">
      <OuterContainer>
        <div style={{ color: "white", position: "absolute", right: "10px", top: "15px" }}>
          <SquareOutlined />
          <Close />
        </div>
        <InnerContainer>
          <Text>
            <div style={{ fontSize: "20px", fontFamily: "Fira Mono" }}>
              Hello there, my name is <span style={{ fontWeight: "1000" }}>Tai</span>
            </div>
            <div style={{ fontSize: "30px", marginBottom: "20px" }}>I'm a software engineer.</div>
            <div>
              <div style={{ fontSize: "15px", width: "70%" }}>
                Currently, I'm a penultimate Computer Engineering student studying in NUS.
              </div>
              <div style={{ fontSize: "15px", width: "70%" }}>
                My interests include AI/ML, Robotics, IOT, Trading, Anime, Startups and Guitar. I am actively looking
                for internship and freelancing opportunities!
              </div>
            </div>
          </Text>
          <Image src={Picture}></Image>
        </InnerContainer>
      </OuterContainer>
    </Container>
  )
}

export default MainSection
