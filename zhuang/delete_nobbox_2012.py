file=open("2012_traindel.txt",'w')
with open("2012_train.txt") as f:
    lines=f.readlines()
    # print(lines)
    for i,line in enumerate(lines):
        print(line)
        print(len(line))
        print("i",i)
        if(len(line)>78):
            file.write(line)