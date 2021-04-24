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
        this.props.createTodo(this.state.project, this.state.user, this.state.text)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="project-field">project</label>
                    <input
                        type="number"
                        name="project"
                        value={this.state.project}
                        onChange={(event)=>this.handleChange(event)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="user-field">userCreator</label>
                    <input
                        type="text"
                        name="user"
                        value={this.state.userCreator}
                        onChange={(event)=>this.handleChange(event)}
                    />
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