#Program to read a text file and return number of sentences, words and characters in the file
f= open("ioi.txt")
data = ""
for line in f.readlines():
  data += line
  print (data)
flag1=0
flag2=0
flag3=0
for i in range(0,len(data)):
  if (data[i] == '.'):
    flag3=flag3+1
    #flag2 = flag2 + 1
  if(data[i] == " "):
    flag2 = flag2 + 1
  if ((ord(data[i]) <=90 and ord(data[i]) >= 65 ) or (ord(data[i]) <=122 and ord(data[i]) >= 97) ):
    flag1 = flag1 + 1

print("The text file contain",flag3,"number of sentences,",flag2," words and",flag1," characters")
#print(flag1)
#print(flag2)
#print(flag3)