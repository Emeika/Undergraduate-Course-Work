// App.js
import React from 'react';
import Form from './components/Form';
import ToDo from './components/ToDo';
import './App.css'; // Import your combined CSS file

const App = () => {
  return (
    <div className="app-container">
      <div className="form-container">
        <h1>Form</h1>
        <Form />
      </div>
      <div className="todo-container">
        <h1>To Do APP</h1>
        <ToDo />
      </div>
    </div>
  );
};

export default App;
