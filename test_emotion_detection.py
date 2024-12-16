
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection_joy(self):
        text_to_analyze = "I am glad this happened"
        assert emotion_detector(text_to_analyze).get('dominant_emotion') == "joy"

    def test_emotion_detection_anger(self):
        text_to_analyze = "I am really mad about this"
        assert emotion_detector(text_to_analyze).get('dominant_emotion') == "anger"

    def test_emotion_detection_disgust(self):
        text_to_analyze = "I feel disgusted just hearing about this"
        assert emotion_detector(text_to_analyze).get('dominant_emotion') == "disgust"

    def test_emotion_detection_sadness(self):
        text_to_analyze = "I am so sad about this"
        assert emotion_detector(text_to_analyze).get('dominant_emotion') == "sadness"

    def test_emotion_detection_fear(self):
        text_to_analyze = "I am really afraid that this will happen"
        assert emotion_detector(text_to_analyze).get('dominant_emotion') == "fear"
   
if __name__ == "__main__":
    unittest.main(verbosity=2)