import React, { useState } from 'react';
import axios from 'axios';
import { Form, FormGroup, FormLabel, FormControl, Button } from 'react-bootstrap';

const CreateProject = () => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/projects/', {
        name,
        description,
      });
      console.log(response.data); //  success, e.g., show a success message
      setName('');
      setDescription('');
    } catch (error) {
      console.error(error); //  error, e.g., show an error message
    }
  };

  return (
     <div>
      <h2>Create Project</h2>
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
          <FormLabel>Description:</FormLabel>
          <FormControl
            as="textarea"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </FormGroup>
        <Button type="submit">Create Project</Button>
      </Form>
    </div>
  );
};

export default CreateProject;
