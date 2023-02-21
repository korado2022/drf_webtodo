import React from 'react';
import axios from 'axios';
//import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import TodoList from './components/Todo.js';
import NotFound404 from './components/NotFound404.js';
// import ProjectListUsers from './components/ProjectsUser.js';
import 'bootstrap/dist/css/bootstrap.min.css';
//import { Button } from 'react-bootstrap';
import NaviBar from './components/Menu';
import Footer from './components/Footer';
import {HashRouter, Route, BrowserRouter, Link, Switch, Redirect} from 'react-router-dom';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': []
        };
    }


    componentDidMount() {
//        const users = [
//            {
//                "username": "Sergey",
//                "first_name": "Sergey",
//                "last_name": "Sergeev",
//                "email": "sergey@m.ru"
//            },
//            {
//                "username": "Ivan",
//                "first_name": "Ivan",
//                "last_name": "Ivanov",
//                "email": "ivan@m.ru"
//            },
//            {
//                "username": "Петр",
//                "first_name": "Петр",
//                "last_name": "Петров",
//                "email": "petr@m.ru"
//            },
//            {
//                "username": "asd",
//                "first_name": "",
//                "last_name": "",
//                "email": "asd@m.ru"
//            },
//        ]
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
            this.setState(
                {
                    'users': response.data
                }
            )}).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
            this.setState(
                {
                    'projects': response.data
                }
            )}).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todos/').then(response => {
                this.setState(
                    {
                        'todos': response.data
                    }
                )}).catch(error => console.log(error))

    }
    render() {
          return (
          
            <div>
                <NaviBar />
                <BrowserRouter>
                    <Switch>
                        <Route exact path='/users' component={() => < UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => < ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todos' component={() => < TodoList todos={this.state.todos} />} />
                        {/* <Route path='/user/:username'>
                            <ProjectListUsers users={this.state.users} />
                        </Route> */}

                        <Redirect from='/project' to='/projects' />
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
                <Footer />
            </div>
          );
        }
}

export default App;
