import React, { Component } from "react";

class VideoContainer extends Component {
  render() {
    let time,
      link = "http://localhost:5000/video_feed";
    console.log(this.props.running);
    if (this.props.running) {
      link = "http://localhost:5000/model_feed";
      time = Date.now();
    }
    return (
      <div className="VideoContainer">
        <div id="video-container" className="flex-column">
          <h1>CloudTect - Object Detection</h1>
          <h4>Your Feed</h4>
          <img id="video" src={link} alt="" />
          <small id="image-info">{time}</small>
        </div>
        <div id="output-container" className="flex-column" />
      </div>
    );
  }
}

export default VideoContainer;
