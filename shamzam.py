from flask import Flask, request
import requests
import os 

app = Flask(__name__)

API_TOKEN =  os . environ ["KEY"] # Must set key first

@app.route("/recognize", methods=["POST"])
def recognize():
    if "file" not in request.files:
        return {"error": "No file provided"}, 400
    
    file = request.files["file"]
    if file.filename == "":
        return {"error": "No selected file"}, 400

    url = "https://api.audd.io/"
    files = {"file": file}

    data = {
        "api_token": API_TOKEN,
    }

    response = requests.post(url, files=files, data=data)

    if response.status_code != 200 or not response.text.strip():
        return {"error": "Invalid response from API"}, 500

    try:
        result = response.json()
    except requests.exceptions.JSONDecodeError:
        return {"error": "Failed to parse JSON response"}, 500

    if result.get("status") == "success" and result.get("result"):
        return {
            "title": result["result"]["title"],
            "artist": result["result"]["artist"]
        }, 200
    
    return {"error": "No match found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
