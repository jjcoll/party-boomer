from flask import render_template, request, redirect, url_for, jsonify
from app import app
from app.selenium_script import create_caos
from threading import Thread

song_name = 'nothing'
app_playing = False
url = ''
given_likes = 0;
total_likes = 0;

@app.route('/', methods=['GET', 'POST'])
def index():
  global song_name
  global total_likes
  global url
  if request.method == 'POST':
    url = request.form.get('url')
    song_name = request.form.get('song-name')
    total_likes = int(request.form.get('n-likes'))

    return redirect(url_for('playing'))
  return render_template("index.html")

@app.route('/playing', methods=['GET', 'POST'])
def playing():
  global given_likes
  global total_likes
  global app_playing
  print(app_playing)
  if app_playing == False:
    app_playing = True;
    print(app_playing)
    play_thread = Thread(target=play)
    play_thread.start()
    return render_template('playing.html')
  return render_template('test.html')


@app.route('/test', methods=['GET'])
def test():
  return render_template('test.html')


@app.route('/get_playing_stats', methods=['GET'])
def update_playing():
    return jsonify({'song_name': song_name, 'total_likes': total_likes, 'given_likes': given_likes })

def play():
  global given_likes
  global app_playing
  global total_likes
  for i in range(total_likes):
    print('doing something')
    create_caos(url, song_name)
    given_likes = i + 1
  app_playing = False

  given_likes = 0
  total_likes = 0
  print('finished')
  return
