import React from "react"
import styled from "styled-components"

const Container = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 70%;
  max-width: 1000px;
`
const InnerContainer = styled.div`
  width: 95%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 40px 40px;
  border-radius: 20px;
  height: 60%;
  background-color: black;

  @media (max-width: 1024px) {
    flex-direction: column;
  }
`
const InputForm = styled.div`
  width: 65%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-end;
  height: 100%;
  @media (max-width: 1024px) {
    width: 100%;
  }
`
const InputContainer = styled.div`
  width: 100%;
  height: 20%;
  border-radius: 10px;
  background-color: white;
  padding: 10px;
`
const MessageContainer = styled(InputContainer)`
  height: 50%;
`
const Header = styled.div`
  width: 20%;
  color: white;
  font-weight: 1000;
  font-size: 40px;
  margin-right: 10px;
  margin-bottom: 20px;
`
const Contact = () => {
  return (
    <Container id="contact">
      <InnerContainer>
        <Header>Contact me.</Header>
        <InputForm>
          <InputContainer>Name</InputContainer>
          <InputContainer>Email</InputContainer>
          <MessageContainer>Message</MessageContainer>
        </InputForm>
      </InnerContainer>
    </Container>
  )
}

export default Contact
