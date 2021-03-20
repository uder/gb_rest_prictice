import React from "react";
import {Link} from 'react-router-dom';

const ProjectItem = ({project}) => {
    return(
        <tr>
            <td>
                <Link to={`project/${project.id}`}>{project.name}</Link>
            </td>
            <td>
                {project.repoUrl}
            </td>
        </tr>
    )
}

const ProjectList=({projects})=>{
//    let { id } = useParams();
//    let filtered_projects=projects.filter((project) => projects.id === id)
//    console.log({id})
//    console.log(filtered_projects)
    return (
        <table>
            <th>Project Name</th>
            <th>Repository URL</th>
            {projects.map((current)=><ProjectItem project={current} />)}
        </table>
    )
}

export default ProjectList