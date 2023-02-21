import React from 'react';
import Container from 'react-bootstrap/Container';


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.title}</td>
            <td>{project.link_repo}</td>
            <td>{project.developers}</td>
        </tr>
    )
}


const ProjectList = ({projects}) => {
    return (
        <Container>
            <table>
                <th>Id</th>
                <th>Title</th>
                <th>Link repository</th>
                <th>Developers</th>
                {projects.map((project) => <ProjectItem project={project} />)}
            </table>
        </Container>
    )
}


export default ProjectList