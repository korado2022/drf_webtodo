import React from 'react';
import Nav from 'react-bootstrap/Nav';



const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.title}</td>
            <td>{project.link_repo}</td>
            <td>{project.developers}</td>
            <td><button onClick={ ()=> deleteProject(project.id) } type='button'>Delete</button></td>
        </tr>
    )
}


const ProjectList = ({projects, deleteProject}) => {
    return (
            <div className='container'>
                <table>
                    <th>Id</th>
                    <th>Title</th>
                    <th>Link repository</th>
                    <th>Developers</th>
                    <th></th>
                    {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject} />)}
                </table>
                <Nav.Link href='/projects/create'>Create</Nav.Link>
            </div>
    )
}


export default ProjectList