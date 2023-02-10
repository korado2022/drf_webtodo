import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button } from 'react-bootstrap';
import NaviBar from './components/Menu';
import Footer from './components/Footer';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
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
}
    render() {
          return (
          
            <div>
                <NaviBar />
                <UserList users={this.state.users} />
                <Footer />
            </div>
          );
        }
}

export default App;
