import React, { useState } from 'react';

const Counter = () => {
  const [count, setCount] = useState(0);

  const incrementCount = () => {
    setCount(count + 1);
    };
    
    const decrementCount = () => {
    setCount(count -1);
  };

  return (
    <div>
      <br></br>
      <p>Count: {count}</p>
        <button onClick={incrementCount}>increment</button>
          <button onClick={decrementCount}>decrement</button>
          
    </div>
  );
};

export default Counter;
