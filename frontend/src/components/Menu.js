import React from "react";

const MenuItem = ({menu_item}) =>{
    return (
        <li>
            {menu_item.name}
        </li>
    )
}

const Menu=({menu_items})=>{
    return (
        <ul>
            {menu_items.map((item)=><MenuItem menu_item={item} />)}
        </ul>
    )
}

export default Menu