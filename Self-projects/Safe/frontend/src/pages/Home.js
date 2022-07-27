import React from "react"
import styled from "styled-components/macro"
import { motion } from "framer-motion"

import Header from "../components/Header"
import Dashboard from "../components/Dashboard/Dashboard"
import Transactions from "../components/Transactions/Transactions"

import { Fab, Zoom } from "@mui/material"
import AddIcon from "@mui/icons-material/Add"
import { useNavigate } from "react-router-dom"

const Container = styled.div`
  display: flex;
  flex-direction: column;
  padding: 35px 35px;
  background-color: #292929;
  height: 100vh;
  overflow: hidden;
`

const Home = () => {
  const navigate = useNavigate()
  const onClick = () => {
    navigate("/form")
  }

  return (
    <>
      <Container>
        <motion.div
          transition={{ duration: 0.1 }}
          initial={{ opacity: 0.7, x: "100vw" }}
          animate={{ opacity: 1, x: "0vw" }}
          exit={{ x: "100vw" }}
        >
          <Header />
          <Dashboard />
          <Transactions />
        </motion.div>
      </Container>
      <Zoom in style={{ transitionDelay: "50ms" }}>
        <Fab
          onClick={onClick}
          size="medium"
          style={{ position: "absolute", bottom: "25px", right: "20px", backgroundColor: "#5EEAD1", color: "black" }}
        >
          <AddIcon fontSize="large" htmlColor="#55EAD1" />
        </Fab>
      </Zoom>
    </>
  )
}

export default Home
