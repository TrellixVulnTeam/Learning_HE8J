import React from "react"
import styled from "styled-components"

import Header from "../components/Header"
import Dashboard from "../components/Dashboard"
import Transactions from "../components/Transactions"

const Container = styled.div`
  display: flex;
  flex-direction: column;
  padding: 46px 43px;
  background-color: #292929;
  height: 100vh;
`

const index = () => {
  return (
    <Container>
      <Header />
      <Dashboard />
      <Transactions />
    </Container>
  )
}

export default index
