import React, { useState } from "react"
import styled from "styled-components"
import { Modal, Box, Typography } from "@mui/material"

const Container = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100%;
  max-width: 1000px;
`
const Header = styled.div`
  color: white;
  font-weight: 900;
  font-size: 35px;
`
const InnerContainer = styled.div`
  display: flex;
  flex-direction: column;
  width: 90%;
  height: 80%;
  align-items: center;
  justify-content: space-between;
  padding: 20px 40px;
`
const Gallery = styled.div`
  margin-top: 30px;
  display: grid;
  grid-template-rows: repeat(20px, 6);
  grid-template-columns: repeat(20px, 6);
  grid-row-gap: 5px;
  grid-column-gap: 5px;
  width: 100%;
  height: 80%;
`

const Card = styled.div`
  height: 100%;
  background-color: white;
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0px;
  font-size: 20px;
  font-weight: 900;
  text-align: center;

  position: relative;
  &:hover {
    cursor: pointer;
    background-color: #69c2a1;
    color: white;
    /* &:after {
      transition: 0.5s ease-in;
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      bottom: 0;
      right: 0;
      background-color: rgba(0, 0, 0, 0.1);
    } */
  }
`

const ModalCard = styled.div``

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 400,
  bgcolor: "background.paper",
  border: "2px solid #000",
  boxShadow: 24,
  p: 4,
}

const Projects = () => {
  const [whichModalVisible, setWhichModalVisible] = useState(0)
  const openModal = (i) => {
    console.log(i)
    setWhichModalVisible(i)
  }
  const closeModal = () => {
    setWhichModalVisible(0)
  }

  return (
    <Container id="projects">
      <InnerContainer>
        <Header>Projects</Header>
        <Gallery>
          <Card onClick={() => openModal(1)} style={{ gridColumn: "1/6", gridRow: "1/2" }}>
            Safe - personal finance
          </Card>
          {/* <Card style={{ gridColumn: "2/3", gridRow: "2/4" }}>2</Card> */}
          <Card style={{ gridColumn: "3/5", gridRow: "2/3" }}>
            <div style={{ width: "40%" }}>Autonomous car</div>
          </Card>
          <Card style={{ gridColumn: "3/4", gridRow: "3/5" }}>FPGA timer/ mapping</Card>
          <Card style={{ gridColumn: "5/6", gridRow: "2/5" }}>
            <div style={{ width: "40%" }}> ROS robot</div>
          </Card>
          <Card style={{ gridColumn: "1/3", gridRow: "4/5" }}>Halpmi</Card>
        </Gallery>
      </InnerContainer>
      <Modal
        open={whichModalVisible === 1}
        onClose={closeModal}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Text in a modal
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
          </Typography>
        </Box>
      </Modal>
    </Container>
  )
}

export default Projects
