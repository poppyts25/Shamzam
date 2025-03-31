# code to test user story 4 on the shamzam.py microservice
# User Story 4: As a user, I want to convert a music fragment to a music track in the catalogue, so that I can listen to it.

import unittest
import requests
import os
from unittest.mock import patch
from shamzam import app

API_URL = "http://127.0.0.1:5000/recognize"  # Flask app URL

class Testing(unittest.TestCase):
    ###########################################################
    ## Test [1]     Recognize Track                          ##
    ###########################################################
    def test1(self):
        file_path = "wavs\\~Blinding Lights.wav"
        title = "Blinding Lights"
        artist = "The Weeknd"

        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(API_URL, files=files)
        
        result = response.json()
        
        # Check if request was successful
        self.assertEqual(response.status_code, 200)
        self.assertIn("title", result)
        self.assertIn("artist", result)
        self.assertEqual(result["title"], title)
        self.assertEqual(result["artist"], artist)
        print(result)

    ###########################################################
    ## Test [2]     Recognise track not in database          ##
    ###########################################################
    def test2(self):
        file_path = "wavs\\~Davos.wav"

        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(API_URL, files=files)
        
        result = response.json()
        
        # Check if request was unsuccessful
        self.assertEqual(response.status_code, 404)
       
    ###########################################################
    ## Test [3]    Incorrect API URL                         ##
    ###########################################################
    def test3(self):
        # Simulate a valid file upload request
        file_path = "wavs\\~Blinding Lights.wav"
        title = "Blinding Lights"
        artist = "The Weeknd"

        API_URL_TEST = "http://127.0.0.1:5000"  # Invalid URL

        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(API_URL_TEST, files=files)

        # Check if page not found
        self.assertEqual(response.status_code, 404)

    ###########################################################
    ## Test [4]     Invalid File Path/ No file sent          ##
    ###########################################################
    def test4(self):
        file_path = "wavs\\~Invalid.wav"
        if not os.path.exists(file_path):
            with self.assertRaises(FileNotFoundError):
                with open(file_path, "rb") as f:
                    files = {"file": f}
                    requests.post(API_URL, files=files)
        
        file_path = None
        with self.assertRaises(TypeError):
            with open(file_path, "rb") as f:
                files = {"file": f}
                requests.post(API_URL, files=files)
        

