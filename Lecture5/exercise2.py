from random import randint

class Exercise2:
    def dice_rolls(self):
        return randint(1, 6) + randint(1, 6)

    def main_program(self):
        rolls = 1000
        dice_counter = {i: 0 for i in range(2, 13)}

        for _ in range(rolls):
            roll = self.dice_rolls()
            dice_counter[roll] += 1

        for total in range(2, 13):
            pct = dice_counter[total] / rolls * 100
            print(f"Total: {total:<10} Percentage: {pct:.2f}%")







