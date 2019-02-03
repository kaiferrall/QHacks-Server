import React, { Component } from "react";
import "./App.css";

import CMDContainer from "./components/cli/CMDContainer";
import VideoContainer from "./components/video/VideoContainer";

class App extends Component {
  constructor() {
    super();
    this.state = {
      running: false
    };
    this.toggleStatus = this.toggleStatus.bind(this);
  }
  toggleStatus(command) {
    this.setState({ running: command });
  }
  render() {
    return (
      <div className="App">
        <div className="container">
          <div className="left">
            <VideoContainer running={this.state.running} />
          </div>
          <div className="right">
            <CMDContainer toggleStatus={this.toggleStatus} />
          </div>
        </div>
      </div>
    );
  }
}

export default App;
