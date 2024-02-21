import React, { useState } from 'react';
import { Form, FormGroup, FormLabel, FormControl, Button } from 'react-bootstrap';
import axios from 'axios';

const CreateTask = () => {
  const [name, setName] = useState('');
  const [user, setUser] = useState('');
  const [projectId, setProjectId] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/task-descriptions/', {
        name,
        user,
        project: projectId,
      });
      console.log(response.data); //  handles success, e.g., show a success message
      setName('');
      setUser('');
      setProjectId('');
    } catch (error) {
      console.error(error); //  handles error, e.g., show an error message
    }
  };

  return (
    <div>
      <h2>Create Task</h2>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <FormLabel>Name:</FormLabel>
          <FormControl
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </FormGroup>
        <FormGroup>
          <FormLabel>User:</FormLabel>
          <FormControl
            type="text"
            value={user}
            onChange={(e) => setUser(e.target.value)}
            required
          />
        </FormGroup>
        <FormGroup>
          <FormLabel>Project ID:</FormLabel>
          <FormControl
            type="number"
            value={projectId}
            onChange={(e) => setProjectId(e.target.value)}
            required
          />
        </FormGroup>
        <Button type="submit">Create Task</Button>
      </Form>
    </div>
  );
};

export default CreateTask;
