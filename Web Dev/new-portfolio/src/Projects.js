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
  {
    title: "Safe (WIP)",
    description:
      "Safe is a personal finance app, made for daily budgeting. It supports multi-wallet capability, and data-analytics to inform users about their spendings. It supports basic filtering of categories/accounts. Future capabilities include receipt-scanning, and excel exporting for a clearer view.",
    imageURL: "",
    link: "assets/safe.png",
    skills: ["React", "Redux", "Django"],
  },
  {
    title: "RTOS Car",
    description:
      "This Real-Time-Operating-System car is built on the Freedom KL25Z. It supports self-navigation around an obstacle, while simultaneously outputting different audio/lights depending on its position.",
    imageURL: "",
    link: "assets/rtos.png",
    skills: ["RTOS", "Baremetal", "Python"],
  },
  {
    title: "FPGA Timer/ Mapper",
    description: "testing",
    imageURL:
      "This project is built on the Basys-3 FPGA board, with a 0.96' OLED display and a small microphone. It supports multi-mode through the use of on-board switch combination. There are two modes : a clap activated timer and stopwatch, and a hiking-aid that helps to keep track of current position. Built by me and my schoolmate, Dillon",
    link: "assets/ee2026.png",
    skills: ["Verilog", "Python", "Embedded Systems"],
  },
  {
    title: "ROS Infrared Target Detection + Automatic Mapping Robot",
    description:
      "Accomplished a	raspberry-pi	powered,	ROS2	programmed	Turtlebot	that	navigates	itself	through	an	area	and	produces	a	complete	map,	while	shooting	a	ping-pong	ball	at	any	infrared	target	detected. Led the	design	of	the	shooting	mechanism	and	the	integration	to	the	bot,	CAD-ed	using	Solidworks. Aided	in	the	programming	of	the	detection	and	threshold	measurement	to	ensure	accurate	result",
    imageURL: "",
    link: "assets/turtlebot.png",
    skills: ["ROS", "Python", "Solidworks"],
  },
  {
    title: "Halpmi",
    description:
      "HALPMI is a Command Line Interface (CLI) Application that allows administrators in clinics to manage the clinic's day-to-day administrative tasks. More specifically, using HALPMI the user is able to insert new information regarding Doctors, Patients and Medication. Users can also schedule appointment for Patients with Doctors. Users are also able to track stocks of medications.",
    imageURL: "",
    link: "assets/halpmi.png",
    skills: ["CSS", "JS"],
  },
]

const cards = projects.map((project) => (
  <ProjectCard title={project.title} description={project.description} skills={project.skills} link={project.link} />
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
            <div style={{ width: "40%" }}>RTOS car</div>
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
