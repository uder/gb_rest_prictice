import React from "react";
import {useParams} from 'react-router-dom';

const ProjectItem = ({project}) => {
    return(
        <tr>
            <td>
                {project.id}
            </td>
            <td>
                {project.name}
            </td>
            <td>
                {project.repoUrl}
            </td>
        </tr>
    )
}

const ProjectInfo=({projects})=>{
    let { id } = useParams();
    let filtered_projects=projects.filter((project) => project.id === parseInt(id));
    console.log({id})
    console.log(filtered_projects)
    console.log(projects)
    return (
        <table>
            <th>Project Name</th>
            <th>Repository URL</th>
            {filtered_projects.map((current)=><ProjectItem project={current} />)}
        </table>
    )
}

export default ProjectInfo