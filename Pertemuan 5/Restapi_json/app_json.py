from flask import Flask, jsonify, request, make_response
import json

app = Flask(__name__)
app.config['DEBUG'] = True

# Buka file JSON
with open('mahasiswa.json', 'r') as file_json:
    # Parsing data JSON
    data = json.load(file_json)

# Cetak isi data JSON
@app.route('/', methods=['GET'])
def index():
    for dtmhs in data['mahasiswa']:
        print(f"Nama: {dtmhs['nama']}")
        print("Sosial Media:")
        print(f"- Facebook: {dtmhs['social_media']['facebook']}")
        print(f"- Twitter: {dtmhs['social_media']['twitter']}")
        print(f"- Instagram: {dtmhs['social_media']['instagram']}")

    return make_response(jsonify({'Biodata': data}), 200)

if __name__ == '__main__':
    app.run()