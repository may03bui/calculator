import math

def calculator(operator, a, b):
    if operator == "x":
        return a * b
    elif operator == "+":
        return a + b
    elif operator == "/":
        return a / b
    elif operator == "-":
        return a - b
    else:
        print("Invalid operation")


def process_file(file_name):
    converted_file_name = "data/" + file_name
    acc = 0
    with open(converted_file_name, "r") as file:
        lines = file.read().splitlines()
        for l in lines:
            (calc, operator, a, b) = l.split(" ")
            acc += calculator(operator, int(a), int(b))

    return acc


def process_goto(file_name):
    converted_file_name = "data/" + file_name
    with open(converted_file_name, "r") as file:
        lines = file.read().splitlines()
        bitmap = [False for i in range(0, len(lines))]
        prevAddr = -1
        currAddr = 0
        found = False

        while not found:
            current_line = lines[currAddr]
            splitted = current_line.split(" ")
            prevAddr = currAddr

            if len(splitted) == 2:
                currAddr = int(splitted[1]) - 1
            else:
                currAddr = math.floor(calculator(splitted[2], int(splitted[3]), int(splitted[4]))) - 1

            if bitmap[currAddr]:
                found = True
            else:
                bitmap[currAddr] = True

            print(prevAddr)
            print(currAddr)
            print()

        return currAddr + 1


def annoying_process(file_name):
    converted_file_name = "data/" + file_name
    with open(converted_file_name, "r") as file:
        lines = file.read().splitlines()
        bitmap = [False for i in range(0, len(lines))]
        prevAddr = -1
        currAddr = 0
        found = False

        while not found:
            current_line = lines[currAddr]
            splitted = current_line.split(" ")
            prevAddr = currAddr

            if splitted[0] == "goto":
                if len(splitted) == 2:
                    currAddr = int(splitted[1]) - 1
                else:
                    currAddr = math.floor(calculator(splitted[2], int(splitted[3]), int(splitted[4]))) - 1

            elif splitted[0] == "remove":
                index = int(splitted[1]) - 1   # The line number converted so it corresponds to the list index
                if len(lines) > index >= 0:
                    lines.pop(index)
                    bitmap.pop(index)

                if index > prevAddr:
                    currAddr += 1

            else:  # Replace
                index1 = int(splitted[1]) - 1
                index2 = int(splitted[2]) - 1

                if len(lines) > index1 >= 0 and len(lines) > index2 >= 0:
                    lines[index1] = lines[index2]

                currAddr += 1


            if bitmap[currAddr] or currAddr >= len(lines) or currAddr < 0:
                found = True
            else:
                bitmap[currAddr] = True

            print(lines[prevAddr])

        return prevAddr + 1





# print(process_file("step2.txt"))
# print(process_goto("step3.txt"))
print(annoying_process("step4.txt"))