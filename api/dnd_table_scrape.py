import pandas as pd
from pandas.core.frame import DataFrame
import requests
from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def index():
    data = WildMagicAffect(10, 3).search().info
    return json.dumps({'affect': data})

@app.route('/roll/<int:d20>/<int:d100>', methods=['GET'])
def show_affect(d20, d100):
    if d20 > 20 or d20 < 1:
        return json.dumps({'error': "d20 is out of range"})
    if d100 > 100 or d100 < 1:
        return json.dumps({'error': "d100 is out of range"})
    data = WildMagicAffect(d20, d100).search().info
    return json.dumps({'affect': data})


class WildMagicAffect():

    def __init__(self, d20: int, d100: int):
        self.d20 = d20
        self.d100 = d100
        self.info: str

    def search(self) -> object:
        self.info = affects.loc[affects["d20/d100"]== self.d100, match_d20_header(self.d20)].values[0]
        return self


def match_d20_header(d20: int) -> str:
    if d20 in range(1, 4):
        return "1-3/Extreme"
    if d20 in range(4, 10):
        return "4-9/Moderate"
    if d20 in range(10, 21):
        return "10-20/Nuisance"
    raise ValueError("That wasn't a d20")

def get_table(url= "https://www.dandwiki.com/wiki/Wild_Magic_Surge_Table,_Variant_(5e_Variant_Rule)") -> DataFrame:
    resp = requests.get(url)
    return pd.read_html(resp.text, header=0)[0]

# Pulls the table into a pandas df and stores it in memory to reduce requests to the external site
affects = get_table()

if __name__ == "__main__":
    app.run()