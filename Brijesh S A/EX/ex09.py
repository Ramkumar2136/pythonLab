infile =open("input.txt",'r')
outfile =open("output.txt",'w')

lines=chars=0

for line in infile:
    lines +=1
    chars += len(line)
    outfile.write(line)

print(lines," Lines copied ",chars," characters copied.")
infile.close()
outfile.close()