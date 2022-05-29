const TodoCard = ({ title, description, isCompleted, onClick, onDelete, onChecked }) => {
  return (
    <div style={{ border: "2px solid black", width: "40%", margin: "20px" }}>
      {isCompleted ? <strike>{title}</strike> : <div>{title}</div>}
      <div>{description}</div>
      <span>
        <label htmlFor="completed_status">{isCompleted ? "Done" : "Haven't"}</label>
        <input type="checkbox" id="completed_status" defaultChecked={isCompleted} onChange={onChecked} />
        <button onClick={onClick}> Edit</button>
        <button onClick={onDelete}> Delete</button>
      </span>
    </div>
  )
}

export default TodoCard
