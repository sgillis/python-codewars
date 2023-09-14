class User(object):
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def rank_diff(self, rank):
        if rank > 0 and self.rank < 0:
            return rank - self.rank - 1
        elif rank < 0 and self.rank > 0:
            return rank - self.rank + 1
        else:
            return rank - self.rank

    def inc_progress(self, rank):
        if rank > 8 or rank < -8 or rank == 0:
            raise
        if self.rank == 8:
            return
        diff = self.rank_diff(rank)
        if diff == -1:
            additional_progress = 1
        elif diff == 0:
            additional_progress = 3
        elif diff < -1:
            additional_progress = 0
        else:
            additional_progress = 10 * diff * diff
        self.progress += additional_progress
        while self.progress >= 100:
            self.progress = self.progress - 100
            if self.rank == -1:
                self.rank = 1
            elif self.rank == 7:
                self.rank = 8
                self.progress = 0
            else:
                self.rank += 1
