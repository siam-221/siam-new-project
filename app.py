from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    # এটি আপনার index.html ফাইলটিকে খুঁজে নিয়ে দেখাবে
    return send_from_directory(os.getcwd(), 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
