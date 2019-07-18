# Supporting Shellfish App

This is the team project for studying the functionalities of cloud computing!

## Short Description
In this project, a cloud-based service will be implemented,
using IBM Visual Recognition API. <br>
The objective is, to create a web application which provides funny supporting hints, 
by recognizing the mood due to the facial expression of the user. <br>

We are using:
- Cloud Service:        Visual Recognition API
- Frontend:             Javascript
- Backend:              Python / Flask
- DB for Training:      MUG Facial Expression

### Docker Image
For creating the Docker Images, please run the above docker-compose.yml file. <br>

```shell
    docker-compose build
```

After the Images have been created, please do the following steps...

#### Supporting Shellfish Backend
For running the backend python flask server, please run the 
following command:
__Without Docker__:
````shell
    python app.py
````

__With Docker__:
```shell
    docker run -p 5000:5000 supporting_shellfish_backend
```

Finally open [http://0.0.0.0:5000](http://0.0.0.0:5000) in your browser to get a sight into the possible operations.<br>


#### more is yet to come...
