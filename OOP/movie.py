class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def movie_info(self):
        print(self.title, self.director, self.year)


m = Movie("Inception", "Christopher Nolan", 2010)
m.movie_info()