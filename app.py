from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    version = os.getenv("APP_VERSION", "0.1.0")
    return f"""
    <html>
        <body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
            <h1>Jerome's Exam Submission</h1>
            <p><strong>Course:</strong> BSIT</p>
            <p><strong>Skill:</strong> Containerization with Docker</p>
            <hr>
            <p>Current Version: {version}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

    