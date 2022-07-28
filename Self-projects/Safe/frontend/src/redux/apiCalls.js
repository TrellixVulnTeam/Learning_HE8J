import axios from "axios"
import { updateStart, updateSuccess, updateError } from "./userSlice"

export const updateUser = async (user, dispatch) => {
  dispatch(updateStart())
  try {
    const res = await axios.post("http://127.0.0.1:8000/api/token/", user)
    dispatch(updateSuccess(res.data))
  } catch (err) {
    dispatch(updateError())
  }
}
