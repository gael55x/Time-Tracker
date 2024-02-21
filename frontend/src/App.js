import './App.css';
import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Container, Button, Row, Col, Card, Form } from 'react-bootstrap';
import CreateProject from './components/CreateProject';
import CreateTask from './components/CreateTask';
/* TagUser component is currently WIP */
/* import TagUser from './components/TagUser'; */
import DeleteProject from './components/DeleteProject';
import DeleteTask from './components/DeleteTask';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const client = axios.create({
  baseURL: "http://127.0.0.1:8000"
});


function App() {

  const [currentUser, setCurrentUser] = useState();
  const [userData, setUserData] = useState(null);
  const [registrationToggle, setRegistrationToggle] = useState(false);
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  useEffect(() => {
    client.get("/user/")
    .then(function(res) {
      setCurrentUser(true);
      // response has a user object
      setUserData(res.data.user); 
    })
    .catch(function(error) {
      setCurrentUser(false);
    });
  }, []);

  function update_form_btn() {
    if (registrationToggle) {
      document.getElementById("form_btn").innerHTML = "Register";
      setRegistrationToggle(false);
    } else {
      document.getElementById("form_btn").innerHTML = "Log in";
      setRegistrationToggle(true);
    }
  }

  function submitRegistration(e) {
    e.preventDefault();
    client.post(
      "/register/",
      {
        email: email,
        username: username,
        password: password
      }
    ).then(function(res) {
      client.post(
        "/login/",
        {
          email: email,
          username: username,
          password: password
        }
      ).then(function(res) {
        setCurrentUser(true);
      });
    });
  }

  function submitLogin(e) {
    e.preventDefault();
    client.post(
      "/login/",
      {
        email: email,
        username: username,
        password: password
      }
    ).then(function(res) {
      setCurrentUser(true);
    });
  }

  function submitLogout(e) {
    e.preventDefault();
    client.post(
      "/logout/",
      {withCredentials: true}
    ).then(function(res) {
      setCurrentUser(false);
    });
  }

  if (currentUser) {
    return (
      <div>
        <Navbar bg="dark" variant="dark">
          <Container>
            <Navbar.Brand>Time-Tracker App</Navbar.Brand>
            <Navbar.Toggle />
            <Navbar.Collapse className="justify-content-end">
              <Navbar.Text className="custom-nav-text">
                Signed in as: <strong>{userData.username}</strong>
              </Navbar.Text>
              <Navbar.Text>
                <Form onSubmit={e => submitLogout(e)}>
                  <Button type="submit" variant="light">Log out</Button>
                </Form>
              </Navbar.Text>
            </Navbar.Collapse>
          </Container>
        </Navbar>
        {userData && (
          <div>
            <Container className="mt-4">
              <div className="text-center">
                <h2 style={{ marginBottom: '20px' }}>Welcome, {userData.username}!</h2>
                <Card style={{ width: '400px', margin: '0 auto', padding: '20px' }}>
                  <Card.Body>
                    <Card.Title>Your Profile</Card.Title>
                    <Card.Text>
                      <p><strong>Username:</strong> {userData.username}</p>
                      <p><strong>Email:</strong> {userData.email}</p>
                    </Card.Text>
                    {/* Edit Profile button for next version */}
                    {/* <Button variant="primary">Edit Profile</Button> */}
                  </Card.Body>
                </Card>
              </div>
            </Container>
            <Container className="mt-5">
              <Row>
                <Col md={4}>
                  <CreateProject />
                </Col>
                <Col md={4}>
                  <CreateTask />
                </Col>
                <Col md={4}>
                  {/* WIP */}
                  {/* <TagUser /> */}
                </Col>
              </Row>
              <Row>
                <Col md={4}>
                  {/* I NEED TO EDIT THIS SUCH THAT IT handles projectID for dynamic purposes */}
                  <DeleteProject projectId={1} />
                </Col>
                <Col md={4}>
                  {/* I NEED TO EDIT THIS SUCH THAT IT handles TaskId for dynamic purposes */}
                  <DeleteTask taskId={1} />
                </Col>
              </Row>
            </Container>

        </div>
        )}
      </div>
    );
  }
  return (
    <div>
    <Navbar bg="dark" variant="dark">
      <Container>
        <Navbar.Brand>Time-Tracker App</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end">
          <Navbar.Text>
            <Button id="form_btn" onClick={update_form_btn} variant="light">Register</Button>
          </Navbar.Text>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    {
      registrationToggle ? (
        <div className="center">
          <Form onSubmit={e => submitRegistration(e)}>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Email address</Form.Label>
              <Form.Control type="email" placeholder="Enter email" value={email} onChange={e => setEmail(e.target.value)} />
              <Form.Text className="text-muted">
                We'll never share your email with anyone else.
              </Form.Text>
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicUsername">
              <Form.Label>Username</Form.Label>
              <Form.Control type="text" placeholder="Enter username" value={username} onChange={e => setUsername(e.target.value)} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
            </Form.Group>
            <Button variant="primary" type="submit">
              Submit
            </Button>
          </Form>
        </div>        
      ) : (
        <div className="center">
          <Form onSubmit={e => submitLogin(e)}>
            <Form.Group className="mb-3" controlId="formBasicUsername">
              <Form.Label>Username</Form.Label>
              <Form.Control type="text" placeholder="Enter username" value={username} onChange={e => setUsername(e.target.value)} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Email address</Form.Label>
              <Form.Control type="email" placeholder="Enter email" value={email} onChange={e => setEmail(e.target.value)} />
              <Form.Text className="text-muted">
                We'll never share your email with anyone else.
              </Form.Text>
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
            </Form.Group>
            <Button variant="primary" type="submit">
              Submit
            </Button>
          </Form>
        </div>
      )
    }
    </div>
  );
}


export default App;