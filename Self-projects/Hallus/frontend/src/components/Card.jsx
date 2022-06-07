import React from "react"
import styled from "styled-components"

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid lightgray;
  border-radius: 10px;
  width: 40vw;
  overflow: hidden;
`
const Image = styled.div`
  height: 50%;
  background-color: black;
  width: 100%;
`
const Description = styled.div`
  width: 100%;
  display: flex;
  justify-content: space-between;
  position: relative;
  padding: 5px;
`
const Name = styled.h2``
const Location = styled.div`
  margin-top: auto;
`

const Card = () => {
  return (
    <Container>
      <Image>dfd </Image>
      <Description>
        <div>
          <Name>New Place</Name>
          <Description>this is a nice place</Description>
        </div>
        <div style={{ display: "flex" }}>
          <Location>Clementi</Location>
        </div>
      </Description>
    </Container>
  )
}

export default Card
