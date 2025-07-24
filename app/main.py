from flask import Flask, request, jsonify, redirect
from datetime import datetime
from .models import url_store, create_url_entry, increment_clicks, get_url_entry
from .utils import generate_short_code, validate_url

app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "URL is required"}), 400

    long_url = data['url']

    if not validate_url(long_url):
        return jsonify({"error": "Invalid URL format"}), 400

    # Generate a unique short code
    short_code = generate_short_code()
    while short_code in url_store:
        short_code = generate_short_code()

    # Store the URL entry
    create_url_entry(short_code, long_url)

    short_url = request.host_url + short_code
    return jsonify({
        "short_code": short_code,
        "short_url": short_url
    })

@app.route('/<short_code>', methods=['GET'])
def redirect_short(short_code):
    entry = get_url_entry(short_code)
    if not entry:
        return jsonify({"error": "Short code not found"}), 404

    increment_clicks(short_code)
    return redirect(entry["url"])

@app.route('/api/stats/<short_code>', methods=['GET'])
def url_stats(short_code):
    entry = get_url_entry(short_code)
    if not entry:
        return jsonify({"error": "Short code not found"}), 404

    return jsonify({
        "url": entry["url"],
        "clicks": entry["clicks"],
        "created_at": entry["created_at"].isoformat()  # serialize datetime to string
    })

if __name__ == '__main__':
    # Run the Flask development server
    app.run(host='0.0.0.0', port=5000, debug=True)
