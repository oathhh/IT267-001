from movie_protected import Movie

class Documentaray(Movie):
    def __init__(self) -> None:
        super().__init__()
        self.channel = None #public attribute

    def add_channel(self,channel:str):
        self.channel = channel