a=open("06ReadWriteAppend.txt","w")
a.write("Hello World")
a.close()
b=open("06ReadWriteAppend.txt","rt")
print(b.read)
b.close()
c=open("06ReadWriteAppend.txt","a")
c.write(", My Name Adhil.")