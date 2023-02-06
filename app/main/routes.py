from base64 import b64encode
from io import BytesIO

import cv2
import numpy as np
from PIL import Image
from flask import render_template, Response, flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from werkzeug.exceptions import abort
from wtforms import FileField, SubmitField
from app.main import main_bp
from app.main.camera import Camera
from source.test_new_images import detect_cig_in_image
from source.video_detector import detect_cig_in_frame
from flask import Flask, jsonify
import os

cig_or_not ='No Smoking'
confidence = 100
@main_bp.route("/")
def home_page():
    return render_template("home_page.html")

@main_bp.route("/data")
def data():
    global cig_or_not
    global confidence
    return jsonify(cig_or_not=cig_or_not,confidence=confidence)

@main_bp.route("/penjelasan_model")
def penjelasan_model():
    return render_template("penjelasan_model.html")

@main_bp.route("/pengujian")
def pengujian():
    return render_template("pengujian.html")


def gen(camera):
    global cig_or_not
    global confidence
    while True:
        frame = camera.get_frame()
        frame_processed,cig_or_not,confidence = detect_cig_in_frame(frame)
        frame_processed = cv2.imencode('.jpg', frame_processed)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_processed + b'\r\n')


@main_bp.route('/video_feed')
def video_feed():
    return Response(gen(
        Camera()
    ),
        mimetype='multipart/x-mixed-replace; boundary=frame')


def allowed_file(filename):
    ext = filename.split(".")[-1]
    is_good = ext in ["jpg", "jpeg", "png"]
    return is_good


@main_bp.route("/image-cig-detector", methods=["GET", "POST"])
def image_cig_detector():
    return render_template("image_detector.html",form = PhotoCigForm())


@main_bp.route("/image-processing", methods=["POST"])
def image_processing():
    form = PhotoCigForm()

    if not form.validate_on_submit():
        flash("An error occurred", "danger")
        abort(Response("Error", 400))

    pil_image = Image.open(form.image.data)
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    array_image = detect_cig_in_image(image)
    rgb_image = cv2.cvtColor(array_image, cv2.COLOR_BGR2RGB)
    image_detected = Image.fromarray(rgb_image, 'RGB')

    with BytesIO() as img_io:
        image_detected.save(img_io, 'PNG')
        img_io.seek(0)
        base64img = "data:image/png;base64," + b64encode(img_io.getvalue()).decode('ascii')
        return base64img
        
@main_bp.route("/about")
def about():
    return render_template("about.html")

# form
class PhotoCigForm(FlaskForm):
    image = FileField('Choose image:',
                      validators=[
                          FileAllowed(['jpg', 'jpeg', 'png', 'jfif'], 'The allowed extensions are: .jpg, .jpeg, .jfif and .png')])

    submit = SubmitField('Detect')
