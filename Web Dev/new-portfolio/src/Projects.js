import React from "react"
import styled from "styled-components"

const Container = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 70vh;
`

const InnerContainer = styled.div`
  display: flex;
  flex-direction: column;
  width: 80%;
  height: 40%;
  align-items: center;
  justify-content: space-between;
  padding: 20px 40px;
`
const Gallery = styled.div`
  display: flex;
  flex-direction: row;
  width: 30%;
  justify-content: space-between;
`

const Card = styled.div`
  height: 50px;
  width: 50px;
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
`
const Projects = () => {
  return (
    <Container>
      <InnerContainer>
        Projects
        <Gallery>
          <Card>Hello</Card>
          <Card>Hello</Card>
          <Card>Hello</Card>
        </Gallery>
      </InnerContainer>
    </Container>
  )
}

export default Projects
