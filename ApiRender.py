from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_excel("dataserformateado.xlsx")

@app.route('/data', methods=['GET'])
def get_data():
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
