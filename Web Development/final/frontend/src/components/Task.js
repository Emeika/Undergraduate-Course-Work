import React from 'react';

const Task = ({ task, onDelete }) => {
    return (
        <div>
            <span>{task.title}</span>
            <button onClick={() => onDelete(task.id)}>Delete</button>
        </div>
    );
};

export default Task;
