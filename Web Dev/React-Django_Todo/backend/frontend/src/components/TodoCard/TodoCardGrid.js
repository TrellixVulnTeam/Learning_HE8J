import { Card, Title } from "./TodoCard.styled"

const TodoCard = ({ title, description, isCompleted, onClick, onDelete, onChecked }) => {
  return (
    <Card>
      <div style={{ display: "grid", gridTemplateRows: "repeat(1fr, 2)", gridTemplateColumns: "7fr 3fr" }}>
        <Title style={{}} strike={isCompleted}>
          {title}
        </Title>
        <div style={{}}>
          <label htmlFor="completed_status">{isCompleted ? "Done" : "Haven't"}</label>
          <input type="checkbox" id="completed_status" defaultChecked={isCompleted} onChange={onChecked} />
        </div>

        <div style={{}}>{description}</div>
        <div style={{}}>
          <button onClick={onClick}> Edit</button>
          <button onClick={onDelete}> Delete</button>
        </div>
      </div>
    </Card>
  )
}

export default TodoCard
