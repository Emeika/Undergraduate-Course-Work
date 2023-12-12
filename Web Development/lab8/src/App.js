// App.js

import React from 'react';
import UserList from './components/UserList';
import RandomQuote from './components/RandomQuote';
import './App.css';

const App = () => {
  return (
    <div>
      <h1>User List</h1>
      <UserList />
      <div>
        <RandomQuote />
    </div>
    </div>
    
    
  );
};

export default App;
