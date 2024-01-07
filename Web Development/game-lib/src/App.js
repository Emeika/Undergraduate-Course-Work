import React, { useState, useEffect } from 'react';

import './App.css';
import LoadingPage from './components/LoadingPage';
import Navigation from './components/Navbar';

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
          <h1>Your Game Library App</h1>
          {/* Other components and content */}
        </div>
      )}
    </div>
  );
};

export default App;
