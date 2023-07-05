import React, { Fragment, useEffect, useState } from "react";
import { Route, Switch, Redirect } from "react-router-dom";
import Login from "./Pages/Login";

function App() {
  const [data, setData] = useState("");

  useEffect(() => {
    fetchData();
  }, []);

  async function fetchData() {
    const response = await fetch("http://localhost:5000/api/data");
    const jsonData = await response.json();
    setData(jsonData.message);
    console.log(jsonData.message);
  }

  return (
    <Switch>
      <Route path="/" exact>
        <Redirect to="/login"></Redirect>
      </Route>

      <Route path="/login">
        <Login></Login>
      </Route>
    </Switch>
  );
}

export default App;
