import webbrowser

""" This class provides a way to store movie related information. """
class Movie():
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	# Constructor take four parameters excluding self: movie title, storyline, poster image URL and YouTube trailer URL.
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		
	# Function that shows the YouTube trailer of a movie.
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)