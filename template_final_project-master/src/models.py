class GameModel:
    def __init__(self):
        self.score = 0
        self.timer = 30
        self.high_score = self.load_high_score()

    @staticmethod
    def load_high_score():
        try:
            with open("etc/high_scores.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("etc/high_scores.txt", "w") as file:
            file.write(str(self.high_score))

