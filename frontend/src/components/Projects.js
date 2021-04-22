import React from "react";
import {Link} from 'react-router-dom';

const ProjectItem = ({project, deleteProject}) => {
    return(
        <tr>
            <td>
                <Link to={`project/${project.id}`}>{project.name}</Link>
            </td>
            <td>
                {project.repoUrl}
            </td>
            <td>
                <button onClick={()=>deleteProject(project.id)} type='button'>Удалить</button>
            </td>
        </tr>
    )
}

const ProjectList=({projects, deleteProject})=>{
//    let { id } = useParams();
//    let filtered_projects=projects.filter((project) => projects.id === id)
//    console.log({id})
//    console.log(filtered_projects)
    return (
        <table>
            <thead>
                <tr>
                    <th>Project Name</th>
                    <th>Repository URL</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {projects.map((project)=><ProjectItem project={project} deleteProject={deleteProject}/>)}
            </tbody>
        </table>
    )
}

export default ProjectList