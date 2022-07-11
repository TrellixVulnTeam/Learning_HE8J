import React from "react"

const Frontpage = () => {
  return (
    <div className="container text-white flex flex-col items-center justify-center py-56 px-24 md:flex-row">
      <div className="w-1/3">
        <img src="../../assets/computer.png" className="object-contain w-96" alt="computer"></img>
      </div>
      <div className="flex flex-col gap-5 md:basis-4/5 md:order-first items-center justify-center text-center md:items-start md:text-left">
        <h1 className="font-semibold text-4xl">Hello! I'm Tai, a </h1>
        <div className="text-gray-300">
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
          standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to
          make a type specimen book. It has survived not only five centuries, but also the leap into electronic
          typesetting, remaining essentially
        </div>
        <div className="font-semibold border border-white p-2 w-32">Let's connect</div>
      </div>
    </div>
  )
}

export default Frontpage
