// UserList.js

import React, { useState, useEffect } from 'react';

const User = ({ user }) => (
  <li>
    {user.name} - {user.company.name} - {user.address.city}
  </li>
);

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [filteredUsers, setFilteredUsers] = useState([]);
  const [filterValue, setFilterValue] = useState('');

  useEffect(() => {
    // Fetch data when the component mounts
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => response.json())
      .then(data => {
        setUsers(data);
        setFilteredUsers(data); // Initially set filtered users to all users
      });
  }, []); // Empty dependency array to run the effect only once on mount

  const handleFilter = (value) => {
    setFilterValue(value);
    // Implement filtering logic based on company name, city, or any other relevant property
    const filtered = users.filter(user =>
      user.company.name.toLowerCase().includes(value.toLowerCase()) ||
      user.address.city.toLowerCase().includes(value.toLowerCase()) ||
      // Add additional relevant properties for filtering
      // user.property.toLowerCase().includes(value.toLowerCase()) ||
      false // placeholder for additional conditions
    );
    setFilteredUsers(filtered);
  };

  return (
    <div>
      <label>Filter by: </label>
      <input type="text" value={filterValue} onChange={(e) => handleFilter(e.target.value)} />
      <ul>
        {filteredUsers.map(user => (
          <User key={user.id} user={user} />
        ))}
      </ul>
    </div>
  );
};

export default UserList;
