import React from 'react';
import axios from 'axios';
//import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import TodoList from './components/Todo.js';
import NotFound404 from './components/NotFound404.js';
import LoginForm from './components/Auth.js';
// import ProjectListUsers from './components/ProjectsUser.js';
import 'bootstrap/dist/css/bootstrap.min.css';
//import { Button } from 'react-bootstrap';
import NaviBar from './components/Menu';
import Footer from './components/Footer';
import {HashRouter, Route, BrowserRouter, Link, Switch, Redirect} from 'react-router-dom';
import Cookies from 'universal-cookie';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': ''
        }
        // const insAonymous = false;
    }

    

    load_data(){
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(response => {
            this.setState(
                {
                    'users': response.data
                }
            )}).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/', {headers}).then(response => {
            this.setState(
                {
                    'projects': response.data
                }
            )}).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todos/', {headers}).then(response => {
                this.setState(
                    {
                        'todos': response.data
                    }
                )}).catch(error => console.log(error)) 
    }

    // вариант для storage
    // get_token_from_storage(){
    //     const cookies = new Cookies()
    //     const token = cookies.get('token')
    //     this.setState({'token': token})
    // }

    get_token_from_cookies(){
        const cookies = new Cookies()
        const token = cookies.get('token')
  
        this.setState({'token': token}, ()=>this.load_data())
    }

    set_token(token){
        // вариант через LocalStorage
        // localStorage.setItem('token': token)
        // let item = localStorage.getItem('token')
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, ()=>this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', 
            {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
                console.log(response.data['token'])
            }).catch(error => alert('Не верный логин или пароль'))
    }

    is_auth(){
        return !!this.state.token
    }

    get_headers(){
        let headers = {
            'Content-Type': 'applications/json'
        }

        if(this.is_auth()){
            headers['Authorization'] = `Token ${this.state.token}`
        }

        return headers
    }


    logout(){
        this.set_token('')
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
        // axios.get('http://127.0.0.1:8000/api/users/').then(response => {
        //     this.setState(
        //         {
        //             'users': response.data
        //         }
        //     )}).catch(error => console.log(error))

        // axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
        //     this.setState(
        //         {
        //             'projects': response.data
        //         }
        //     )}).catch(error => console.log(error))

        // axios.get('http://127.0.0.1:8000/api/todos/').then(response => {
        //         this.setState(
        //             {
        //                 'todos': response.data
        //             }
        //         )}).catch(error => console.log(error))
        // this.get_token_from_storage()    // вариант для storage
        this.get_token_from_cookies()
        
    }
    render() {
        console.log(this.state.token)
        return (
          
            <div>
                <NaviBar is_in={this.is_auth() ? true : false}  logout={() => this.logout()} />
                
                <BrowserRouter>
                    <Switch>
                        <Route exact path='/users' component={() => < UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => < ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todos' component={() => < TodoList todos={this.state.todos} />} />
                        <Route exact path='/login' component={() => < LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
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
