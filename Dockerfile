FROM resin/rpi-raspbian

RUN apt-get update && apt-get install -y \
	python \
	python2.7-dev \
	python-pip \
	python-dev \
	gcc \
	libraspberrypi0 libraspberrypi-dev libraspberrypi-doc libraspberrypi-bin \
	mpd mpc

ADD ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

ADD ./app.py ./app.py
ADD ./led2.py ./led2.py
ADD ./temp2.py ./temp2.py
ADD ./music/m1.mp3 /var/lib/mpd/music/m1.mp3
#ADD ./lib/4.14.34+/* /lib/modules/4.14.34+/

ENTRYPOINT service mpd restart && mpc add http://centova.radios.pt:8401/stream.mp3/1 && /bin/bash

EXPOSE 5000

#CMD ["python", "app.py"]

#Run it:

#docker run -ti --privileged -p 5000:5000 --rm -v /dev/snd:/dev/snd filiperfernandes/ai-domotics:v2
