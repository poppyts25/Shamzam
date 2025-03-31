# Microservice one
# Story 1: Add music track to catalogue
# Story 2: Remove music track from catalogue
# Story 3: List music tracks in catalogue

import database
from flask import Flask, request

app  = Flask(__name__)

# Add music track to the database
@app.route("/admin/<string:track>", methods=["PUT"])
def upload_track(track):
    js = request.get_json()
    title = js["title"]
    artist = js["artist"]
    file_path = js["file"]  

    if title is not None and artist is not None and file_path is not None:
        track = {"title":title,"artist":artist,"file":file_path}
        if database.db.lookup(title) != None:
            if database.db.update(js):
                return "",204 # No Content
            else:
                return "",500 # Internal Server Error
        else:
            if database.db.insert(js):
                return "",201 # Created
            else:
                return "",500 # Internal Server Error
    else:
        return "",400 # Bad Request

# Remove music track from the database
@app.route("/admin/<string:track>", methods=["POST"])
def remove_track(track):
    js = request.get_json()
    title = js["title"]
    if title is not None:
        if database.db.lookup(title) != None:
            if database.db.delete(title):
                return "",204 # No Content
            else:
                return "",500 # Internal Server Error
        else:
            return "",404 # Bad Request
    else:
        return "",400 # Bad Request


@app.route("/admin", methods=["GET"])
def list_tracks():
    tracks = database.db.list()
    
    if tracks is None:  # Check if the database query failed
        return "", 500
    else:
        return tracks, 200
if __name__ == "__main__":
  app.run(host="localhost",port=3000, debug=True)
