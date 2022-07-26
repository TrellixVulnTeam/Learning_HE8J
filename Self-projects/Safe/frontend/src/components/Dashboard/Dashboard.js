import React from "react"
import styled from "styled-components/macro"
import Graph from "./Graph"

const Container = styled.div`
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 25%;
  background-color: #d9d9d9;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  margin-bottom: 20px;
  padding: 18px 20px 10px 20px;
`
const GraphContainer = styled.div`
  height: 90px;
  overflow-x: scroll;
`

const Dashboard = () => {
  return (
    <Container>
      <div>
        <div style={{ color: "black" }}>Total Balance</div>
        <h1 style={{ color: "black", fontFamily: "Inter" }}>$12,000</h1>
      </div>
      <GraphContainer>
        <Graph />
      </GraphContainer>
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <div style={{ color: "#EC7474", fontWeight: 500 }}>↓ $500</div>
        <div style={{ color: "#6AC5B4", fontWeight: 500 }}>↑ $500</div>
      </div>
    </Container>
  )
}

export default Dashboard
