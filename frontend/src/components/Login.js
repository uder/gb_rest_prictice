import React from "react";

class LoginForm extends React.Component{
    constructor(props){
        super(props)
        this.state={
            'login': '',
            'password': '',
        }
    }
    handleChange(event){
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }
    handleSubmit(event){
        //For testing only. Comment out next lines
//        console.log(this.state.login+" : "+this.state.password)
        this.props.get_token(this.state.login, this.state.password)

        event.preventDefault()
    }
    render(){
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <input
                    type="text"
                    name="login"
                    placeholder="Login"
                    value={this.state.login}
                    onChange={(event)=>this.handleChange(event)}
                />
                <input
                    type="text"
                    name="password"
                    placeholder="Password"
                    value={this.state.password}
                    onChange={(event)=>this.handleChange(event)}
                />
                <input type="submit" value="Login" />
            </form>
        );
    }
}

export default LoginForm