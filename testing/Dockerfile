FROM arm32v5/debian

RUN apt-get -yq update
RUN apt-get -yq install python2.7-dev
#RUN apt-get -yq install vlc-nox
RUN apt-get -yq install python-pip
RUN apt-get -yq install python-dev
RUN apt-get -yq install python-pip
RUN apt-get -yq install mpd mpc

RUN /bin/bash -c "mpc add http://radio.nolife-radio.com:9000/stream"

ADD ./app.py ./app.py
ADD ./led2.py ./led2.py
ADD ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["python", "app.py"]

#docker run -ti --privileged -p 5000:5000 --rm -v /dev/snd:/dev/snd filiperfernandes/ai-domotics:v2