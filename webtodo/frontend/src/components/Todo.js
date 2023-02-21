import React from 'react';
import Container from 'react-bootstrap/Container';


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.text_note}</td>
            <td>{todo.create_at}</td>
            <td>{todo.update_at}</td>
            <td>{todo.status}</td>
            <td>{todo.working}</td>
            <td>{todo.author_todo}</td>
        </tr>
    )
}


const TodotList = ({todos}) => {
    return (
        <Container>
            <table>
                <th>Id</th>
                <th>Text mote</th>
                <th>Date create</th>
                <th>Date update</th>
                <th>Status</th>
                <th>Working</th>
                <th>Author todo</th>
                {todos.map((todo) => <TodoItem todo={todo} />)}
            </table>
        </Container>
    )
}


export default TodotList