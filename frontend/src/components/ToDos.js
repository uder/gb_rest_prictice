import React from "react";

const ToDoItem = ({todo}) => {
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
        </tr>
    )
}

const ToDoList=({todos})=>{
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
                </tr>
            </thead>
            <tbody>
                {todos.map((current)=><ToDoItem todo={current} />)}
            </tbody>
        </table>
    )
}

export default ToDoList