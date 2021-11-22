start = 0
end = 0
years = 0

while start < 9:
    start = int(input("How many start?\n"))

total = start

while end < start:
    end = int(input("How many end?\n"))

while total < end:
    total += int(total / 3) - int(total / 4)
    years += 1
    print(f"llamas {total}")

print(f"It takes {years} years to achieve the target population size")
