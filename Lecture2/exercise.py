floor = 123

if floor < 13:
    new_floor = floor - 1
else:
    new_floor = floor

# better
new_floor = floor - 1 if floor < 13 else floor

#switch case using match
status = 404
match status:
    case 200:
        print("OK")
    case 400 | 404:
        print("Client error")
    case 500:
        print("Server error")
    case _:
        print("Unknown status")
