import React from "react";
import { useParams } from "react-router-dom";
import Container from 'react-bootstrap/Container';

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.title}</td>
            <td>{project.developers}</td>
        </tr>
    )
}

const ProjectListUsers = ({projects}) => {

    let { id } = useParams();
    let filter_item = projects.filter((project => project.users.includes(parseInt(id))))

    return (
        <Container>
            <table>
                <th>Id</th>
                <th>Title</th>
                <th>Developers</th>
                {filter_item.map((project) => <ProjectItem project={project} />)}
            </table>
        </Container>
    )





}

export default ProjectListUsers