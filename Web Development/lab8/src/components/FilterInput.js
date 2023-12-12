// FilterInput.js

import React, { useState } from 'react';

const FilterInput = ({ onFilter }) => {
  const [filterValue, setFilterValue] = useState('');

  const handleInputChange = (e) => {
    const value = e.target.value;
    setFilterValue(value);
    onFilter(value);
  };

  return (
    <div>
      <label>Filter by: </label>
      <input type="text" value={filterValue} onChange={handleInputChange} />
    </div>
  );
};

export default FilterInput;
