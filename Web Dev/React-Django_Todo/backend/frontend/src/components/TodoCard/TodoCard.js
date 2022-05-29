import { Card, Title } from "./TodoCard.styled"

const TodoCard = ({ title, description, isCompleted, onClick, onDelete, onChecked }) => {
  return (
    <Card>
      <div style={{ display: "flex" }}>
        <Title style={{ width: "70%" }} strike={isCompleted}>
          {title}
        </Title>
        <div style={{ width: "30%" }}>
          <label htmlFor="completed_status">{isCompleted ? "Done" : "Haven't"}</label>
          <input type="checkbox" id="completed_status" defaultChecked={isCompleted} onChange={onChecked} />
        </div>
      </div>

      <div style={{ display: "flex", flexDirection: "row" }}>
        <div style={{ flex: 0.7 }}>{description}</div>
        <div style={{ flex: 0.3 }}>
          <button onClick={onClick}> Edit</button>
          <button onClick={onDelete}> Delete</button>
        </div>
      </div>
    </Card>
  )
}

export default TodoCard
