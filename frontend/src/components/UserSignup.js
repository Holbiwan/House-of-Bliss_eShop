import React, { useState } from 'react';
import axios from 'axios';

function UserSignup() {
  const [userData, setUserData] = useState({
    username: '',
    email: '',
    password: '',
    address: '',
    bio: '',
  });

  const handleChange = (e) => {
    setUserData({ ...userData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/users/', userData);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Sign Up</h1>
      <form onSubmit={handleSubmit}>
        <input
          name="username"
          value={userData.username}
          onChange={handleChange}
          placeholder="Username"
          required
        />
        <input
          name="email"
          type="email"
          value={userData.email}
          onChange={handleChange}
          placeholder="Email"
          required
        />
        <input
          name="password"
          type="password"
          value={userData.password}
          onChange={handleChange}
          placeholder="Password"
          required
        />
        <input
          name="address"
          value={userData.address}
          onChange={handleChange}
          placeholder="Address"
        />
        <textarea
          name="bio"
          value={userData.bio}
          onChange={handleChange}
          placeholder="Bio"
        />
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
}

export default UserSignup;
