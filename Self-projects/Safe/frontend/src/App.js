import React from "react"
import { Route, Routes } from "react-router-dom"
import Form from "./pages/Form"
import Home from "./pages/Home"
import { AnimatePresence } from "framer-motion"
import { useLocation } from "react-router-dom"

const App = () => {
  const location = useLocation()

  return (
    <AnimatePresence exitBeforeEnter>
      <Routes location={location} key={location.pathname}>
        <Route path="/" element={<Home />} />
        <Route path="/form" element={<Form />} />
      </Routes>

      {/* <Fab
        onClick={onClick}
        size="medium"
        style={{ position: "absolute", bottom: "25px", right: "20px", backgroundColor: "#5EEAD1", color: "black" }}
      >
        {isForm ? <CheckIcon fontSize="large" htmlColor="#55EAD1" /> : <AddIcon fontSize="large" htmlColor="#55EAD1" />}
      </Fab> */}
    </AnimatePresence>
  )
}

export default App
