import React, { useState } from "react"
import { useNavigate } from "react-router-dom"

import styled from "styled-components/macro"

import { Fab, Zoom } from "@mui/material"
import { NavigateNext } from "@mui/icons-material"
import Input from "../components/common/Input"
import { useDispatch } from "react-redux"
import { updateUser } from "../redux/apiCalls"

const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 35px 35px;
  background-color: #292929;
  height: 100vh;
  overflow: hidden;
`

const CardContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  width: 100%;
  height: 40%;
  background-color: #d9d9d9;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  margin-bottom: 20px;
  padding: 30px 20px 10px 20px;
`

const Login = () => {
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const onClick = () => {
    updateUser({ username: username, password: password }, dispatch)
  }
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  return (
    <>
      <Container>
        <CardContainer style={{ position: "relative" }}>
          <Input value={username} setValue={setUsername} placeholder="username" />
          <Input value={password} setValue={setPassword} type="password" placeholder="password" />
          <Zoom in style={{ transitionDelay: "50ms" }}>
            <Fab
              onClick={onClick}
              size="medium"
              style={{
                position: "absolute",
                bottom: "25px",
                right: "20px",
                backgroundColor: "#5EEAD1",
                color: "black",
              }}
            >
              <NavigateNext fontSize="large" htmlColor="#55EAD1" />
            </Fab>
          </Zoom>
        </CardContainer>
      </Container>
    </>
  )
}

export default Login
