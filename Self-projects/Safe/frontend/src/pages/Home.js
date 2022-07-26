import React from "react"
import styled from "styled-components/macro"

import Header from "../components/Header"
import Dashboard from "../components/Dashboard/Dashboard"
import Transactions from "../components/Transactions/Transactions"

const Container = styled.div`
  display: flex;
  flex-direction: column;
  padding: 46px 43px;
  background-color: #292929;
  height: 100vh;
  overflow: hidden;
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
