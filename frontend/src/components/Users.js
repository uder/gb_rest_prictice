import React from "react";

const UserItem = ({user}) => {
    return(
        <tr>
            <td>
                {user.user_name}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UserList=({users})=>{
    return (
        <table>
            <th>UserName</th>
            <th>FirstName</th>
            <th>LastName</th>
            <th>Email</th>
            {users.map((current)=><UserItem user={current} />)}
        </table>
    )
}

export default UserList