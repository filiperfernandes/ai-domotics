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
$ docker pull filiperfernandes/ai-domotics:v4
```

- Run it:

```
$ docker run -ti --privileged -p 5000:5000 --rm -v /dev/snd:/dev/snd filiperfernandes/ai-domotics:v4
```

## Usage

- LED: ON/OFF/STATE (GET)
```
http://192.168.1.2:5000/on

or

http://192.168.1.2:5000/led?val=0 (0=off/1=on)
```

- Radio: Play/Stop
```
http://192.168.1.2:5000/play_or_stop

or

http://192.168.1.2:5000/toggle?val=0 (0=stop/1=play)
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

- LED: Itensity (GET)
```
http://192.168.1.2:5000/intensity?val=0 (0=off/1=one_led/2=2_leds/3=3_leds)
```

- Temperature Sensor (GET)
```
http://192.168.1.2:5000/temp (return string with temp in ºC)
```


