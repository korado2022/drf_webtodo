import React from "react";

class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {title: '', link_repo: '', developers: []}
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }


    handleSubmit(event) {
        this.props.createProject(this.state.title, this.state.link_repo, this.state.developers)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)} className="container">
                <div className="form-group">
                    <label htmlFor="title">title</label>
                        <input type="text" className="form-control"  name="title" value={this.state.title} 
                        onChange={(event)=>this.handleChange(event)} />
                </div>
                <div className="form-group">
                <label htmlFor="link_repo">link_repo</label>
                        <input type="text" className="form-control" name="link_repo" value={this.state.link_repo} 
                        onChange={(event)=>this.handleChange(event)} />
                </div>
                <div className="form-group">
                <label htmlFor="developers">developers</label>
                        <input type="number" className="form-control" name="developers" value={this.state.developers} 
                        onChange={(event)=>this.handleChange(event)} />
                </div>
                <input type="submit" className="btn btn-primary" value="Save"></input>
            </form>
        );
    }
}

export default ProjectForm