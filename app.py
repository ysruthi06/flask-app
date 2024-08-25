from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get("data", [])
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    lowercase_alphabets = [x for x in alphabets if x.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets, default="", key=lambda x: x.lower())
    
    response = {
        "is_success": True,
        "user_id": "sruthi_06122003",  # replace with your full name and DOB
        "email": "sruthiy06@gmail.com",  # replace with your email
        "roll_number": "21BRS1236",  # replace with your roll number
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }
    
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
