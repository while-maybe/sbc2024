import React from "react";

const Student = ({name, age}) => {
    
    return (
        <li>{name} is {age} years old{age > 21 ? " (Mature Student)": ""}</li>
    )
};

export default Student