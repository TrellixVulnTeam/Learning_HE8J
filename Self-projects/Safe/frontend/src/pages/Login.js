import React from "react"
import styled from "styled-components/macro"
import { motion } from "framer-motion"

import Header from "../components/Header"
import Dashboard from "../components/Dashboard/Dashboard"
import Transactions from "../components/Transactions/Transactions"

import { Fab, Zoom } from "@mui/material"
import AddIcon from "@mui/icons-material/Add"
import { useNavigate } from "react-router-dom"
import { InputContainer, SmallInput } from "./forms.styled"
import { ForkRight, NavigateNext } from "@mui/icons-material"

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

const Input = ({ type, placeholder, value, setValue, onClick }) => {
  return (
    <InputContainer onClick={onClick}>
      <SmallInput type={type} value={value} placeholder={placeholder} />
    </InputContainer>
  )
}

const Login = () => {
  const navigate = useNavigate()
  const onClick = () => {
    navigate("/")
  }

  return (
    <>
      <Container>
        <CardContainer style={{ position: "relative" }}>
          <Input placeholder="username" />
          <Input type="password" placeholder="password" />
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
