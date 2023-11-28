import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import TravelJournal from './components/Journal';

function App() {
  return (
    <div className="App">
      <Navbar />
      <main>
        <TravelJournal />
      </main>
      <footer>
        <p>© 2023 My Travel App</p>
      </footer>
    </div>
  );
}

export default App;
