import React from "react"
import styled from "styled-components"
import { useState } from "react"

const Container = styled.div`
  padding: 5px 10px;
  background-color: ${(props) => (props.isActive ? "white" : "#838282")};
  color: ${(props) => (props.isActive ? "black" : "white")};
  border-radius: 8px;
  :hover {
    cursor: pointer;
  }
`

const TagButton = ({ name, isActive }) => {
  return <Container isActive={isActive}>{name}</Container>
}

export default TagButton
