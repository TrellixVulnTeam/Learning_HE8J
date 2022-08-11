import React from "react"

import styled from "styled-components"
import Picture from "./assets/comp-logo.png"

const Container = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 10px 40px;
  height: 70vh;
  background-color: white;
  color: black;
  border-radius: 0 0 0 0;
`
const InnerContainer = styled.div`
  width: 100%;
  height: 90%;
  display: flex;
  padding: 0 50px;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  border: 2px solid black;
`
const Image = styled.img`
  height: 40%;
`

const MainSection = () => {
  return (
    <Container>
      <InnerContainer>
        <div>
          <div style={{ fontSize: "20px" }}>
            Hello there, my name is <span style={{ fontWeight: "1000" }}>Tai</span>
          </div>
          <div style={{ fontSize: "30px" }}>I'm a</div>
        </div>
        <Image src={Picture}></Image>
      </InnerContainer>
    </Container>
  )
}

export default MainSection
