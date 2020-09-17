with open("cat.jpg", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        print(byte)
        byte = f.read(1)
