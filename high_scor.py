class HighScore:
    def __init__(self):
        self.high_score = self.load_high_score()

    def load_high_score(self):
        try:
            with open("high_score.txt","r") as f:
                return int(f.read().strip())
        except FileNotFoundError:
            with open("high_score.txt", "w") as f:
                f.write("0")
            return 0

    def save_high_score(self, score):
        with open("high_score.txt","w") as f:
            f.write(str(score))

    def update_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            self.save_high_score(score)