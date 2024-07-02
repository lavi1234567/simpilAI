
from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('execute_app.html')

@app.route('/submit_selected_text', methods=['POST'])
def submit_selected_text():
    selected_text = request.json.get('selected_text')
    
    with open("input.txt", "w") as file:
        file.write(selected_text)
    
  
    try:
        subprocess.run(['python', 'app.py'])
       
        with open("llama_output.txt", "r") as file:
            output = file.read()
        return jsonify({'output': output})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
