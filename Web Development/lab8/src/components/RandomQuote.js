// RandomQuote.js

import React, { useState, useEffect } from 'react';

const RandomQuote = () => {
  const [quote, setQuote] = useState(null);

  useEffect(() => {
    // Function to fetch a random quote from the API
    const fetchRandomQuote = async () => {
      try {
        const response = await fetch('https://api.quotable.io/random');
        const data = await response.json();
        setQuote(data);
      } catch (error) {
        console.error('Error fetching random quote:', error);
      }
    };

    // Fetch a random quote when the component mounts
    fetchRandomQuote();

    // Set up an interval to fetch a new random quote every 10 seconds
    const intervalId = setInterval(fetchRandomQuote, 10000);

    // Clean up the interval on component unmount
    return () => clearInterval(intervalId);
  }, []); // Empty dependency array to run the effect only once on mount

  return (
    <div>
      <h2>Random Quote</h2>
      {quote && (
        <div>
          <p>{quote.content}</p>
          <p>- {quote.author}</p>
        </div>
      )}
    </div>
  );
};

export default RandomQuote;
