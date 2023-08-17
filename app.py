from flask import Flask, render_template, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_file', methods=['POST'])
def process_file():
    try:
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # Save the uploaded file
            file_path = os.path.join('uploads', uploaded_file.filename)
            uploaded_file.save(file_path)

            # Run the Python script
            script_output = subprocess.check_output(['python', 'reference_scrape.py', file_path], universal_newlines=True)

            return jsonify({'result': script_output})
        else:
            return jsonify({'error': 'No file uploaded'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
