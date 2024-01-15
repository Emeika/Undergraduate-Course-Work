import logo from './logo.svg';
import './App.css';
import Greetings from './components/Greetings';
import Counter from './components/Counter';

import React, { useState } from 'react';

const App = () => {
  const [name, setName] = useState('');

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  return (
    <div>
      <label>
        Name: 
        <input type="text" value={name} onChange={handleNameChange} />
      </label>
      <Greetings name={name} />
      <Counter />

    </div>
  );
};

export default App;
