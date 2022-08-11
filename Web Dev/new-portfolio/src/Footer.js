import { Facebook, GitHub, Instagram, LinkedIn } from "@mui/icons-material"
import { Button, Fab } from "@mui/material"
import React from "react"
import styled from "styled-components"

const Container = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 20px 40px;
`
const SocialMediaRight = styled.div`
  width: 80px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
`
const SocialIcons = ({ children }) => {
  return <Fab sx={{ height: "8px", width: "35px", borderRadius: 8, color: "black" }}>{children}</Fab>
}
const Footer = () => {
  return (
    <Container>
      <div>{""}</div>
      <SocialMediaRight>
        <SocialIcons>
          <LinkedIn />
        </SocialIcons>
        <SocialIcons>
          <GitHub />
        </SocialIcons>
      </SocialMediaRight>
    </Container>
  )
}

export default Footer
