import React from 'react';
import Container from 'react-bootstrap/Container';
import { Link } from 'react-router-dom';


const UserItem = ({user}) => {
    return (
        <tr>
            <td><Link to={`/user/${user.username}`}>{user.username}</Link></td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>
    )
}


const UserList = ({users}) => {
    return (
        <div className='container'>
        <Container>
            <table>
                <th>User name</th>
                <th>First name</th>
                <th>Last name</th>
                <th>Email</th>
                {users.map((user) => <UserItem user={user} />)}
            </table>
        </Container>
        </div>
    )
}


export default UserList