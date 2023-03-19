# Print numbers from 0 to 10 using while
# Skip the 5 iteration from print
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)



# Print numbers from 0 to 1o using for
# Stop the loop if the number = 5
for j in range(11):
    if j ==5:
        break
    print(j)
# Print multiplication table from 1 to 5
for m in range(6):
    print(f'multiplication table of {m}')
    for n in range(11):
        print(f'{m} x {n} = {m*n}')