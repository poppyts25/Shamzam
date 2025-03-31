# Code to test user story 1 in the admin.py microservice
# User Story 1: As an administrator, I want to add a music track to the catalogue, so that a user can listen to it.

import requests
import unittest
import database 

admin = "http://localhost:3000/admin"

class Testing(unittest.TestCase):
    ###########################################################
    ## Test [1]     Add track to empty catalogue             ##
    ###########################################################
    def test1(self):
        database.db.clear()
        title = "Blinding Lights"
        artist = "The Weeknd"
        file_path = "wavs\\Blinding Lights.wav"

        hdrs = {"Content-Type":"application/json"}
        js   = {"title":title,"artist":artist,"file":file_path}
        rsp  = requests.put(f'{admin}/{title}',headers=hdrs,
                json=js)

        self.assertEqual(rsp.status_code,201)
    
    ###########################################################
    ## Test [2]     Add another track to catalogue           ##
    ###########################################################
    def test2(self):
        title = "Don't Look Back In Anger"
        artist = "Oasis"
        file_path = "wavs\\Don't Look Back In Anger.wav"

        hdrs = {"Content-Type":"application/json"}
        js   = {"title":title,"artist":artist,"file":file_path}
        rsp  = requests.put(f'{admin}/{title}',headers=hdrs,
                json=js)

        self.assertEqual(rsp.status_code,201)

    ###########################################################
    ## Test [3]    Add track that is in catalogue already    ##
    ###########################################################
    def test3(self):
        title = "Blinding Lights"
        artist = "The Weeknd"
        file_path = "wavs\\Blinding Lights.wav"

        hdrs = {"Content-Type":"application/json"}
        js   = {"title":title,"artist":artist,"file":file_path}
        rsp  = requests.put(f'{admin}/{title}',headers=hdrs,
                json=js)

        title = "Blinding Lights"
        artist = "The Weeknd"
        file_path = "wavs\\Blinding Lights.wav"

        hdrs = {"Content-Type":"application/json"}
        js   = {"title":title,"artist":artist,"file":file_path}
        rsp  = requests.put(f'{admin}/{title}',headers=hdrs,
                json=js)

        self.assertEqual(rsp.status_code,204)


    ###########################################################
    ## Test [4]    Add track with missing artist             ##
    ###########################################################
    def test4(self):
        title = "Blinding Lights"
        artist = None
        file_path = "wavs\\Blinding Lights.wav"

        hdrs = {"Content-Type":"application/json"}
        js   = {"title":title, "artist":artist,"file":file_path}
        rsp  = requests.put(f'{admin}/{title}',headers=hdrs,
                json=js)

        self.assertEqual(rsp.status_code,400)