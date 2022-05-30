import { ArrowLeftOutlined, ArrowRightOutlined } from "@material-ui/icons"
import React, { useState } from "react"
import styled from "styled-components"
import { sliderItems } from "../data"

const Container = styled.div`
  height: 100vh;
  width: 100%;
  overflow: hidden;
  position: relative;
  display: flex;
`
const Arrow = styled.div`
  width: 50px;
  height: 50px;
  border-radius: 50%;
  cursor: pointer;
  background-color: #ece2ec;
  border-radius: 50%;

  display: flex;
  align-items: center;
  justify-content: center;
  left: ${(props) => props.direction === "left" && "5px"};
  right: ${(props) => props.direction === "right" && "5px"};
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto;
  opacity: 50%;

  z-index: 2;
`
const Wrapper = styled.div`
  height: 100%;
  display: flex;
  transition: all 1.5s ease;
  transform: translate(${(props) => props.slideIndex * -100}vw);
`
const Slides = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100vw;
  height: 100%;
  align-items: center;
  background-color: ${(props) => props.bg};
`

const ImgContainer = styled.div`
  height: 100%;
  overflow: hidden;
  display: flex;
  justify-content: center;
`

const Image = styled.img`
  height: 100%;
`
const InfoContainer = styled.div`
  background-color: white;
  padding: 50px;
`

const Title = styled.h1`
  font-size: 70px;
`

const Description = styled.div`
  margin: 50px 0px;
  font-size: 20px;
  font-weight: 500;
  letter-spacing: 3px;
`

const Button = styled.button`
  background-color: transparent;
  padding: 10px;
  font-size: 20px;
  width: 40%;
`

const Slider = () => {
  const [slideIndex, setSlideIndex] = useState(1)

  const handleClick = (direction) => {
    if (direction === "left") {
      setSlideIndex(slideIndex > 0 ? slideIndex - 1 : 2)
    }
    if (direction === "right") {
      setSlideIndex(slideIndex < sliderItems.length - 1 ? slideIndex + 1 : 0)
    }
  }
  return (
    <Container>
      <Arrow direction="left" onClick={() => handleClick("left")}>
        <ArrowLeftOutlined></ArrowLeftOutlined>
      </Arrow>
      <Arrow direction="right" onClick={() => handleClick("right")}>
        <ArrowRightOutlined></ArrowRightOutlined>
      </Arrow>
      <Wrapper slideIndex={slideIndex}>
        {sliderItems.map((slide) => (
          <Slides bg={slide.bg}>
            <ImgContainer>
              <Image src={slide.img}></Image>
            </ImgContainer>
            <InfoContainer>
              <Title>{slide.title} </Title>
              <Description>{slide.desc}</Description>
              <Button>Buy Now</Button>
            </InfoContainer>
          </Slides>
        ))}
      </Wrapper>
    </Container>
  )
}

export default Slider
