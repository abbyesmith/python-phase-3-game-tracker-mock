from .result import Result

class Game:
    def __init__(self, title):
        self.title = title
        
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if (not hasattr(self, "_title")) and isinstance(title, str) and len(title) > 0:
            self._title = title

    title = property(get_title, set_title)

    def results(self):
        return [result for result in Result.all if result.game ==self]
    
    def players(self):
        return [result.player for result in self.results()]
    
    def game_results_for_player(self, player):
        return [result for result in self.results() if result.player == player]
    
    def average_score(self, player):
        num_results = len(self.game_results_for_player(player))
        sum_results = sum(
            [result.score for result in self.game_results_for_player(player)]
        )
        return sum_results / num_results


#### Game

# - `Game __init__(self, title)`
#   - `Game` is initialized with a title (string)
#   - Title **cannot be** changed after the `Game` is initialized
# - `Game property title`
#   - Returns the `Game`'s title
#   - Titles must be strings greater than 0 characters
#   - if you are using exceptions comment out the test on lines 25 - 32 in the game_test.py and uncomment lines 34 - 38