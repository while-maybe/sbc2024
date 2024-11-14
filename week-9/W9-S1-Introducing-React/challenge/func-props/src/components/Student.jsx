import React from "react";

const Student = ({name, age, onClickStudent}) => {
    
    return (
        <li>{name} is {age} years old {age > 21 ? " (Mature Student)": ""}
        <button onClick={() => onClickStudent(name)}>Say hi</button>
        </li>
    )
};

export default Student