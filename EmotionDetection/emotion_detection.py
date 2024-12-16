import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data = { "raw_document": { "text": text_to_analyze } }

    result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    response = requests.post(url, json=json_data, headers=headers)

    if response.status_code == 400:
        return result 

    response_json = json.loads(response.text)

    if "emotionPredictions" in response_json and len(response_json["emotionPredictions"]):
        predictions = response_json["emotionPredictions"][0]
        
        if 'emotion' in predictions:
            max_score = 0
            for emotion_name in ("anger", "disgust", "fear", "joy", "sadness"):
                if emotion_name in predictions['emotion']:
                    current_score = predictions['emotion'][emotion_name] 
                    
                    if current_score > max_score:
                        result['dominant_emotion'] = emotion_name
                        max_score = current_score
                    
                    result[emotion_name] = current_score

    return result    


