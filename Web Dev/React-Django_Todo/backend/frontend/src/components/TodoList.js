// import TodoCard from "./TodoCard"
import TodoCard from "./TodoCardGrid"
import { useEffect, useState } from "react"
const todos = [
  { id: 1, title: "go toilet", description: "i dont know", isCompleted: true },
  { id: 2, title: "sdfmsdiofcm", description: "i dont know", isCompleted: false },
  { id: 3, title: "sdfmsdiofcm", description: "i dont know", isCompleted: false },
]

function getCookie(name) {
  let cookieValue = null
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";")
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}

const link = "http://127.0.0.1:8000/todos-api/todos/"
const TodoList = () => {
  // const [todos, setTodos] = useState(initialState.todoList)
  const [todoList, setTodoList] = useState(todos)
  const [activeItem, setActive] = useState({ id: "", title: "", description: "placeholder", isCompleted: false })
  const [isEditing, setIsEditing] = useState(false)

  const fetchTodos = () => {
    fetch(link, {
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => setTodoList(data))
      .then(console.log(todoList))
  }

  useEffect(() => fetchTodos, [])

  const handleChange = (e) => {
    console.log(e.target.name)
    console.log(e.target.value)
    setActive({ ...activeItem, title: e.target.value })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    const csrftoken = getCookie("csrftoken")
    var postURL = link

    var RESTmethod = "POST"
    if (isEditing) {
      postURL = postURL + `${activeItem.id}`
      setIsEditing(false)
      RESTmethod = "PUT"
    }

    fetch(postURL, {
      method: RESTmethod,
      headers: {
        "Content-type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify(activeItem),
    })
      .then((response) => {
        return response.json()
      })
      .then((data) => {
        setActive({ ...activeItem, title: "", id: null })
      })
      .then(() => fetchTodos())
      .catch((e) => console.log(e))
  }

  const startEdit = (todo) => {
    setIsEditing(true)
    setActive(todo)
  }

  const handleDelete = (todo) => {
    const csrftoken = getCookie("csrftoken")
    fetch(link + `${todo.id}`, {
      method: "DELETE",
      headers: { "Content-type": "application/json", "X-CSRFToken": csrftoken },
    }).then((response) => {
      console.log(response.status)
      if ((response.status === 200) | (response.status === 204)) {
        console.log("im in")
        const filteredList = todoList.filter((x) => x.id !== todo.id)
        setTodoList(filteredList)
      }
    })

    // console.log(mainState.todoList)
  }

  const handleComplete = (todo) => {
    console.log("chang")
    const csrftoken = getCookie("csrftoken")
    fetch(link + `${todo.id}`, {
      method: "PUT",
      headers: { "Content-type": "application/json", "X-CSRFToken": csrftoken },
      body: JSON.stringify({ ...todo, isCompleted: !todo.isCompleted }),
    }).then((response) => {
      console.log(response.status)
      if ((response.status === 200) | (response.status === 204)) {
        console.log("changed status")
        fetchTodos()
      }
    })
  }

  return (
    <div style={{ border: "5px solid black", width: "50%", margin: "auto" }}>
      <form onSubmit={handleSubmit}>
        <label htmlFor="new_todo_input">What needs to be done</label>
        <input type="text" id="new_todo_input" name="text" value={activeItem.title} onChange={handleChange}></input>
        <button type="submit">Add</button>
      </form>
      <h1>Heres your task list</h1>
      <div>
        {todoList.map((todo) => (
          <TodoCard
            key={todo.id}
            onClick={() => startEdit(todo)}
            title={todo.title}
            description={todo.description}
            isCompleted={todo.isCompleted}
            onDelete={() => handleDelete(todo)}
            onChecked={() => handleComplete(todo)}
          />
        ))}
      </div>
    </div>
  )
}

export default TodoList
