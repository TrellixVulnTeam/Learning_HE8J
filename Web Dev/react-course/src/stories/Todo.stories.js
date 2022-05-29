import Todo from "../components/Todo"

export default {
  title: "Todo",
  component: Todo,
}
const Template = (args) => <Todo {...args} />

export const TodoTest = () => Template.bind({})

TodoTest.args = {
  text: "Boom",
}
