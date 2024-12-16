from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector App")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_handler():
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] == None:
        return "<strong>Invalid text! Please try again!</strong"
    else:
        return f"For the given statement, the system response is 'anger': {result['anger'] }, 'disgust': { result['disgust'] }, 'fear': { result['fear'] }, 'joy': { result['joy'] } and 'sadness': { result['sadness'] }. The dominant emotion is <strong>{ result['dominant_emotion'] }</strong>."
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)