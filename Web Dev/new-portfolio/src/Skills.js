import React from "react"
import styled from "styled-components"

const Container = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 20px 40px;
  height: 100vh;
  width: 100%;
`
const InnerContainer = styled.div`
  background-color: rgba(0, 0, 0, 0.5);
  padding: 0px 20px;
  width: 70%;
  height: 60%;
  margin-top: 10vh;
  display: flex;
  flex-direction: row;
  align-items: center;
  border-radius: 0 30px;

  @media (max-width: 1000px) {
    width: 90%;
    padding: 0px 0px 0 10px;
  }
`

const Bar = styled.div`
  height: 30px;
  border-radius: 20px;
  /* border: 1px solid white; */
  overflow: hidden;
  width: 80%;
  background-color: rgba(255, 255, 255, 0.2);
  @media (max-width: 1000px) {
    width: 60%;
  }
`
const InnerBar = styled.div`
  height: 105%;
  width: ${(props) => props.percentage};
  background-color: #69c2a1;
  border-radius: 0 20px 20px 0;
`
const BarContainer = styled.div`
  display: flex;
  width: 90%;
  flex-direction: column;
  justify-content: space-between;
  padding: 40px 10px;
  align-items: center;
  height: 100%;
`
const SkillBar = ({ skillName, percentage }) => {
  return (
    <div style={{ display: "flex", width: "100%", justifyContent: "space-between", alignItems: "center" }}>
      <h1 style={{ color: "white", fontSize: "22px", width: "%" }}>{skillName}</h1>
      <Bar>
        <InnerBar percentage={percentage} />
      </Bar>
    </div>
  )
}
const Skills = () => {
  return (
    <Container id="skills">
      <InnerContainer>
        <BarContainer>
          <SkillBar skillName="CSS" percentage="70%" />
          <SkillBar skillName="Python" percentage="85%" />
          <SkillBar skillName="Javascript" percentage="80%" />
          <SkillBar skillName="Java" percentage="85%" />
          <SkillBar skillName="C ++ " percentage="75%" />
          <SkillBar skillName="Embedded" percentage="70%" />
        </BarContainer>
        <h1 style={{ fontSize: "45px", textOrientation: "upright", writingMode: "vertical-lr", color: "white" }}>
          SKILLS
        </h1>
      </InnerContainer>
    </Container>
  )
}

export default Skills
