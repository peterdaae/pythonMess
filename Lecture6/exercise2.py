class Exercise2:
    def csv_cleaner(self):
        users = "Lecture6/users.csv"
        users_errors = "Lecture6/users_errors.txt"
        users_clean = "Lecture6/users_clean.csv"

        try:

            with open(users, "r") as infile, open(users_errors, "w") as outfile_errors, open(users_clean, "w") as outfile:

                header = infile.readline().strip()

                if not header:
                    print("error")
                    return

                outfile.write(header + "\n")

                for lineno, line in enumerate(infile, start=2):
                    if not line:
                        continue
                    parts = line.split(",")
                    if len(parts) != 4:
                        outfile_errors.write(f'Line {line}: wrong number of columns -> "{line}"\n')
                        continue

                    id_s, name, age_s, email = [p.strip() for p in parts]

                    try:
                        _ = int(id_s)
                    except ValueError:
                        outfile_errors.write(f'Line {lineno}: invalid id (ValueError) -> "{id_s}"\n')
                        continue

                    if name == "":
                        outfile_errors.write(f'Line {lineno}: missing name -> "{name}"\n')
                        continue

                    try:
                        age_int = int(age_s)
                    except ValueError:
                        outfile_errors.write(f'Line {lineno}: invalid age (ValueError) -> "{age_s}"\n')
                        continue

                    if age_int < 18:
                        outfile_errors.write(f'Line {lineno}: underage -> "{age_s}"\n')
                        continue

                    if "@" not in email:
                        outfile_errors.write(f'Line {lineno}: invalid email -> "{email}"\n')
                        continue

                    outfile.write(f"{id_s}, {name}, {age_int}, {email}\n")

        except FileNotFoundError:
            print("File not found")
            return

        print("Errors: -----------")
        with open(users_errors, "r") as e:
            print(e.read())

        print("Clean version: -----------")
        with open(users_clean, "r") as o:
            print(o.read())


