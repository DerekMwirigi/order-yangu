### 1. Environment setting up

#### 1.1
```
Locally start firestore emulator in detach mode.
To be avle to easily start debuging/setting up the codebase and work easily, I have packaged docker container yml files to setip google firestore emulator
inside services/<service_name>/docker/firestore/ there is the Docker file to start up a container on the machine to server google firestore emulator
docker compose -f docker-stacks/docker-firestore.yml up d
```
