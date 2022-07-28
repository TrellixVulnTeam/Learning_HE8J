import React, { useState } from "react"
import { useNavigate } from "react-router-dom"

import { motion } from "framer-motion"

import { ButtonBase, Fab, Zoom } from "@mui/material"
import CheckIcon from "@mui/icons-material/Check"

import "./Dropdown.css"

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
import Input from "../components/common/Input"
import Ripple from "../components/common/Ripple"
import FormDialog from "../components/common/Dialog"

const MenuItem = ({ value, onClick, setValue }) => {
  return (
    <Ripple
      onClick={() => {
        setValue(value)
        onClick()
      }}
      style={{ justifyContent: "flex-start" }}
    >
      <DropdownItem>{value}</DropdownItem>
    </Ripple>
  )
}

const Dropdown = ({ choices, onClick, setValue }) => {
  return (
    <DropDownContainer>
      {choices.map((choice) => (
        <MenuItem onClick={onClick} value={choice} setValue={setValue} />
      ))}
      <MenuItem value=" + Add new account" />
    </DropDownContainer>
  )
}

const choices = ["DBS", "HSBC", "Maybank"]

const InnerForm = () => {
  const [visible, setVisible] = useState(false)
  const [value, setValue] = useState("")
  const [CRDB, setCRDB] = useState("CR")
  const [amount, setAmount] = useState(0)

  return (
    <>
      <InputContainer>
        <SmallInput onChange={(e) => setAmount(e.target.value)} placeholder="$12,000" />
        <BasicDiv onClick={() => setCRDB(CRDB === "CR" ? "DB" : "CR")}>{CRDB}</BasicDiv>
      </InputContainer>
      <div>
        <Input
          marginBottom={visible ? "10px" : ""}
          value={value}
          placeholder="DBS"
          onClick={() => {
            console.log(visible)
            setVisible(!visible)
          }}
        />

        {visible && (
          <motion.div transition={{ duration: 0.2 }} initial={{ y: "20vh" }} animate={{ y: "0vh" }} exit={{ y: "0vh" }}>
            <Dropdown
              choices={choices}
              onClick={() => {
                setVisible(!visible)
              }}
              setValue={setValue}
            />
          </motion.div>
        )}
      </div>
      <Input isTextField={true} placeholder="Description" />
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
  const Temp = () => {
    return <div>Hello</div>
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
                  <FormDialog />
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
