import json
from flask import Flask, request, jsonify
import inference
app=Flask(__name__)


@app.route('/')
def swati():
    return jsonify({'name':'swati','email':'pushpswati@gmail.com'})


@app.route('/api', methods=['GET'])
def query_recs():
    namev = request.args.get('name')
   # print(namev)
    
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == namev:
                return jsonify(records)
        return jsonify({'error': 'data not found'})

    
@app.route('/create', methods=['POST'])
def update_record():
    record = json.loads(request.data)  # Data comming 
    new_records = []
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)

    print(new_records)
    with open('data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


@app.route('/numberplt', methods=['POST'])
def numberplate():
    payload = json.loads(request.data)  # Data comming 
    image_url=payload['image_url']
    result=inference.predict(image_url)
    return jsonify(result)


if __name__=="__main__":
    app.run(host='0.0.0.0',port='8001')
    