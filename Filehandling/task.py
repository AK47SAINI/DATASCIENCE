try:
    with open("aa.txt",'x') as f:
        f.write("my name is aashish")
        f.close()
except Exception as e:
    print("file is not present in the given directory!!")
else:
    print("Successfully appended the data in the given file")