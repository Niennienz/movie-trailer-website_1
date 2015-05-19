import media
import fresh_tomatoes

# Information of the movie <Toy Story>, stored in a Movie instance.
toy_story = media.Movie(
		"Toy Story",
		"A story of a boy and his toys that come to life.",
		"http://upload.wikimedia.org/wikipedia/"
		"en/1/13/Toy_Story.jpg",
		"https://www.youtube.com/watch?v=KYz2wyBy3kc"
)

# Information of the movie <Avatar>, stored in a Movie instance.
avatar = media.Movie(
		"Avatar",
		"A marine on a alien planet.",
		"http://upload.wikimedia.org/wikipedia/"
		"en/b/b0/Avatar-Teaser-Poster.jpg",
		"https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

# Information of the movie <Man of Steel>, stored in a Movie instance.
man_of_steel = media.Movie(
		"Man of Steel",
		"A very first story of Superman.",
		"http://upload.wikimedia.org/wikipedia/"
		"en/8/85/ManofSteelFinalPoster.jpg",
		"https://www.youtube.com/watch?v=T6DJcgm3wNY"
)

# Information of the movie <Avengers II>, stored in a Movie instance.
avengers_2 = media.Movie(
		"Avengers II: Age of Ultron",
		"Reunion of Avengers and their fight to AI.",
		"http://upload.wikimedia.org/wikipedia/"
		"en/1/1b/Avengers_Age_of_Ultron.jpg",
		"https://www.youtube.com/watch?v=JAUoeqvedMo"
)

# Information of the movie <The Da Vinci Code>, stored in a Movie instance.
davinci_code = media.Movie(
		"The Da Vinci Code",
		"Adventure of a historian.",
		"http://upload.wikimedia.org/wikipedia/"
		"en/e/e9/The_da_vinci_code_final.jpg",
		"https://www.youtube.com/watch?v=zMba3fckhuQ"
)

# Information of the movie <Midnight in Paris>, stored in a Movie instance.
midnight_in_paris = media.Movie(
		"Midnight in Paris",
		"A young man's great love for a city, Paris.",
		"http://upload.wikimedia.org/wikipedia/"
		"en/9/9f/Midnight_in_Paris_Poster.jpg",
		"https://www.youtube.com/watch?v=FAfR8omt-CY"
)

# A list called 'movies' stores all Movie instances created above.
movies = [toy_story, avatar, man_of_steel,
		  avengers_2, davinci_code, midnight_in_paris]

# Use fresh_tomatoes' API to display the page.
fresh_tomatoes.open_movies_page(movies)