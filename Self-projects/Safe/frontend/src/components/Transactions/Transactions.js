import React, { useState } from "react"
import TagButton from "./TagButton"
import styled from "styled-components/macro"
import TransactionCard from "./TransactionCard"
const Container = styled.div`
  height: 57.5%;
  > * {
    margin-bottom: 10px;
  }
`
const TagsContainer = styled.div`
  display: flex;
  flex-direction: row;
  margin-bottom: 20px;
  overflow-x: scroll;

  > * {
    margin-right: 20px;
  }
`

const tags = ["hello", "boom", "food", "naruto", "boombaaya", "shakakla"]
const Transactions = () => {
  const [activeIndex, setActiveIndex] = useState(0)
  return (
    <Container>
      <TagsContainer>
        {tags.map((tag, index) => (
          <div onClick={() => setActiveIndex(index)}>
            <TagButton key={tag} isActive={index === activeIndex} name={tag} />
          </div>
        ))}
      </TagsContainer>
      <div style={{ overflowY: "scroll", height: "80%" }}>
        <TransactionCard date="Today" />
        <TransactionCard date="18th July 2022" />
        <TransactionCard date="17th July 2022" />
        <TransactionCard date="17th July 2022" />
      </div>
    </Container>
  )
}

export default Transactions
