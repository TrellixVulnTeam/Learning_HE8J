import styled from "styled-components"

export const Card = styled.div`
  border: 0.5px solid black;
  border-radius: 20px;
  width: 80%;
  margin: 20px;
  display: flex;
  flex-direction: column;
  button {
    background-color: skyblue;
  }
  padding: 1rem;
  overflow: hidden;
  .description {
    font-size: 0.8rem;
  }
`
export const Title = styled.div`
  text-decoration: ${(props) => props.strike && "line-through "};
  font-size: large;
  font-weight: bold;
`
