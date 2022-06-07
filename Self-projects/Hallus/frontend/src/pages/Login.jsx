import React from "react"
import styled from "styled-components"

const Container = styled.div`
  display: flex;
  justify-content: space-between;
  padding: 15px;
  height: 80vh;
  align-items: center;
  border-bottom: 1px solid lightgray;
`
const FormContainer = styled.form`
  width: 60%;
  margin: auto;
  height: 20%;
  display: flex;
  flex-direction: column;
  border: 1px red solid;
  border-radius: 10px;
  padding: 25px;
  justify-content: space-between;
`
const Input = styled.div`
  display: flex;
  justify-content: space-between;
`
const Login = () => {
  return (
    <Container>
      <FormContainer>
        <Input>
          <label>Username</label>
          <input></input>
        </Input>
        <Input>
          <label>Password</label>
          <input></input>
        </Input>
      </FormContainer>
    </Container>
  )
}

export default Login
