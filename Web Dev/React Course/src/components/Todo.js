import { string } from "prop-types"
import "../index.css"

const Todo = (props) => {
  const { text } = props
  const deleteHandler = () => {}
  return (
    <div className="card">
      <h2>{text}</h2>
      <div className="actions">
        <button className="btn" onClick={deleteHandler}>
          Delete
        </button>
      </div>
    </div>
  )
}

Todo.propsTypes = {
  text: string,
}

export default Todo
