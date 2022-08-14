import React from "react"
import styled from "styled-components"
const Container = styled.div`
  height: 65vh;
  width: 70vw;
  display: flex;
  justify-content: space-between;
`
const Description = styled.div`
  width: 50%;
  padding: 20px 30px;
`
const Image = styled.div`
  width: 50%;
  background-size: cover;
  background-image: url("https://media.istockphoto.com/photos/programming-code-abstract-technology-background-of-software-developer-picture-id1224500457?k=20&m=1224500457&s=170667a&w=0&h=XzYyHReOY2K1R-rZeQIUXGHLsOJuFHLYtRL7AWR-6GY=");
`
const Pill = styled.div`
  border-radius: 15px;
  background-color: ${(props) => (props.odd ? "#69c2a1" : "white")};
  color: ${(props) => (props.odd ? "white" : "#69c2a1")};
  border: 1px solid #69c2a1;
  padding: 3px 10px;
  font-size: 18px;
  margin-right: 10px;
`
const ProjectCard = ({ title, description, imageUrl, link, skills }) => {
  return (
    <Container>
      <Description>
        <h1>{title}</h1>
        <div>{description}</div>
        <div style={{ position: "absolute", bottom: "20px", display: "flex" }}>
          {skills.map((skill, index) => (
            <Pill odd={!(index % 2)}>{skill}</Pill>
          ))}
        </div>
      </Description>
      <Image />
    </Container>
  )
}

export default ProjectCard
