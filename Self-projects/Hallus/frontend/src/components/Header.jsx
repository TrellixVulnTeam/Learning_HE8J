import React from "react"
import styled from "styled-components"
import MenuIcon from "@mui/icons-material/Menu"
import SendIcon from "@mui/icons-material/Send"
import { IconButton } from "@mui/material"

const Container = styled.div`
  display: flex;
  justify-content: space-between;
  padding: 15px;
  align-items: center;
  border-bottom: 1px solid lightgray;
`
const Left = styled.div``
const Logo = styled.h2``
const Right = styled.div``

const Header = () => {
  return (
    <Container>
      <IconButton>
        <MenuIcon />
      </IconButton>
      <Logo> Logo </Logo>
      <IconButton>
        <SendIcon />
      </IconButton>
    </Container>
  )
}

export default Header
