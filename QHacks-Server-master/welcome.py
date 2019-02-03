from flask import Flask, request, render_template, Response
from flask_cors import CORS
import json
from recorder import VideoCamera, VideoCamera2

app = Flask("App")
cors = CORS(app, resources={r"/*": {"origins": "*"}})


def gen(VideoCamera):
    while True:
        result, frame = VideoCamera.get_frame()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def gen_video(VideoCamera2):
    while True:
        frame = VideoCamera2.get_frame()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
def index():
    res = {"h": 1}

    return render_template('index.html', res=res)


@app.route('/result')
def get_result():
    def results(VideoCamera):
        while True:
            result = VideoCamera.get_results()

            yield result

    return Response(results(VideoCamera()), mimetype='multipart/x-mixed-replace')


@app.route("/model_feed")
def model_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed')
def video_feed():
    return Response(gen_video(VideoCamera2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/test", methods=["POST"])
def run_model():
    action_type = request.args.get("action")
    x = {
        "type": action_type
    }
    return Response(json.dumps(x))
