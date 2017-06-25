import fresh_tomatoes
import media


# Names of movies and contains the information to be used for each movie
dodgeball = media.Movie(
    "Dodgeball",
    "A true underdog story",
    "http://static.rogerebert.com/uploads/movie/movie_poster/"
    "dodgeball-a-true-underdog-story-2004/"
    "large_iYrYVlNOZdPAWL7GXRCLMwxA9yG.jpg",  # noqa
    "https://www.youtube.com/watch?v=W-XbDZUnUmw")

# print(dodgeball.storyline)

dumb_and_dumber = media.Movie(
    "Dumb and Dumber",
    "Two friends who try to return someone's property, "
    "but find themselves in a sticky situation",
    "http://t0.gstatic.com/images?q=tbn:"
    "ANd9GcRfKxcLRaftGDJ-q6WataYprMWOROBAhNPxuqjCUL8vaCA6ZaW1",  # noqa
    "https://www.youtube.com/watch?v=l13yPhimE3o")
# print(dumb_and_dumber.storyline)
# dumb_and_dumber.show_trailer()

black_hawk_down = media.Movie(
    "Black Hawk Down",
    "Based on the true story of a war waged in Mogadishu "
    "by the high tech Black Hawk helicopters "
    "and the US Army Rangers and Deltas",
    "https://upload.wikimedia.org/wikipedia/"
    "en/0/0c/Black_hawk_down_ver1.jpg",  # noqa
    "https://www.youtube.com/watch?v=tnV6wM-vd9s")

hangover = media.Movie(
    "The Hangover",
    "Three buddies wake up from a bachelor party in Las Vegas, "
    "with no memory of the previous night and the bachelor is missing",
    "https://upload.wikimedia.org/wikipedia/en/"
    "b/b9/Hangoverposter09.jpg",  # noqa
    "https://www.youtube.com/watch?v=tcdUhdOlz9M")

waterboy = media.Movie(
    "The Waterboy",
    "A waterboy for a college football team discovers he has a unique "
    "tackling ability and becomes a member of the team",
    "http://games.lukky.us/wp-content/uploads/"
    "imdbcache/tt0120484.jpg",  # noqa
    "https://www.youtube.com/watch?v=z8yv9eq5s14")

step_brothers = media.Movie(
    "Step Brothers",
    "Two aimless middle-aged losers still living at home are forced "
    "against their will to become roommates when their parents marry",
    "https://upload.wikimedia.org/wikipedia/en/d/"
    "d9/StepbrothersMP08.jpg",  # noqa
    "https://www.youtube.com/watch?v=CewglxElBK0")

# Defines what is inside movies
movies = [dodgeball, dumb_and_dumber, black_hawk_down,
          hangover, waterboy, step_brothers]

# Uses the fresh_tomatoes files to pull the movies and then open them in a
# webpage
fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
