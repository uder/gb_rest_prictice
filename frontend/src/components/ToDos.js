import React from "react";

const ToDoItem = ({todo, deleteTodo, createTodo}, ) => {
    return(
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.userCreator}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.createdAt}
            </td>
            <td>
                {todo.updatedAt}
            </td>
            <td>
                {todo.active}
            </td>
            <td>
                <button onClick={()=>deleteTodo(todo.uuid)} type='button'>Удалить</button>
            </td>

        </tr>
    )
}

const ToDoList=({todos, deleteTodo, createTodo})=>{
    return (
        <table>
            <thead>
                <tr>
                    <th>Project</th>
                    <th>Creator</th>
                    <th>Text</th>
                    <th>Created at</th>
                    <th>Updated at</th>
                    <th>Active</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {/*{todos.map((current)=><ToDoItem todo={current} />)}*/}
                {todos.map((item)=><ToDoItem todo={item} deleteTodo={deleteTodo}/>)}

            </tbody>
        </table>
    )
}

export default ToDoList