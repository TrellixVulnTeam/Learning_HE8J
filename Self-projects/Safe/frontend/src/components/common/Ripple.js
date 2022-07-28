import { ButtonBase } from "@mui/material"
import React from "react"
import "./Ripple.css"

const Ripple = ({ onClick, children, style }) => {
  return (
    <ButtonBase onClick={onClick} style={style} className="Ripple">
      {children}
    </ButtonBase>
  )
}

export default Ripple
