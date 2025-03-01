kata = "The right format"

for _ in range(42 - len(kata)):
    print("-", end='')
print(f"{kata}", end='')
