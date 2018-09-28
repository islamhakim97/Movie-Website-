import webbrowser
class Movie():
    def __init__(self,movie_title,movie_story,poster_image,movie_trailer):
        self.title=movie_title
        self.story=movie_story
        self.poster_image_url = poster_image
        self.trailer_youtube_url=movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)

