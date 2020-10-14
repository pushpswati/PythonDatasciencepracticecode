import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_records():
    namev = request.args.get('name')
   # print(namev)
    
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for k in records:
            if records[k] == namev:
                return jsonify(records)
        return jsonify({'error': 'data not found'})
app.run(host='0.0.0.0',port='8001')