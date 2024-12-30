import requests
import json

def find_dominant_emotion(emotions_obj):
    max = 0
    dominant = None
    for emo_name, emo_score in emotions_obj.items():
        if float(emo_score) > max:
            max = float(emo_score)
            dominant = emo_name
        else:
            continue
    
    return dominant

# from EmotionDetection.emotion_detection import emotion_detector
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=headers)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        # print("\n", formatted_response, "\n")

        emotions = formatted_response['emotionPredictions'][0]["emotion"]
        # print("\n", emotions, "\n")

        dominant_emotion = find_dominant_emotion(emotions)
        print("\n Emotion for Text: ", text_to_analyse)
        print("\n Dominant Emotion: ", dominant_emotion, "\n")

        emotions["dominant_emotion"] = dominant_emotion
        # print("\n", emotions, "\n")

        return emotions

    elif response.status_code == 400:
        return {
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion": None
                }

    else: # when status code is NOT 200
        return "Something when wrong, please try again later."

