# read from input file and store in a list

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

input = read_file('input.txt')

# print(input)


# calculate how many times the next number is greater than the previous from input
count = 0
for i in range(len(input)):
    if i == 0:
        continue
    if int(input[i]) > int(input[i-1]):
        count += 1
print(count)