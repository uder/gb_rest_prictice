import React from "react";
import {Link} from 'react-router-dom';

const ToDoItem = ({todo, deleteTodo}, ) => {
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
                <button onClick={()=>deleteTodo(todo.uuid)} type='button'>Удалить</button>
            </td>

        </tr>
    )
}

const ToDoList=({todos, deleteTodo})=>{
    return (
        <table>
            <thead>
                <tr>
                    <th>Project</th>
                    <th>Creator</th>
                    <th>Text</th>
                    <th>Created at</th>
                    <th>Updated at</th>
                    <th></th>
                </tr>
            </thead>
            <tfoot>
                <tr>
                    <td>
                        <Link to='/todos/create'>Создать заметку</Link>
                    </td>
                </tr>
            </tfoot>
            <tbody>
                {/*{todos.map((current)=><ToDoItem todo={current} />)}*/}
                {todos.map((item)=><ToDoItem todo={item} deleteTodo={deleteTodo}/>)}

            </tbody>
        </table>
    )
}

export default ToDoList