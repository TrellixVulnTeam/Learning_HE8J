import React from "react"

const Aboutme = () => {
  return (
    <div className="container py-60 px-24 bg-slate-200 w-full flex items-center gap-7">
      <div className="w-1/4">
        <img src={require("./male-placeholder-image.jpeg")}></img>
      </div>
      <div className="container flex flex-col gap-2">
        ![]({require("./male-placeholder-image.jpeg")})<h1 className="font-semibold text-4xl">About me</h1>
        <div className="text-xl">
          I am a Year 2 Computer Engineering Student and I have a wide variety of interests!
        </div>
        <div className="font-semibold text-4xl">Trading</div>
      </div>
    </div>
  )
}

export default Aboutme
