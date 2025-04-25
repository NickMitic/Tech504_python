x = 0

while x < 10:
    print(f"x -> {x}")
    # Need to increment x, otherwise would have infinite loop
    x += 1

print()

x = 0

while x < 10:
    print(f"x -> {x}")
    if x == 4:
        break
    else:
        x += 1
