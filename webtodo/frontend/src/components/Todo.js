import React from 'react';
import Nav from 'react-bootstrap/Nav';

const TodoItem = ({todo, deleteTodo}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.text_note}</td>
            <td>{todo.create_at}</td>
            <td>{todo.update_at}</td>
            <td>{todo.status}</td>
            <td>{todo.working}</td>
            <td>{todo.author_todo}</td>
            <td><button onClick={ ()=> deleteTodo(todo.id) } type='button'>Delete</button></td>
        </tr>
    )
}


const TodotList = ({todos, deleteTodo}) => {
    return (
        <div className='container'>
            <table>
                <th>Id</th>
                <th>Text mote</th>
                <th>Date create</th>
                <th>Date update</th>
                <th>Status</th>
                <th>Working</th>
                <th>Author todo</th>
                <th></th>
                {todos.map((todo) => <TodoItem todo={todo} deleteTodo={deleteTodo} />)}
            </table>
            <Nav.Link href='/todos/create'>Create</Nav.Link>
        </div>
    )
}


export default TodotList