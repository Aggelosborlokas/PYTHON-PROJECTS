fopen = open("example.py", "r")
a = fopen.readlines()
fopen.close()
for line in a:
    if "#" in line:
        has = line.find("#", 0, len(a))
        if line[:has].count("'") % 2 == 0 or line[:has].count('"') % 2 == 0:
            print(line[:has])
        else:
            print(line)
    else:
        print(line)
