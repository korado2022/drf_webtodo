import React from "react";

class TodoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {text_note: '', working: props.projects[0]?.id, author_todo: props.users[0]?.id}
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }


    handleSubmit(event) {
        this.props.createTodo(this.state.text_note, this.state.working, this.state.author_todo)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)} className="container">
                <div className="form-group">
                    <label htmlFor="text_note">text_note</label>
                        <input type="text" className="form-control"  name="text_note" value={this.state.text_note} 
                        onChange={(event)=>this.handleChange(event)} />
                </div>
                <div className="form-group">
                <label htmlFor="working">working</label>
                    <select name="working" className="form-control" onChange={(event)=>this.handleChange(event)}>
                        {this.props.projects.map((item)=><option value={item.id}>{item.title}</option>)}
                    </select>
                        
                </div>
                <div className="form-group">
                <label htmlFor="author_todo">author_todo</label>
                    <select name="author_todo" className="form-control" onChange={(event)=>this.handleChange(event)}>
                        {this.props.users.map((item)=><option value={item.id}>{item.username}</option>)}
                    </select>
                </div>

                <input type="submit" className="btn btn-primary" value="Save"></input>
            </form>
        );
    }
}

export default TodoForm