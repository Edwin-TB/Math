x = 1
y = 1
seq = [x, y]

def next_term():
    z = seq[-2] + seq[-1]
    seq.append(z)

def prompt():
    print("The first " + str(len(seq)) + " terms of the fibonacci sequence are: " + str(seq))
    response = input("Would you like to add another? [y/n]")
    if response == "y":
        next_term()
        print(seq)
        prompt()
    else: 
        print("Ok!")

prompt()