import React from "react"
import { Link } from "react-router-dom"
import styled from "styled-components"
const TransactionRow = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
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
      <TransactionRow>
        <Image />
        <span style={{ width: "70%" }}>
          <div>{name}</div>
          <div style={{ fontSize: "10px", color: "#838282" }}>{tag}</div>
        </span>
        <div style={{ color: `${type === "CR" ? "#5EEAD1" : "#EC7474"}` }}>${price}</div>
      </TransactionRow>
    </Link>
  )
}
const TransactionCard = ({ date }) => {
  return (
    <div>
      <div style={{ marginBottom: "15px" }}>{date}</div>
      <Transaction name="Caifan" tag="Food" image="" price="19.00" type="CR" />
      <Transaction name="Caifan" tag="Food" image="" price="19.00" type="DB" />
    </div>
  )
}

export default TransactionCard
