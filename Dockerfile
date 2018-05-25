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

#RUN apt-get update && apt-get install -y --reinstall raspberrypi-bootloader raspberrypi-kernel

#RUN apt-get update && apt-get install -y libraspberrypi0 libraspberrypi-dev libraspberrypi-doc libraspberrypi-bin

ADD ./app.py ./app.py
ADD ./led2.py ./led2.py
#ADD ./temp2.py ./temp2.py
ADD ./music/m1.mp3 /var/lib/mpd/music/m1.mp3

ENTRYPOINT service mpd restart && mpc add http://centova.radios.pt:8401/stream.mp3/1 && python app.py
#ENTRYPOINT mv /lib/modules/4.9.35+ /lib/modules/4.14.34+  && python app.py

EXPOSE 5000

#CMD ["python", "app.py"]

#Run it:

#docker run -ti --privileged -p 5000:5000 --rm -v /dev/snd:/dev/snd filiperfernandes/ai-domotics:v4
