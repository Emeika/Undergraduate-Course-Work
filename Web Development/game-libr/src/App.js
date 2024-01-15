import React, { useState, useEffect } from 'react';

import './App.css';
import LoadingPage from './components/LoadingPage';
import Navigation from './components/Navbar';
import HomePage from './components/HomePage';

const App = () => {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Simulate some async operation (e.g., loading data or assets)
    setTimeout(() => {
      setIsLoading(false);
    }, 2000); // Adjust the duration as needed
  }, []);

  return (
    <div>
      <Navigation />
      {isLoading ? (
        <LoadingPage />
      ) : (
        // Your main content goes here
        <div>
          <HomePage />
          {/* Other components and content */}
        </div>
      )}
    </div>
  );
};

export default App;
