import React from "react"
import styled from "styled-components/macro"

const Container = styled.div`
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-bottom: 20px;
  color: white;
  font-size: 20px;
  font-family: "Inter";
  height: 10%;

  > h1 {
    font-size: 40px;
    font-weight: 700;
  }
`

const Header = () => {
  return (
    <Container>
      <div>Hello,</div>
      <h1>Tai</h1>
    </Container>
  )
}

export default Header
