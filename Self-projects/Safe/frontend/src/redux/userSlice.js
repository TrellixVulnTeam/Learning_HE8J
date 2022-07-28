import { createSlice } from "@reduxjs/toolkit"

export const userSlice = createSlice({
  name: "user",
  initialState: {
    pending: false,
    error: false,
    userInfo: {
      userName: "",
      token: "",
    },
  },
  reducers: {
    updateStart: (state) => {
      state.pending = true
    },
    updateSuccess: (state, action) => {
      state.pending = false
      state.userInfo = { ...state.userInfo, token: action.payload.access }
    },
    updateError: (state) => {
      state.error = true
      state.pending = false
    },
  },
})

export const { updateStart, updateSuccess, updateError } = userSlice.actions
export default userSlice.reducer
