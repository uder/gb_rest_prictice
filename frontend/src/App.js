import React from "react";
//import logo from './logo.svg';
import './App.css';
import UsersList from "./components/Users";
import ProjectsList from "./components/Projects";
import ProjectInfo from "./components/ProjectInfo";
import ToDosList from "./components/ToDos";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import LoginForm from "./components/Login.js";
import axios from 'axios';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import Cookies from 'universal-cookie';


class App extends React.Component{
    constructor(props){
        super(props);
        this.state={
            'users':[],
            'projects': [],
            'todos': [],
            'menu_items':[],
            'footer' : '',
            'token': '',
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token',token)
        this.setState({'token': token})
    }

    is_authenticated(){
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token':token})
    }

    get_token(user,password){
        axios.post('http://127.0.0.1:8000/api-token-auth/', {'username': user, 'password': password})
        .then( response=> {
            //For testing purposes only. Comment out next line
//            console.log(response.data)

            this.set_token(response.data['token'])
        }).catch(error=>alert('Wrong UserName or Password'))
    }
    componentDidMount(){
        const menu_items=[
            {
                'name': 'Главная',
                'path': '/',
            },
            {
                'name': 'Проекты',
                'path': '/projects',
            },
            {
                'name': 'Заметки',
                'path': '/todos',
            },
            {
                'name': 'Войти',
                'path': '/login',
            },
        ]
        const footer='Footer Message'
        this.setState(
            {
                'menu_items': menu_items,
                'footer': footer,
            }
        )

        axios.get('http://127.0.0.1:8000/api/user/')
            .then (response =>{
                const users=response.data.results
                this.setState ({
                    'users' : users
                })
            }).catch(error=>console.log(error))
        axios.get('http://127.0.0.1:8000/api/project/')
            .then (response =>{
                const projects=response.data.results
                this.setState ({
                    'projects' : projects
                })
            }).catch(error=>console.log(error))
        axios.get('http://127.0.0.1:8000/api/todo/')
            .then (response =>{
                const todos=response.data.results
                this.setState ({
                    'todos' : todos
                })
            }).catch(error=>console.log(error))

    }

    render(){
        return (

            <div>
                <BrowserRouter>
                    <Menu menu_items={this.state.menu_items} />
                    <Switch>
                        <Route exact path='/' component={() => <UsersList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects} />} />
                        <Route exact path='/project/:id' component={() => <ProjectInfo projects={this.state.projects} />} />
                        <Route exact path='/todos' component={() => <ToDosList todos={this.state.todos} />} />
                        <Route exact path='/login'
                            component={() => <LoginForm
                                                get_token={(user,password) => this.get_token(user,password)}
                                             />
                            }
                        />
                    </Switch>
                    <Footer footer={this.state.footer} />
                </BrowserRouter>
            </div>
        )
    }
}
export default App;
