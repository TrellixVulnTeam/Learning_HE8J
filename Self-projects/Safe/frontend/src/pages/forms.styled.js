import styled from "styled-components/macro"
export const Container = styled.div`
  display: flex;
  flex-direction: column;
  background-color: #292929;
  height: 100vh;
  padding-top: 5vh;
  overflow: hidden;
`

export const InnerContainer = styled.div`
  height: 95vh;
  position: relative;
  width: 100%;
`

export const Background = styled.div`
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
export const InputContainer = styled.div`
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

export const DropDownContainer = styled.div`
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
export const DropdownItem = styled.div`
  height: 40px;
  font-size: 20px;
  font-weight: 500;
  display: flex;
  align-items: center;
  /* justify-content: left; */
  color: black;
`

export const Image = styled.div`
  width: 107px;
  height: 107px;
  border-radius: 9px;
  background-color: #994c4c;
  margin-right: 16px;
`
export const Title = styled.div`
  display: flex;
  position: absolute;
  top: -53px;
`
export const BasicInput = styled.input`
  border: none;
  :focus {
    outline: none;
  }
`
export const TitleInput = styled(BasicInput)`
  background-color: transparent;
  font-size: 40px;
  font-weight: 700;
  font-family: Inter;
  margin-bottom: 20px;
`

export const SmallInput = styled(BasicInput)`
  font-size: 20px;
  font-weight: 900;
  color: black;
  ${BasicInput}
`

export const BasicDiv = styled.div`
  font-size: 20px;
  font-weight: 700;
  :hover {
    cursor: pointer;
  }
`
