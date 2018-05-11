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

ENTRYPOINT service mpd restart && mpc add http://radio.nolife-radio.com:9000/stream && python app.py

EXPOSE 5000

#CMD ["python", "app.py"]

#Run it:

#docker run -ti --privileged -p 5000:5000 --rm -v /dev/snd:/dev/snd filiperfernandes/ai-domotics:v2
