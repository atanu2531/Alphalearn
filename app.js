import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Dashboard from './components/Dashboard';
import Lesson from './components/Lesson';
import Quiz from './components/Quiz';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Switch>
          <Route path="/dashboard" component={Dashboard} />
          <Route path="/lesson/:id" component={Lesson} />
          <Route path="/quiz/:id" component={Quiz} />
          <Route path="/" exact component={Dashboard} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
