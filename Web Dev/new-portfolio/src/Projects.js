import React, { useState } from "react"
import styled from "styled-components"
import { Dialog, DialogContent, DialogActions, DialogTitle, DialogContentText, Button } from "@mui/material"
import ProjectCard from "./ProjectCard"

const Container = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 95%;
  max-width: 1000px;
`
const Header = styled.div`
  color: white;
  font-weight: 900;
  font-size: 50px;
  text-shadow: 0 0.2rem 0.25rem rgba(0, 0, 0, 0.5);
`
const InnerContainer = styled.div`
  display: flex;
  flex-direction: row;
  width: 100%;
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
  width: 90%;
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
  box-shadow: 0 0.2rem 0.25rem rgba(0, 0, 0, 0.5);
  transition: 0.2s ease-in;

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

const projects = [
  { title: "Safe", description: "testing", imageURL: "", link: "", skills: ["React", "Redux", "Django"] },
  { title: "Autonomous Car", description: "testing", imageURL: "", link: "", skills: ["RTOS", "Baremetal"] },
  {
    title: "FPGA Timer/ Mapper",
    description: "testing",
    imageURL: "",
    link: "",
    skills: ["Verilog", "Python", "Embedded Systems"],
  },
  {
    title: "ROS Infrared Target Detection + Automatic Mapping Robot",
    description: "testing",
    imageURL: "",
    link: "",
    skills: ["ROS", "Python", "Solidworks"],
  },
  { title: "Halpmi", description: "testing", imageURL: "", link: "", skills: ["CSS", "JS"] },
]

const cards = projects.map((project) => (
  <ProjectCard title={project.title} description={project.description} skills={project.skills} />
))

const Projects = () => {
  const [whichModalVisible, setWhichModalVisible] = useState(-1)
  const openModal = (i) => {
    console.log(i)
    setWhichModalVisible(i)
  }
  const closeModal = () => {
    setWhichModalVisible(-1)
  }

  return (
    <Container id="projects">
      <InnerContainer>
        <Header>Projects</Header>
        <Gallery>
          <Card onClick={() => openModal(0)} style={{ gridColumn: "1/6", gridRow: "1/2" }}>
            Safe - personal finance
          </Card>
          {/* <Card style={{ gridColumn: "2/3", gridRow: "2/4" }}>2</Card> */}
          <Card onClick={() => openModal(1)} style={{ gridColumn: "3/5", gridRow: "2/3" }}>
            <div style={{ width: "40%" }}>Autonomous car</div>
          </Card>
          <Card onClick={() => openModal(2)} style={{ gridColumn: "3/4", gridRow: "3/5" }}>
            FPGA timer/ mapping
          </Card>
          <Card onClick={() => openModal(3)} style={{ gridColumn: "5/6", gridRow: "2/5" }}>
            <div style={{ width: "40%" }}> ROS robot</div>
          </Card>
          <Card onClick={() => openModal(4)} style={{ gridColumn: "1/3", gridRow: "4/5" }}>
            Halpmi
          </Card>
        </Gallery>
      </InnerContainer>
      <Dialog
        open={whichModalVisible !== -1}
        keepMounted
        onClose={closeModal}
        aria-describedby="alert-dialog-slide-description"
        fullWidth
        maxWidth="md"
      >
        {cards[whichModalVisible]}
      </Dialog>
    </Container>
  )
}

export default Projects
