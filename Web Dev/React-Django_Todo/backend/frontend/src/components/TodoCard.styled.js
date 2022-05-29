import styled from "styled-components"

export const Card = styled.div`
  border: 2px solid black;
  width: 40%;
  margin: 20px;
  display: flex;
  flex-direction: column;
  button {
    background-color: skyblue;
  }
  padding: 1rem;
`
export const Title = styled.div`
  text-decoration: ${(props) => props.strike && "line-through "};
  font-size: large;
  font-weight: bold;
`
