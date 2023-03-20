from flask import Flask
from flask import send_from_directory

app = Flask(__name__, static_folder='/app')  

@app.route('/<path:filename>')  
def send_file(filename):  
    return send_from_directory(app.static_folder, filename)

app.run(host='0.0.0.0', port=8000)
