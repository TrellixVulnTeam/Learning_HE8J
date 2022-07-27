import React, { useState } from "react"
import styled from "styled-components/macro"
import { motion } from "framer-motion"

import { ButtonBase, Fab, Zoom } from "@mui/material"
import CheckIcon from "@mui/icons-material/Check"
import { useNavigate } from "react-router-dom"

import "./Dropdown.css"
import { OptionUnstyled, SelectUnstyled } from "@mui/base"
import "../components/Transactions/Ripple.css"

const Container = styled.div`
  display: flex;
  flex-direction: column;
  background-color: #292929;
  height: 100vh;
  padding-top: 5vh;
  overflow: hidden;
`

const InnerContainer = styled.div`
  height: 95vh;
  position: relative;
  width: 100%;
`

const Background = styled.div`
  background-color: #d9d9d9;
  height: 92.5%;
  border-radius: 20px 20px 0 0;
  padding: 36px;
  z-index: 1;
  width: 100%;
  position: absolute;
  bottom: 0;
  padding-top: 79px;
`
const InputContainer = styled.div`
  width: 100%;
  height: 66px;
  border-radius: 10px;
  border: none;
  margin-bottom: 30px;
  background-color: white;
  color: black;
  padding: 23px 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  > * {
    color: black;
  }
`

const DropDownContainer = styled.div`
  width: 100%;
  height: auto;
  border-radius: 10px;
  border: none;
  margin-bottom: 30px;
  background-color: lightgrey;
  color: black;
  padding: 5px 20px;
  display: flex;
  flex-direction: column;
  align-items: left;
  > * {
    color: black;
  }
`
const DropdownItem = styled.div`
  height: 40px;
  font-size: 20px;
  font-weight: 500;
  display: flex;
  align-items: center;
  /* justify-content: left; */
  color: black;
`

const Image = styled.div`
  width: 107px;
  height: 107px;
  border-radius: 9px;
  background-color: #994c4c;
  margin-right: 16px;
`
const Title = styled.div`
  display: flex;
  position: absolute;
  top: -53px;
`
const BasicInput = styled.input`
  border: none;
  :focus {
    outline: none;
  }
`
const TitleInput = styled(BasicInput)`
  background-color: transparent;
  font-size: 40px;
  font-weight: 700;
  font-family: Inter;
  margin-bottom: 20px;
`

const SmallInput = styled(BasicInput)`
  font-size: 20px;
  font-weight: 900;
  color: black;
  ${BasicInput}
`

const BasicDiv = styled.div`
  font-size: 20px;
  font-weight: 700;
  :hover {
    cursor: pointer;
  }
`

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
                  <div style={{ fontSize: "20px", fontWeight: 400, color: "black", fontFamily: "Inter" }}>Food</div>
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
