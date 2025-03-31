# code to test user story 2 in admin.py microservice
# User Story 2: As an administrator, I want to remove a music track from the catalogue, so that a user cannot listen to it.

import requests
import unittest
import database 

admin = "http://localhost:3000/admin"

class Testing(unittest.TestCase):
    #######################################################
    ## Test [1]     Remove track from database           ##
    #######################################################
    def test1(self):
        # reset database
        database.db.clear()

        # Add a track
        title = "Blinding Lights"
        artist = "The Weeknd"
        file_path = "wavs\\Blinding Lights.wav"

        hdrs = {"Content-Type":"application/json"}
        js   = {"title":title,"artist":artist,"file":file_path}
        rsp  = requests.put(f'{admin}/{title}',headers=hdrs,
                json=js)

        # Check if track was added
        self.assertEqual(rsp.status_code,201)

        # Check database is not empty
        rsp  = requests.get(f'{admin}',headers=hdrs)
        self.assertEqual(rsp.status_code,200)
        self.assertEqual(len(rsp.json()),1)

        # Remove the track
        js   = {"title":title}
        rsp  = requests.post(f'{admin}/{title}',headers=hdrs,
                json=js)

        self.assertEqual(rsp.status_code,204)

        # check database is now empty
        rsp  = requests.get(f'{admin}',headers=hdrs)
        self.assertEqual(rsp.status_code,200)
        self.assertEqual(rsp.json(),[])

    #######################################################
    ## Test [2]     Remove track not in database         ##
    #######################################################
    def test2(self):
        # reset database
        database.db.clear()

        # Add a track
        title = "Blinding Lights"
        artist = "The Weeknd"
        file_path = "wavs\\Blinding Lights.wav"

        hdrs = {"Content-Type":"application/json"}
        js   = {"title":title,"artist":artist,"file":file_path}
        rsp  = requests.put(f'{admin}/{title}',headers=hdrs,
                json=js)

        # Check if track was added
        self.assertEqual(rsp.status_code,201)

        # Check database is not empty
        rsp  = requests.get(f'{admin}',headers=hdrs)
        self.assertEqual(rsp.status_code,200)
        self.assertEqual(len(rsp.json()),1)

        # Remove a track not in the database
        title = "Don't Look Back In Anger"
        artist = "Oasis"
        file_path = "wavs\\Don't Look Back In Anger.wav"

        js   = {"title":title}
        rsp  = requests.post(f'{admin}/{title}',headers=hdrs,
                json=js)

        self.assertEqual(rsp.status_code,404)

        # check database is not empty
        rsp  = requests.get(f'{admin}',headers=hdrs)
        self.assertEqual(rsp.status_code,200)
        self.assertEqual(len(rsp.json()),1)

    #######################################################
    ## Test [3]     Remove track with missing title      ##
    #######################################################
    def test3(self):
        # reset database
        database.db.clear()

        # Add a track
        title = "Blinding Lights"
        artist = "The Weeknd"
        file_path = "wavs\\Blinding Lights.wav"

        hdrs = {"Content-Type":"application/json"}
        js   = {"title":title,"artist":artist,"file":file_path}
        rsp  = requests.put(f'{admin}/{title}',headers=hdrs,
                json=js)

        # Check if track was added
        self.assertEqual(rsp.status_code,201)

        # Check database is not empty
        rsp  = requests.get(f'{admin}',headers=hdrs)
        self.assertEqual(rsp.status_code,200)
        self.assertEqual(len(rsp.json()),1)

        # Remove a track with missing title
        title = None
        artist = "The Weeknd"
        file_path = "wavs\\Don't Look Back In Anger.wav"

        js   = {"title":title}
        rsp  = requests.post(f'{admin}/{title}',headers=hdrs,
                json=js)

        self.assertEqual(rsp.status_code,400)

        # check database is not empty
        rsp  = requests.get(f'{admin}',headers=hdrs)
        self.assertEqual(rsp.status_code,200)
        self.assertEqual(len(rsp.json()),1)