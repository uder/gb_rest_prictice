import React from "react";
import logo from './logo.svg';
import './App.css';
import UsersList from "./components/Users";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import axios from 'axios';

class App extends React.Component{
    constructor(props){
        super(props);
        this.state={
            'users':[],
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
                const users=response.data
                this.setState ({
                    'users' : users
                })
            }).catch(error=>console.log(error))

    }

    render(){
        return (
            <div>
                <Menu menu_items={this.state.menu_items} />
                <UsersList users={this.state.users} />
                <Footer footer={this.state.footer} />
            </div>
        )
    }
}

export default App;
