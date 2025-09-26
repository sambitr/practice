def solve(s):
    #return s.title()
    result = []
    for part in s.split(" "):
        result.append(part.title())
    return " ".join(result)

# response = solve("1 w 2 r 3g")
# print(response)