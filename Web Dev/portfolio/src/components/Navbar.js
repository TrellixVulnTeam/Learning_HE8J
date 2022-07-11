import React from "react"

const Navbar = () => {
  return (
    <div className="flex justify-between p-5 items-center text-white font-semibold">
      <h1 className="text-3xl">LOGO</h1>
      <ul className="flex gap-10 items-center">
        <li className="hover:cursor-pointer"> Home </li>
        <li className="hover:cursor-pointer"> Skills </li>
        <li className="hover:cursor-pointer"> Projects </li>
        <li className="border px-3 py-2 hover:cursor-pointer"> Let's Connect </li>
      </ul>
    </div>
  )
}

export default Navbar
