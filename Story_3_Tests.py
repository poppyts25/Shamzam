# code to test User Story 3 in the admin.py microservice
# User Story 3: As an administrator, I want to list the names of the music tracks in the catalogue, so that I know what it contains

import requests
import unittest
import database 
from unittest.mock import patch


admin = "http://localhost:3000/admin"

class Testing(unittest.TestCase):
    #######################################################
    ## Test [1]     List tracks in database              ##
    #######################################################
    def test1(self):
        database.db.clear()
        title = "Blinding Lights"
        artist = "The Weeknd"
        file_path = "wavs\\Blinding Lights.wav"

        hdrs = {"Content-Type":"application/json"}
        js   = {"title":title,"artist":artist,"file":file_path}
        rsp  = requests.put(f'{admin}/{title}',headers=hdrs,
                json=js)

        title = "Don't Look Back In Anger"
        artist = "Oasis"
        file_path = "wavs\\Don't Look Back In Anger.wav"

        hdrs = {"Content-Type":"application/json"}
        js   = {"title":title,"artist":artist,"file":file_path}
        rsp  = requests.put(f'{admin}/{title}',headers=hdrs,
                json=js)

        hdrs = {"Content-Type":"application/json"}
        rsp  = requests.get(f'{admin}',headers=hdrs)

        print(rsp.text)
        self.assertEqual(rsp.status_code,200)
    
    #######################################################
    ## Test [2]     List tracks in empty database        ##
    #######################################################
    def test2(self):
        database.db.clear()
        hdrs = {"Content-Type":"application/json"}
        rsp  = requests.get(f'{admin}',headers=hdrs)

        self.assertEqual(rsp.status_code,200)
        self.assertEqual(rsp.json(),[])
