# Shamzam
Shazam-like MVP called Shamzam using some microservices. Uses AudD.io API requests to recognise wav snippets.

## Setup:

- store music fragments and full tracks in folder called "wavs" in project directory

### Admin.py microservice:
This microservice allows an administrator to manage a music catalogue by adding, removing, and listing music tracks

- run the admin.py microservice in anaconda prompt:
    
    python admin.py

- run the unit tests for user stories 1-3 in a separate anaconda prompt:

    python -m unittest Story_1_Tests.py
    python -m unittest Story_2_Tests.py
    python -m unittest Story_3_Tests.py


### Shamzam.py microservice:
This microservice identifies music tracks from uploaded audio files using the AudD API

- Set environment variable for API key in anaconda prompt.

    set KEY="YOUR API KEY"

- run the shamzam.py microservice in anaconda prompt:

    python shamzam.py

- in a separate anaconda prompt run the unit tests:

    python -m unittest Story_4_Tests.py
