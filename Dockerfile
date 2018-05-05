FROM alexellis2/python-gpio-flask:v6
ADD ./app.py ./app.py
ADD ./led2.py ./led2.py

EXPOSE 5000

CMD ["python", "app.py"]
