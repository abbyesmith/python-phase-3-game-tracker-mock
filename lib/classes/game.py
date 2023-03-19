from classes.result import Result

class Game:
    def __init__(self, title):
        self.title = title
        
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if (not hasattr(self, "_title")) and isinstance(title, str) and len(title) > 0:
            self._title = title

    title = property(get_title, set_title)

