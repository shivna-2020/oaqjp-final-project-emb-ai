"""
Emotion Detector App using Flask

This module provides a simple web interface to detect emotions 
in text using the EmotionDetection library. 
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector App")

@app.route("/")
def index():
    """
    Render the homepage.

    This route serves the index.html template
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_handler():
    """
    Handle the emotion detection request.

    This route processes a GET request with a query parameter 
    `textToAnalyze` containing the text to analyze. 
    Returns:
        str: An HTML-formatted response 
    """
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "<strong>Invalid text! Please try again!</strong>"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <strong>{result['dominant_emotion']}</strong>."
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
