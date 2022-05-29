import React from "react"
import { useNavigate, useParams } from "react-router-dom"

export const Profile = () => {
  let navigate = useNavigate()
  let { username } = useParams()

  return (
    <div>
      This is the profile page for {username}! Profile
      <button onClick={() => navigate("/about")}>Change to about page</button>
    </div>
  )
}
