from flask import Flask, render_template
import requests 


app = Flask(__name__)

@app.route('/')
def root():
    return " premier league standings"

@app.route('/premierleaguefelix')
def premier():
    url = "https://premier-league-standings1.p.rapidapi.com/"

    headers = {
        "X-RapidAPI-Key": "5e081a9dfbmshce86c4bcf156378p12cb19jsn442f7a6e1973",
        "X-RapidAPI-Host": "premier-league-standings1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    klasmen = response.json()

    return render_template('premier.html', data=klasmen)
  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' )