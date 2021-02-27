import hashlib

hash = input("give the hash string you want to crack, better be a good one: ")
f = open("wordlists.txt", "rt")
for x in f:
    x = x.strip("\n")
    word = hashlib.md5(x.encode("utf").strip()).hexdigest()#in this case u can use ant hash algorithm
    if word == hash:
        print("password found:", x)
