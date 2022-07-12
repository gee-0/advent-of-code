# def read_file(filename):
#     with open(filename, 'r') as f:
#         return f.read().splitlines()

# input = read_file('input.txt')

# # print(input)

# for i in range(len(input)):
#     input[i] = int(input[i])

# # calculate how many times the next number is greater than the previous from input
# count = 0
# for i in range(len(input)):
#     numOne = sum(input[i:i+3])
#     numTwo = sum(input[i+1:i+4])
#     if numTwo > numOne:
#         count += 1
        
# print

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

input2 = read_file('input2.txt')

def position():
    depth = 0
    horizontal = 0
    for i in range(len(input2)):
        inputLine = input2[i].split()
        cmd = inputLine[0]
        val = int(inputLine[1])
        if cmd == "down":
            depth = depth + val
        elif cmd == "up":
            depth = depth - val
        else:
            horizontal = horizontal + val
    print(f"Final depth is {depth}")
    print(f"Horizontal movement is {horizontal}")
    print(f"Total movement is {depth * horizontal}")
position()
