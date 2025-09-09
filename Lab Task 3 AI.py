class AC_Agent:
    def __init__ (self, set_temp):
        self.set_temp = set_temp
        self.last_move = None

    def check(self, temp):
        if temp > self.set_temp:
            move = "AC is ON"
        else:
            move = "AC is OFF"

        if move == self.last_move:
            move = print(f"No change, keep {self.last_move}")

        if "No change" not in move:
            self.last_move = move



areas = {
    "Study Room": 27,
    "Meeting Room": 22,
    "Dining Hall": 25,
    "Garage": 20
}

set_temp = 24
bot = AC_Agent(set_temp)


for place, temp in areas.items():
    result = bot.check(temp)
    print(f"{place}: {temp}°C  is   {result}")



