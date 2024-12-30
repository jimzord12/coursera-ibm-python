from flask import render_template, request, Flask
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import requests


#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
# Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    if label is None:
        return
        
    # Return a formatted string with the sentiment label and score
    a = "The given text has been identified as {} with a score of {}."
    return a.format(label.split('_')[1], score)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, True)
