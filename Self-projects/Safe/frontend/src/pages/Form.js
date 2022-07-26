import React from "react"
import styled from "styled-components"

const Container = styled.div`
  display: flex;
  flex-direction: column;
  background-color: #292929;
  height: 100vh;
  padding-top: 5vh;
  overflow: hidden;
`

const InnerContainer = styled.div`
  height: 95vh;
  position: relative;
  width: 100%;
`

const Background = styled.div`
  background-color: #d9d9d9;
  height: 92.5%;
  border-radius: 20px 20px 0 0;
  padding: 36px;
  z-index: 1;
  width: 100%;
  position: absolute;
  bottom: 0;
  padding-top: 79px;
`
const InputBox = styled.div`
  width: 100%;
  height: 66px;
  border-radius: 10px;
  border: none;
  margin-bottom: 30px;
  background-color: white;
  color: black;
  padding: 23px 20px;
  font-size: 20px;
  font-weight: 700;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  > * {
    color: black;
  }
`
const Image = styled.div`
  width: 107px;
  height: 107px;
  border-radius: 9px;
  background-color: #994c4c;
  margin-right: 16px;
`
const Title = styled.div`
  display: flex;
  position: absolute;
  top: -53px;
`
const Form = () => {
  return (
    <Container>
      <InnerContainer>
        <Background>
          <Title>
            <Image />
            <div style={{ display: "flex", flexDirection: "column" }}>
              <h1 style={{ fontSize: "40px", fontWeight: 700 }}>Caifan</h1>
              <div style={{ fontSize: "20px", fontWeight: 400, color: "black" }}>Food</div>
            </div>
          </Title>
          <InputBox>
            <div>$12000</div>
            <div>CR</div>
          </InputBox>
          <InputBox> DBS</InputBox>
          <InputBox> DBS</InputBox>
        </Background>
      </InnerContainer>
    </Container>
  )
}

export default Form
