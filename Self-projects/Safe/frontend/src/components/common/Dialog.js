import * as React from "react"
import Button from "@mui/material/Button"
import TextField from "@mui/material/TextField"
import Dialog from "@mui/material/Dialog"
import DialogActions from "@mui/material/DialogActions"
import DialogContent from "@mui/material/DialogContent"
import DialogContentText from "@mui/material/DialogContentText"
import DialogTitle from "@mui/material/DialogTitle"
import { Menu, MenuItem, Select } from "@mui/material"

const FormDialog = () => {
  const [open, setOpen] = React.useState(false)

  const handleClickOpen = () => {
    setOpen(true)
  }

  const handleClose = () => {
    setOpen(false)
  }

  const [value, setValue] = React.useState("Food")
  const handleChange = (e) => {
    setValue(e.target.value)
    handleClose()
  }
  return (
    <div>
      <Button style={{ color: "black", fontSize: "20px", justifyContent: "flex-start" }} onClick={handleClickOpen}>
        {value}
      </Button>
      <Dialog open={open} onClose={handleClose}>
        <DialogContent>
          <DialogContentText style={{ marginBottom: "10px" }}>Select your spending category!</DialogContentText>
          <Select onChange={handleChange} autoFocus id="tag" type="text" fullWidth variant="standard">
            <MenuItem style={{ color: "black" }} value="Food">
              Fod
            </MenuItem>
            <MenuItem style={{ color: "black" }} value="Shopping">
              Shopping
            </MenuItem>
            <MenuItem style={{ color: "black" }} value="Date">
              Date
            </MenuItem>
          </Select>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleClose}>Confirm</Button>
        </DialogActions>
      </Dialog>
    </div>
  )
}

export default FormDialog
