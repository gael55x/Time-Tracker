import React from 'react';
import axios from 'axios';
import { Button } from 'react-bootstrap';

const DeleteTask = ({ taskId }) => {
  const handleDelete = async () => {
    try {
      await axios.delete(`http://127.0.0.1:8000/task-descriptions/${taskId}/`);
      console.log('Task deleted successfully');
    } catch (error) {
      console.error(error); // error, e.g., show an error message
    }
  };

  return (
    <div>
      <h2>Delete Task</h2>
      <Button variant="danger" onClick={handleDelete}>Delete Task</Button>
    </div>
  );
};

export default DeleteTask;
