# input----this is a string   

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line


line = input("enter a string: ")
result = split_and_join(line)
print(result)