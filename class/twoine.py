with open("first/class/any2.txt" ) as f:
    read =  f.read()
    with open("New_sample.txt", "w") as g:
        g.write(read)
