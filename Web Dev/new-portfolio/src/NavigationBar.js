import { Download } from "@mui/icons-material"
import React, { useState } from "react"
import styled from "styled-components"
import Footer from "./Footer"

const Container = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  background-color: black;
  position: fixed;
  width: 100%;
  z-index: 99;
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
  font-size: 20px;
  display: flex;
  align-items: center;
`
const scroll = (id) => {
  const section = document.querySelector(id)
  section.scrollIntoView({ behavior: "smooth", block: "start" })
}

const NavigationBar = () => {
  const onDownload = () => {
    const link = document.createElement("a")
    link.download = "resume.pdf"
    link.href = "/assets/Resume2022.pdf"
    link.target = "_blank"
    link.click()
  }
  return (
    <Container>
      <div style={{ display: "flex" }}>
        <Tab onClick={() => scroll("#home")}>Home</Tab>
        <Tab>Skills</Tab>
        <Tab onClick={() => scroll("#projects")}>Projects</Tab>
        <Tab onClick={() => scroll("#contact")}>Contact</Tab>
        <Tab onClick={onDownload}>
          <Download /> Resume
        </Tab>
      </div>
      <Footer />
    </Container>
  )
}

export default NavigationBar
