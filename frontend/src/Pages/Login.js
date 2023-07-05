import React, { useState } from "react";
import { Card, Form, Button, Container } from "react-bootstrap";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isReady, setIsReady] = useState(false);

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const sendData = async () => {
    try {
      const body = {
        username,
        password,
      };
      const response = await fetch("http://localhost:5000/api/datosUsuario", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      })
        .then((resp) => resp.json())
        .then((json) => {
          //console.log(json)
          setIsReady(true);
        });
    } catch (error) {
      console.error("Error al mandar los datos del login:", error);
    }
  };

  return (
    <Container>
      <Card style={{ width: "300px" }}>
        <Card.Body>
          <Card.Title>Iniciar sesión</Card.Title>
          <Form>
            <Form.Group controlId="formUsername">
              <Form.Label>Usuario:</Form.Label>
              <Form.Control
                type="text"
                value={username}
                onChange={handleUsernameChange}
              />
            </Form.Group>
            <Form.Group controlId="formPassword">
              <Form.Label>Contraseña:</Form.Label>
              <Form.Control
                type="password"
                value={password}
                onChange={handlePasswordChange}
              />
            </Form.Group>
            <Button variant="primary" onClick={sendData}>
              Iniciar sesión
            </Button>
          </Form>
        </Card.Body>
      </Card>
    </Container>
  );
}

export default Login;
