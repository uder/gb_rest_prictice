import React from "react";
import {Link} from 'react-router-dom';


const MenuItem = ({menu_item}) =>{
    return (
        <li>
            <Link to={menu_item.path}>{menu_item.name}</Link>
        </li>
    )
}

const Menu=({menu_items})=>{
    return (
        <nav>
            <ul>
                {menu_items.map((item)=><MenuItem menu_item={item} />)}
            </ul>
        </nav>
    )
}

export default Menu