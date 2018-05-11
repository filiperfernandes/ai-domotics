#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
#from flask_httpauth import HTTPBasicAuth
from led2 import *
import os, subprocess

app = Flask(__name__, static_url_path = "")
    
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]
    
@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    return jsonify( { 'tasks': tasks } )

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify( { 'task': task[0] } )

@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify( { 'task': task } ), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

@app.route('/test', methods=['GET'])
def test():
	a=5
	b=7
	return ("Hello World!" + str(a*b))

@app.route('/on', methods=['GET'])
def l_on():
	led_on()
	return ("Led on")

@app.route('/off', methods=['GET'])
def l_off():
	led_off()
	return ("Led off")

@app.route('/morse', methods=['GET'])
def morse():
	text=request.args.get('text')
	talk(text)
	return ("Morse")

@app.route('/state', methods=['GET'])
def l_state():
        return (state("18"))

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
# content = request.get_json(silent=True)
# print (content)
# music=content['music']
# os.system("runuser -l  vlc -c 'vlc --no-video /root/music/m1.mp3'")
#	cmd=['mpc', 'play']
#	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
	mpcCommand(['mpc', 'play'])
	return ("Playing...")


@app.route('/stop', methods=['GET', 'POST'])
def stop():
#	cmd=['mpc', 'stop']
#	p  = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#	return ("Stopped")
	mpcCommand(['mpc', 'stop'])
	return ("Stopped")

@app.route('/volup', methods=['GET', 'POST'])
def volup():
        mpcCommand(['mpc', 'volume', '+10'])
        return ("Volume +10")

@app.route('/voldown', methods=['GET', 'POST'])
def voldown():
        mpcCommand(['mpc', 'volume', '-10'])
        return ("Volume -10")

@app.route('/radio', methods=['GET', 'POST'])
def chRadio():
	content = request.get_json(silent=True)
	url=content['url']
	mpcCommand(['mpc', 'clear'])
        mpcCommand(['mpc', 'add', url])
        return ("Volume -10")

#mpv --no-video "$(yturl https://www.youtube.com/watch?v=N73sDPuxKQI&list=RDN73sDPuxKQI)"    
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')

