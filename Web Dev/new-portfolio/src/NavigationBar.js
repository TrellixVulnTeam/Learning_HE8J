import React from "react"
import styled from "styled-components"

const Container = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  background-color: black;
`

const Tab = styled.div`
  padding: 14px 20px;
  transition: 0.2s ease-in;
  font-weight: 800;
  color: white;
  &:hover {
    background-color: white;
    color: black;
    cursor: pointer;
  }
`

const NavigationBar = () => {
  return (
    <Container>
      <div style={{ display: "flex" }}>
        <Tab>Home</Tab>
        <Tab>Skills</Tab>
        <Tab>Projects</Tab>
        <Tab>Contact</Tab>
      </div>
      {/* <div>Right</div> */}
    </Container>
  )
}

export default NavigationBar
