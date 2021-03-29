import React from "react";
import {useHistory} from 'react-router-dom';
import './LoginButton.css'

function Login(){
    const history=useHistory();
    const redirectLogin=()=>history.push('/login');
    return  (
        <button onClick={redirectLogin}>Войти</button>
    )
}
class LoginButton extends React.Component{
    render(){
        return(
                this.props.is_authenticated() ?
                    <div class='login'>
                        <button onClick={()=>this.props.logout()}>Выйти</button>
                    </div>
                :
                    <div class='login'>
                        <Login />
                    </div>
            )
    }
}
export default LoginButton
