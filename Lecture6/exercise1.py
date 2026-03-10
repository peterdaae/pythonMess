class Exercise1:
    def read_write(self):

        counts = dict.fromkeys(["ERROR", "DEBUG", "INFO", "WARNING"], 0)
        badline = 0

        with open("Lecture6/server.log", "r") as infile:
            for line in  infile:
                string = line.strip()

                if not string:
                    continue

                try:
                    date, level, msg = string.split(maxsplit=2)
                    level = level.upper()
                    if level not in counts:
                        raise ValueError("Unknown level")
                    counts[level] += 1

                except Exception:
                    badline += 1

        with open("Lecture6/summary.txt", "w") as outfile:
            for level in ["ERROR", "DEBUG", "INFO", "WARNING"]:
                outfile.write(f"{level}: {counts[level]}\n")


            outfile.write(f"badline: {badline}\n")

        with open("Lecture6/summary.txt", "r") as new_infile:
            print(new_infile.read())