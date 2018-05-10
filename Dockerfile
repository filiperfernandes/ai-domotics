FROM alexellis2/python-gpio-flask:v6
ADD ./app.py ./app.py
ADD ./led2.py ./led2.py

RUN sudo apt-get install -yq vlc
EXPOSE 5000

CMD ["python", "app.py"]
