n = 0
while True:
    try:
        n = int(input("Height:"))
    except ValueError:
        continue

    if 0 < n < 9:
        break

for i in range(1, n + 1):
    print((n - i) * " " + i * "#" + "  " + i * "#")
