from swaglyrics.cli import lyrics
from flask import Flask, render_template
import os
from swaglyrics import spotify

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath('tab.py')), 'templates'))

song = None
artist = None


@app.route('/')
def tab():
	global song, artist
	song = spotify.song()
	artist = spotify.artist()
	current_lyrics = lyrics(song, artist)
	current_lyrics = current_lyrics.split('\n')
	return render_template('lyrics.html', lyrics=current_lyrics, song=song, artist=artist)


@app.route('/songChanged', methods=['GET'])
def song_changed():
	global song
	if song == spotify.song() or spotify.song() is None:
		return 'no'
	return 'yes'


if __name__ == '__main__':
	app.run()
