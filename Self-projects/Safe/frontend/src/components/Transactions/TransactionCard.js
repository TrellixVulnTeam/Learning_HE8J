import React from "react"
import { Link } from "react-router-dom"
import { ButtonBase } from "@mui/material/"
import styled from "styled-components/macro"
import "./Ripple.css"
const TransactionRow = styled.div`
  width: 100%;
  display: flex;
  padding: 11px 0;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  :hover {
    cursor: pointer;
  }
`
const Image = styled.div`
  width: 27px;
  height: 27px;
  border-radius: 9px;
  background-color: #d9d9d9;
`

const Transaction = ({ name, tag, image, price, type }) => {
  return (
    <Link style={{ textDecoration: "none" }} to="/form">
      <ButtonBase className="Ripple">
        <TransactionRow>
          <Image />
          <span style={{ width: "70%", textAlign: "left" }}>
            <div>{name}</div>
            <div style={{ fontSize: "10px", color: "#838282" }}>{tag}</div>
          </span>
          <div style={{ color: `${type === "CR" ? "#5EEAD1" : "#EC7474"}` }}>${price}</div>
        </TransactionRow>
      </ButtonBase>
    </Link>
  )
}
const TransactionCard = ({ date }) => {
  return (
    <div style={{ marginBottom: "14px" }}>
      <div>{date}</div>
      <Transaction name="Caifan" tag="Food" image="" price="19.00" type="CR" />
      <Transaction name="Caifan" tag="Food" image="" price="19.00" type="DB" />
    </div>
  )
}

export default TransactionCard
