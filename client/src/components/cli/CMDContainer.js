import React, { Component } from "react";
import axios from "axios";

class CMDContainer extends Component {
  constructor() {
    super();
    this.state = {
      command: "",
      history: [],
      status: false
    };
    this.onSubmit = this.onSubmit.bind(this);
    this.onChange = this.onChange.bind(this);
  }

  onSubmit(e) {
    e.preventDefault();
    if (this.state.command == "cls") {
      this.setState({ command: "", history: [], status: false });
    } else {
      switch (this.state.command) {
        case "run":
          this.props.toggleStatus(true);
          this.setState({ status: true });
          break;
        case "stop":
          this.props.toggleStatus(false);
          this.setState({ status: false });
          break;
      }
      let updatedHistory = this.state.history;
      updatedHistory.push(this.state.command);
      this.setState({
        command: "",
        history: updatedHistory
      });
    }
  }

  onChange(e) {
    this.setState({ command: e.target.value });
  }
  render() {
    let loading;
    if (this.state.status) {
      loading = (
        <div>
          <p>running object detection on footage...</p>
        </div>
      );
    }
    let rows = this.state.history.map((row, index) => {
      return (
        <form readOnly={true} key={index} id="cli-form" className="flex-row">
          <p>$:</p>
          <input
            style={{ color: "white" }}
            readOnly={true}
            value={row}
            id="cli-input"
            type="text"
          />
        </form>
      );
    });
    return (
      <div className="CMDContainer">
        <div className="flex-column">
          <p>Welcome (run a command to get started)</p>
          {rows}
          {loading}
          <form id="cli-form" onSubmit={this.onSubmit} className="flex-row">
            <p>$:</p>
            <input
              style={{ color: "white" }}
              autoComplete="off"
              onChange={this.onChange}
              value={this.state.command}
              id="cli-input"
              type="text"
            />
          </form>
        </div>
        <div className="instructions">
          <small>run - starts model</small>
          <br />
          <small>cls - clear inputs</small>
        </div>
      </div>
    );
  }
}

export default CMDContainer;
