# README

1. [Screenshots](#Screenshots)

## [Highlights & Tasks](#Highlights)

- [x] Create a repo and store your program on GitHub or Bitbucket.
- [x] Documentation.
- [x] Add a simple UI to this web application.
- [x] Dockerize the application.
- [x] Add a GitHub actions or equivalent pipeline to build a docker container.
- [x] Create a bash script with instructions to run the container.
- [x] Create Kubernetes manifest files to host the web server.
- [x] BONUS: Dockerhub image is available for both arm64 and amd64 architectures(used github actions), making it more universal.
- [x] BONUS: deployed frontend on cloud using streamlit sharing. (https://rapidfort.streamlit.app/)
- [ ] BONUS: Tried to deployed backend on Azure using student credits ($100) but requires premium suite due to high memory requirements. (16 GB RAM, 4 CPU cores)
- [x] BONUS: Maintained high standards of code quality: using enviroment variables and saved coding time by using open-sourced templates.
- [x] PERSONAL ACHIEVEMENT: boosted testing time by downloading model once locally and then transfering it to container using, thus avoiding downloading it everytime the container is run: (expected time reduced from 50 minutes to 5-7 minutes)

```
docker cp ~/.cache/huggingface <container_id>:/root/.cache/
```

- [x] PERSONAL ACHIEVEMENT: never worked on docker, kubernetes or github actions before, so it was a great learning experience.

- Quick Links:
  - hosted frontend: https://rapidfort.streamlit.app/
  - dockerhub image: `ankitsharma61016/gitagpt108:latest`
  - Collab backend link: https://colab.research.google.com/drive/1XQ36LZJ_znkBaqkhHWivyYWbYpFdkxcG?usp=sharing
  - resume link: https://drive.google.com/file/d/1IQRxkd0824bWJVbNHF-_HWwhrofTR3hB/view?usp=drive_link

### [Installation](#installation)

- Run `run.sh` using following command:

```bash
./run.sh
```

if you get permission denied error, run the following command and try again:

```bash
chmod +x run.sh
```

- in background the script will do the following things:

  - Check if container with the specified name is already running. if yes, it will exit the script.
  - Check if the container exists but is stopped, it removes the container.
  - Pull the latest image from the repository
  - Run the Docker container with port mapping
  - Check if the container started successfully, and echo the result.
  - [CAUTION] you can change some parameters in `run.sh` but be very careful while doing so.

- to run frontend locally, run the following command, then go to `localhost:8502` in your browser:

```bash
streamlit run frontend.py --server.port 8502
```

- hosted frontend on cloud using streamlit sharing, link is given below:

```bash
https://rapidfort.streamlit.app/
```

- [CAUTION] remember the llama2 model is very intensive and requires a lot of memory(13GB+). so, if you are running it on a local machine, it might crash. so, it is recommended to run it on a cloud instance, through google colab. the link to the colab notebook is given below, doing same thing as in `backend.py` but in cloud(without frontend):
  follow this article to generate HF_TOKEN: https://huggingface.co/blog/llama2

```bash
https://colab.research.google.com/drive/1XQ36LZJ_znkBaqkhHWivyYWbYpFdkxcG?usp=sharing
```

### Kubernetes

- to create kubernetes cluster, run the following command:

```bash
kubectl create -f pod.yaml
```

- to check if the pod is running, run the following command:

```bash
kubectl get deployments
```

- to tear down the cluster, run the following command:

```bash
kubectl delete -f pod.yaml
```
