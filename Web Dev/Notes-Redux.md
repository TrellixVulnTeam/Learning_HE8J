1. create a redux folder - slice and store
2. for slice, theres : names, initalstate, and reducers
3. export reducer, go to store and use configurestore and add in reducer
4. Wrap App with provider, store = path to redux store

refer to /Users/tai/Learning/Web Dev/youtube-redux/src/redux

## Why do we use redux?

Context API rerenders everything if state has been changed
Redux only changes it if the thing used is changed.

---

## store.js

```
import { configureStore } from "@reduxjs/toolkit";
import userReducer from "./userSlice";

export default configureStore({
  reducer: {
    user: userReducer,
});
```

---

## userSlice.js

```
import { createSlice } from "@reduxjs/toolkit";

export const userSlice = createSlice({
  name: "user",
  initialState: {
    name: "john",
    email: "john@email.com",
  },
  reducers: {
    update: (state, action) => {
      state.name = action.payload.name;
      state.email = action.payload.email;
    },
    remove: (state) => {
      state = null;
    },
    addHelloToName : (state, action) =>{
      state.name = "Hello " + action.payload.name
    }
  },
});
```

---

## Index.js

```
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import store from "./redux/store";
import { Provider } from "react-redux";

ReactDOM.render(
  <Provider store={store}>
      <App />
  </Provider>,
  document.getElementById("root")
);
```

---

## In any actual component

```
import {useDispatch, useSelector} from "react-redux"
const name = useSelector((state) => state.user.name);
or can use
const {userInfo, pending, error} = useSelector((state) => state.user)
```

---

## To use actions to update state?

```
const dispatch = useDispatch()
const handleClick = (e) => {
    e.preventDefault();
    // without API
    // dispatch(update({ name, email }));
    // with API
    dispatch(updateUser2({ name, email }));
  };
```

---

## API

1. in state, remember to add pending and error to state
   state looks like : initial state -1userInfo -2pending -3error
2. use custom reducers / Redux thunk

### Custom reducers

```
reducers: {
    updateStart: (state) => {
        state.pending = true
    },
    updateSuccess: (state, action) => {
        state.pending= false
        state.userInfo = action.payload
    }
    updateError: (state)=> {
        state.error = true
        state.pending = false
    }
```

add another function in redux folder ## apiCalls.js

```
import axios from "axios";
import { updateStart, updateSuccess, updateFailure } from "./userSlice";

export const updateUser = async (user, dispatch) => {
  dispatch(updateStart());
  try {
    const res = await axios.post("http://localhost:8800/api/users/1/update", user);
    dispatch(updateSuccess(res.data));
  } catch (err) {
    dispatch(updateFailure());
  }
};
```

---

## Async thunk

1. we need to use inside extrareducers

```
export const updateUser2 = createAsyncThunk("users/update", async (user) => {
  const response = await axios.post("http://localhost:8800/api/users/1/update", user)
  return response.data
})
inside initial state,

extraReducers: {
    [updateUser2.pending]: (state) => {
      state.pending = true
      state.error = false
    },
    [updateUser2.fulfilled]: (state, action) => {
      state.userInfo = action.payload
      state.pending = false
    },
    [updateUser2.rejected]: (state) => {
      state.pending = null
      state.error = true
    },
  },

```
