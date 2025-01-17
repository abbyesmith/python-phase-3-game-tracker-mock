class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.add_result_to_all(self)
    
    @classmethod
    def add_result_to_all(cls, result):
        cls.all.append(result)
    
    def get_score(self):
        return self._score

    def set_score(self,score):
        if isinstance(score, int) and 1<= score <= 5000:
            self._score = score
        else:
            raise Exception("Score out of range") 
    
    score = property(get_score, set_score)

    def get_player(self):
        return self._player
    
    def set_player(self, player):
        from .player import Player
        if isinstance(player, Player):
            self._player = player
    
    player = property(get_player, set_player)

    def get_game(self):
        return self._game
    
    def set_game(self, game):
        from .game import Game
        if isinstance(game, Game):
            self._game = game
    
    game = property(get_game, set_game)



        
#### Result

# - `Result __init__(self, player, game, score)`
#   - `Result` is initialized with a `Player` instance, a `Game` instance, and a
#     score (number)
# - `Result property score`
#   - Returns the score for the `Result` instance
#   - Scores must be integers between 1 and 5000, inclusive