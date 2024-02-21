import React from 'react';
import axios from 'axios';
import { Button } from 'react-bootstrap';

const DeleteProject = ({ projectId }) => {
  const handleDelete = async () => {
    try {
      await axios.delete(`http://127.0.0.1:8000/projects/${projectId}/`);
      console.log('Project deleted successfully');
    } catch (error) {
      console.error(error); // show an error message
    }
  };

  return (
    <div>
      <h2>Delete Project</h2>
      <Button variant="danger" onClick={handleDelete}>Delete Project</Button>
    </div>
  );
};

export default DeleteProject;
