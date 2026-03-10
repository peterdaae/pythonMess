import logging
import statistics
logging.basicConfig(level=logging.DEBUG)

class Exercise3:
    path = "Lecture6/numbers.txt"
    out_path = "Lecture6/report.txt"

    def read_numbers(self):
        nums =[]
        try:
            with open(self.path, "r") as infile:
                for line in infile:
                    s = line.strip()
                    if not s:
                        continue
                    nums.append(int(s))

        except FileNotFoundError:
            print("File not found")
        return nums

    def write_report(self, numbers):
        if not numbers:
            print("no numbers in file")
            return

        with open(self.out_path, "w") as outfile:
            outfile.write("count    : " + str(len(numbers)) + "\n")
            outfile.write("min      : " + str(min(numbers)) + "\n")
            outfile.write("max      : " + str(max(numbers)) + "\n")
            outfile.write("mean     : " + str(statistics.mean(numbers)) + "\n")

    def run(self):
        nums = self.read_numbers()
        self.write_report(nums)
        try:
            with open(self.out_path, "r") as r:
                print("Report:")
                print(r.read())
        except FileNotFoundError:
            print("File not found")
