import React from 'react'

class ToDoForm extends React.Component{
    constructor(props){
        super(props)
        this.state={
            project: 0,
            user: '',
            text: '',
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
        console.log(this.state.project)
        console.log(this.state.user)
        console.log(this.state.text)
        console.log(this.props.users)
        this.props.createTodo(this.state.project, this.state.user, this.state.text)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="project-field">project</label>
                    <select name="project" onChange={(event)=>this.handleChange(event)}>
                        {this.props.projects.map((item)=><option value={item.id}>{item.name}</option>)}
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="user-field">userCreator</label>
                    <select name="user" onChange={(event)=>this.handleChange(event)}>
                        {this.props.users.map((item)=><option value={item.uuid}>{item.userName}</option>)}
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="text-field">text</label>
                    <input
                        type="text"
                        name="text"
                        value={this.state.text}
                        onChange={(event)=>this.handleChange(event)}
                    />
                </div>
                <input type="submit" value="Сохранить"/>
            </form>
        );
    }

}

export default ToDoForm