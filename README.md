# ai-domotics

### Prerequisites

- Working raspberry pi
- Install Docker on raspberry pi:

```
$ curl -sSL https://get.docker.com | sh
```

- Start docker:

```
$ sudo systemctl start docker
```

- Add your user (pi) to docker group
```
$ sudo usermod -aG docker pi
```


## Usage

- Clone this repo
- Build Dockerfile ou pull it from remote docker repo:

```
$ docker build -t ai-domotics .
or
$ docker pull filiperfernandes/ai-domotics:v1
```

- Run it:

```
$ docker run -ti --privileged -p 5000:5000 filiperfernandes/ai-domotics:v1
```

### Music Streaming

```
docker pull aaaler/vlc-nox-pi
docker run -ti  --privileged -d aaaler/vlc-nox-pi
``

