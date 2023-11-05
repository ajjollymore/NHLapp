from flask import Flask
import backend.scraper as scraper
app = Flask(__name__)
@app.route('/')
def hello():
    scores = scraper.NFLScores()
    return scores

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")