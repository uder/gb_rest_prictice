import React from "react";

const ProjectItem = ({project}) => {
    return(
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.repoUrl}
            </td>
        </tr>
    )
}

const ProjectList=({projects})=>{
    return (
        <table>
            <th>Project Name</th>
            <th>Repository URL</th>
            {projects.map((current)=><ProjectItem project={current} />)}
        </table>
    )
}

export default ProjectList