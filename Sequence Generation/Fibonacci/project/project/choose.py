x = 1
y = 1
seq = [x, y]

def next_term(response):
    for i in range(response):
        z = seq[-2] + seq[-1]
        seq.append(z)
    

def prompt():
    print("The first " + str(len(seq)) + " terms of the fibonacci sequence are: " + str(seq))
    response = int(input("Which term of the fibonacci sequence would you like? "))
    next_term(response)
    print(seq[response-1])

prompt()