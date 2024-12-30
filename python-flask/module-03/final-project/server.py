"""
Flask application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask app
APP = Flask("EmotionDetector")


@APP.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotion of the provided text.

    Retrieves the text from the request arguments, uses the emotion_detector
    function to analyze the emotions, and returns a formatted response.

    Returns:
        str: A response string with the detected emotions and the dominant emotion.
             If the text is invalid, returns an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        # This means that there was an error
        return "Invalid text! Please try again!"

    # Construct the response using proper string formatting
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


@APP.route("/")
def render_index_page():
    """
    Render the main application page.

    Returns:
        str: The rendered HTML of the main index page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5001, debug=True)
