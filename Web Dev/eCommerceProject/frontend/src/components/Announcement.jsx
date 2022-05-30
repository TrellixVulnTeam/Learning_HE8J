import styled from "styled-components"
const Container = styled.div`
  height: 30px;
  background-color: teal;
  color: white;
  font-weight: 500;
  font-size: 16px;
  display: flex;
  justify-content: center;
  align-items: center;
`

const Announcement = () => {
  return <Container>Super Deal! Free Shipping on Orders Over $50</Container>
}

export default Announcement
