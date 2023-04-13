infile = open("input.dat",'r')
outfile = open("output.dat",'w')
sum =0
s=infile.read()

numbers =[int(x) for x in s.split()]
print("The numbers are > ")
print(numbers)

for num in numbers:
    print(sum)
    sum =sum + num

sum = str(sum)
# outfile.writable()

outfile.write("The sum is ")
outfile.write(sum)

infile.close()
outfile.close()