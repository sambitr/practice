def wrap_string(string, number):
    for i in range(0, len(string), number ):
        print(string[i:i+number])
        if i + number >= len(string):
            break
        
# wrap_string("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)