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


## Get it up and running

- Clone this repo
- Build Dockerfile ou pull it from remote docker repo:

```
$ docker build -t ai-domotics .
or
$ docker pull filiperfernandes/ai-domotics:v2
```

- Run it:

```
$ docker run -ti --privileged -p 5000:5000 --rm -v /dev/snd:/dev/snd filiperfernandes/ai-domotics:v2
```

## Usage

- LED: ON/OFF/STATE (GET)
```
http://192.168.1.2:5000/on
```

- Radio: Play/Stop
```
http://192.168.1.2:5000/play_or_stop
```

- Radio add stream
```
URL:

http://192.168.1.2:5000/radio

Body:

{
    "url": "http://centova.radios.pt:8401/stream.mp3/1"
}

```

