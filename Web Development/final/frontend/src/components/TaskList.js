import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Task from './Task';
import TaskForm from './TaskForm';

const TaskList = () => {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/tasks/')
            .then(response => setTasks(response.data))
            .catch(error => console.error(error));
    }, []);

    const handleDelete = (taskId) => {
        axios.delete(`http://localhost:8000/api/tasks/${taskId}/`)
            .then(() => setTasks(tasks.filter(task => task.id !== taskId)))
            .catch(error => console.error(error));
    };

    const handleTaskAdded = (newTask) => {
        setTasks([...tasks, newTask]);
    };

    return (
        <div>
            <h2>Task List</h2>
            <TaskForm onTaskAdded={handleTaskAdded} />
            {tasks.map(task => (
                <Task key={task.id} task={task} onDelete={handleDelete} />
            ))}
        </div>
    );
};

export default TaskList;
