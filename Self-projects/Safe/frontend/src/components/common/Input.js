import styled from "styled-components/macro"

export const InputContainer = styled.div`
  width: 100%;
  height: ${(props) => (props.isTextField ? "200px" : "66px")};
  border-radius: 10px;
  border: none;
  margin-bottom: ${(props) => (props.marginBottom ? props.marginBottom : "30px")};
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

export const BasicInput = styled.input`
  border: none;
  :focus {
    outline: none;
  }
`

export const SmallInput = styled(BasicInput)`
  font-size: 20px;
  font-weight: 900;
  color: black;
  ${BasicInput}
`
export const SmallTextArea = styled.textarea`
  font-size: 20px;
  font-weight: 600;
  height: 100%;
  font-family: "Poppins";
  color: black;
  border: none;
  :focus {
    outline: none;
  }
`

const Input = ({ marginBottom, type, placeholder, value, setValue, onClick, isTextField }) => {
  return (
    <InputContainer marginBottom={marginBottom} isTextField={isTextField} onClick={onClick}>
      {isTextField ? (
        <SmallTextArea onChange={(e) => setValue(e.target.value)} type={type} value={value} placeholder={placeholder} />
      ) : (
        <SmallInput onChange={(e) => setValue(e.target.value)} type={type} value={value} placeholder={placeholder} />
      )}
    </InputContainer>
  )
}
export default Input
