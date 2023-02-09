import React from 'react';
import Container from 'react-bootstrap/Container';


const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.username}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>

    )
}


const UserList = ({users}) => {
    return (
        <Container>
            <table>
                <th>User name</th>
                <th>First name</th>
                <th>Last name</th>
                <th>Email</th>
                {users.map((user) => <UserItem user={user} />)}
            </table>
        </Container>
    )
}


export default UserList