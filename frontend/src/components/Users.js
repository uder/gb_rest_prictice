import React from "react";

const UserItem = ({user}) => {
    return(
        <tr>
            <td>
                {user.userName}
            </td>
            <td>
                {user.firstName}
            </td>
            <td>
                {user.lastName}
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
            <thead>
                <tr>
                    <th>UserName</th>
                    <th>FirstName</th>
                    <th>LastName</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                {users.map((current)=><UserItem user={current} />)}
            </tbody>
        </table>
    )
}

export default UserList