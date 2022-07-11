import React from "react"

const Navbar = () => {
  return (
    <div className="flex justify-between p-4 items-center text-white font-semibold">
      <div>LOGO</div>
      <div className="flex gap-10 items-center">
        <div> Home </div>
        <div> Skills </div>
        <div> Projects </div>
        <div className="border px-3 py-2"> Let's Connect </div>
      </div>
    </div>
  )
}

export default Navbar
