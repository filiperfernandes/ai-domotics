#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
#from flask_httpauth import HTTPBasicAuth
from led2 import *
#from temp2 import *
import os, subprocess
from subprocess import Popen, PIPE

app = Flask(__name__, static_url_path = "")

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/test', methods=['GET'])
def test():
	return ("Hello World!")

@app.route('/on', methods=['GET'])
def l_on():
	pin = int(request.args.get('pin'))
	led_on(pin)
	return ("1")

@app.route('/off', methods=['GET'])
def l_off():
	pin = int(request.args.get('pin'))
	led_off(pin)
	return ("0")

@app.route('/led', methods=['GET'])
def l_led():
        val = int(request.args.get('val'))
        if(val==0):
		led_off(18)
		return("0")
	else:
		led_on(18)
        	return ("1")

@app.route('/intensity', methods=['GET'])
def l_int():
        val = int(request.args.get('val'))
        if(val==1):
		led_on(18)
		led_off(17)
		led_off(27)
		return ("1")
	elif(val==2):
		led_on(18)
		led_on(17)
		led_off(27)
		return ("2")
	elif(val==3):
		led_on(18)
		led_on(17)
		led_on(27)
		return ("3")
	else:
		led_off(18)
		led_off(17)
		led_off(27)
        	return ("0")

@app.route('/morse', methods=['GET'])
def morse():
	text=request.args.get('text')
	talk(text)
	return ("Morse")

@app.route('/state', methods=['GET'])
def l_state():
	pin = request.args.get('pin')
        return (state(pin))

@app.route('/tts', methods=['GET', 'POST'])
def tts():
	content = request.get_json(silent=True)
	print (content)
	text=content['text']
	text = text.replace(" ", "_")
	os.system("espeak " + text)
	output="Saying: " + text
	return (output)

@app.route('/streamyt', methods=['GET', 'POST'])
def streamyt():
	content = request.get_json(silent=True)
	print (content)
	url=content['url']
	os.system('mpv --no-video "$(yturl ' + url + ')"')
	return ("Playing...")

@app.route('/play', methods=['GET', 'POST'])
def play():
	mpcCommand(['mpc', 'play'])
	return ("1")

@app.route('/stop', methods=['GET', 'POST'])
def stop():
	mpcCommand(['mpc', 'stop'])
	return ("0")

@app.route('/toggle', methods=['GET', 'POST'])
def toggle():
	val = int(request.args.get('val'))
        if(val==0):
		mpcCommand(['mpc', 'stop'])
        	return ("0")
	else:
		mpcCommand(['mpc', 'clear'])
		mpcCommand(['mpc', 'add', 'http://centova.radios.pt:8401/stream.mp3/1'])
		mpcCommand(['mpc', 'play'])
        	return ("1")

@app.route('/volup', methods=['GET', 'POST'])
def volup():
        mpcCommand(['mpc', 'volume', '+10'])
        return ("Volume +10")

@app.route('/voldown', methods=['GET', 'POST'])
def voldown():
        mpcCommand(['mpc', 'volume', '-10'])
        return ("Volume -10")

@app.route('/volume', methods=['GET', 'POST'])
def volume():
	val = request.args.get('val')
        mpcCommand(['mpc', 'volume', val])
        return (val)

@app.route('/radio', methods=['GET', 'POST'])
def chRadio():
	content = request.get_json(silent=True)
	url=content['url']
	mpcCommand(['mpc', 'clear'])
        mpcCommand(['mpc', 'add', url])
        return ("1")

@app.route('/temp', methods=['GET', 'POST'])
def temp():
	temp = str(read_temp())
        return (temp)

@app.route('/current', methods=['GET', 'POST'])
def current():
        song = mpcCommand(['mpc', 'current'])
	return (song)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')

