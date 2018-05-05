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
$ docker run -ti --privileged -p 5000:5000 ai_domotics
```

