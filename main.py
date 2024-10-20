import random
import time
import threading
from durakonline import durakonline
from datetime import datetime

FILE_DIRECTORY = "accounts.txt"
DEBUG_MODE: bool = False

class Bonus:

    games: int = 0
    accounts: [] = []

    def __init__(self):
        self.pages = [
            self.from_file,
        ]
        print("Код запущен")

    def start(self):
        page_type = 1
        self.pages[page_type-1]()

    def from_file(self):

        file = open(FILE_DIRECTORY, "r")
        accounts = file.read().split("\n")
        file.close()

        for token in accounts:
            self.bonusW(token)
            
    def bonusW(self, token: str):
        bot = durakonline.Client(token, server_id="u5", tag="[BOT]", debug=DEBUG_MODE)
        bot.buy_points()
        self.log(f"Бонус получил - {bot.uid}")
                          
    def log(self, message: str, tag: str = "MAIN") -> None:
        print(f">> [{tag}] [{datetime.now().strftime('%H:%M:%S')}] {message}")


if __name__ == "__main__":
    Bonus().start()