def write(str):
    f = open("msg.txt", "a")
    f.write(str + "\n")
    f = open("msg.txt", "r")
    print(f.read())

msg = input("Send a message: ")

write(msg)