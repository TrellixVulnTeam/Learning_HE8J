import React from "react"
import styled from "styled-components"
import { useState } from "react"
const Container = styled.div`
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  width: 135%;

  > * {
    margin-right: 10px;
  }
`
const Bar = styled.div`
  width: 26px;
  height: ${(props) => props.height};
  border-radius: 7px;
  background-color: ${(props) => (props.isActive ? "#6AC5B4" : props.color)};
`

const monthly_spending = {
  Jan: 2900,
  Feb: 2600,
  Mar: 2600,
  April: 1000,
  May: 2500,
  Jun: 1000,
  Jul: 2000,
  Aug: 1300,
  Sep: 2600,
  Oct: 2000,
  Nov: 3500,
  Dec: 2000,
}
const max = Math.max(...Object.values(monthly_spending))
console.log(max)

const color = ["#BDC3C2", "#808483"]
const Graph = () => {
  const [activeIndex, setActiveIndex] = useState(Object.keys(monthly_spending).length - 1)
  return (
    <Container>
      {Object.keys(monthly_spending).map((month, index) => {
        const height = String((monthly_spending[month] / max) * 100) + "%"
        const isActive = index === activeIndex
        return (
          <Bar
            isActive={isActive}
            onClick={() => setActiveIndex(index)}
            key={month}
            height={height}
            color={color[index % 2]}
          />
        )
      })}
    </Container>
  )
}

export default Graph
