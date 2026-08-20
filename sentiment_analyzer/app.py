from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['GET'])
def analyze():
    text = request.args.get('text', '')
    if not text:
        return jsonify({"sentiment": "neutral"})
    # Simple naive sentiment logic to meet the requirement
    text_lower = text.lower()
    if 'fantastic' in text_lower or 'good' in text_lower or 'great' in text_lower:
        return jsonify({"sentiment": "positive"})
    elif 'bad' in text_lower or 'terrible' in text_lower or 'awful' in text_lower:
        return jsonify({"sentiment": "negative"})
    else:
        return jsonify({"sentiment": "neutral"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
