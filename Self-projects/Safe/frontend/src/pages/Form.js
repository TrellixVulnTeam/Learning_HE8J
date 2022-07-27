import React, { useState } from "react"
import styled from "styled-components/macro"
import { motion } from "framer-motion"

import { ButtonBase, Fab, Zoom } from "@mui/material"
import CheckIcon from "@mui/icons-material/Check"
import { useNavigate } from "react-router-dom"

import "./Dropdown.css"
import { OptionUnstyled, SelectUnstyled } from "@mui/base"
import "../components/Transactions/Ripple.css"
import {
  InputContainer,
  SmallInput,
  DropdownItem,
  DropDownContainer,
  BasicDiv,
  Container,
  InnerContainer,
  Background,
  Title,
  Image,
  TitleInput,
} from "./forms.styled"

const Input = ({ placeholder, value, setValue, onClick }) => {
  return (
    <InputContainer onClick={onClick}>
      <SmallInput value={value} placeholder={placeholder} />
    </InputContainer>
  )
}
const MenuItem = ({ value, onClick, setValue }) => {
  return (
    <ButtonBase
      onClick={() => {
        setValue(value)
        onClick()
      }}
      style={{ justifyContent: "flex-start" }}
    >
      <DropdownItem>{value}</DropdownItem>
    </ButtonBase>
  )
}

const Dropdown = ({ choices, onClick, setValue }) => {
  return (
    <DropDownContainer>
      {choices.map((choice) => (
        <MenuItem onClick={onClick} value={choice} setValue={setValue} />
      ))}
    </DropDownContainer>
  )
}

const choices = ["DBS", "HSBC", "Maybank"]

const InnerForm = () => {
  const [visible, setVisible] = useState(true)
  const [value, setValue] = useState("")
  const [CRDB, setCRDB] = useState("CR")
  const [amount, setAmount] = useState(0)

  return (
    <>
      <InputContainer>
        <SmallInput onChange={(e) => setAmount(e.target.value)} placeholder="$12,000" />
        <BasicDiv onClick={() => setCRDB(CRDB === "CR" ? "DB" : "CR")}>{CRDB}</BasicDiv>
      </InputContainer>
      <Input
        value={value}
        placeholder="DBS"
        onClick={() => {
          console.log(visible)
          setVisible(!visible)
        }}
      />
      {visible && (
        <Dropdown
          choices={choices}
          onClick={() => {
            setVisible(!visible)
          }}
          setValue={setValue}
        />
      )}
      <Input placeholder="Description" />
    </>
  )
}
const Form = () => {
  const navigate = useNavigate()
  const [name, setName] = useState(" ")
  const [tag, setTag] = useState(" ")
  const onClick = () => {
    navigate("/")
  }
  return (
    <>
      <Container>
        <motion.div transition={{ duration: 0.1 }} initial={{ y: "50vh" }} animate={{ y: "0vh" }} exit={{ y: "100vh" }}>
          <InnerContainer>
            <Background>
              <Title>
                <Image />
                <div style={{ display: "flex", flexDirection: "column" }}>
                  <TitleInput onChange={(e) => setName(e.target.value)} placeholder="Caifan" />
                  <TitleInput
                    onChange={(e) => setTag(e.target.value)}
                    placeholder="Food"
                    style={{ fontSize: "20px", fontWeight: 400, color: "black", fontFamily: "Inter" }}
                  />
                </div>
              </Title>

              {/* Inner Form */}
              <InnerForm />
            </Background>
          </InnerContainer>
        </motion.div>
      </Container>

      <Zoom in style={{ transitionDelay: "50ms" }}>
        <Fab
          onClick={onClick}
          size="medium"
          style={{ position: "absolute", bottom: "25px", right: "20px", backgroundColor: "#5EEAD1", color: "black" }}
        >
          <CheckIcon fontSize="large" htmlColor="#55EAD1" />
        </Fab>
      </Zoom>
    </>
  )
}

export default Form
