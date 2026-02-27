class Loops0:

    inum = "3901827"
    itrack = 0


    for idg in inum:
        if int(idg) > itrack:
            itrack = int(idg)

    print(inum)
    print(f"largest digit found {itrack}")