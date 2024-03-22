
class PlayerScore:
    """Stores a player identity (name) and a score."""

    def __init__(self, player, score):
        self.player = player
        self.score = score


class TopScores:
    """Stores up to max_size PlayerScores in descending order by score."""

    def __init__(self, max_size=5):
        self._max_size = max_size
        self._data = list()

    def add(self, player, score):
        i = len(self._data)
        while i > 0 and score > self._data[i-1].score:
            i = i - 1
        if len(self._data) < self._max_size or i < len(self._data):
            self._data.insert(i, PlayerScore(player, score) )
            if len(self._data) > self._max_size:
                self._data.pop()

    def __len__(self):
        """Return the number of scores."""
        return len(self._data)

    def get_player(self, index):
        return self._data[index].player
    
    def get_score( self, index):
        return self._data[index].score
    




