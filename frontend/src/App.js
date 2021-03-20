import React from "react";
import logo from './logo.svg';
import './App.css';
import UsersList from "./components/Users";
import ProjectsList from "./components/Projects";
import ToDosList from "./components/ToDos";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import axios from 'axios';
import {BrowserRouter, HashRouter, Route, Link, Switch} from 'react-router-dom'


class App extends React.Component{
    constructor(props){
        super(props);
        this.state={
            'users':[],
            'projects': [],
            'todos': [],
            'menu_items':[],
            'footer' : ''
        }
    }

    componentDidMount(){
        const menu_items=[
            {
                'name': 'Главная'
            },
            {
                'name': 'Тестовый пункт меню 1'
            },
            {
                'name': 'Тестовый пункт меню 2'
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
                        <Route exact path='/todos' component={() => <ToDosList todos={this.state.todos} />} />
                    </Switch>
                    <Footer footer={this.state.footer} />
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
