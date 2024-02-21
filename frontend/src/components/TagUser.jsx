// LACKING: BACKEND  URL FOR projects/<int:pk>/users so I can tag the users on that project -> A mistake on my part. 
// I JUST REalized this on the moment... i wasn't able to plan things out properly -> my mistake.. specifications were ambiguous in the first place



/* COMMENTED OUT: WIP */
/* import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TagUsers = ({ projectId }) => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/projects/${projectId}/users/`);
        setUsers(response.data);
      } catch (error) {
        console.error(error); //  error, e.g., show an error message
      }
    };
    fetchUsers();
  }, [projectId]);

  return (
    <div>
      <h2>Users Assigned to Project</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id}>{user.username}</li>
        ))}
      </ul>
    </div>
  );
};

export default TagUsers;
 */