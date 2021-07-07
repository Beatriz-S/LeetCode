<<<<<<< HEAD

inp=4
for i in range(inp+1):
    result=(i**2)+i/2
    print(result)
=======
def conversion(sec):
   sec_value = sec % (24 * 3600)
   print("sec: " + str(sec) + " % " + " (24*3600): " + str(24*3600) + " = " + str(sec_value))
   hour_value = sec_value // 3600
   sec_value %= 3600
   min = sec_value // 60
   sec_value %= 60
   print("Converted sec value in hour:", hour_value)
   print("Converted sec value in minutes:", min)
    
sec = 50000
conversion(sec)

'''
S=int(input())
M=S//60
Minutes=S//60
H=M//60

remainder=H-Minutes

while(remainder>60):
   if(remainder>=60):
      H=H+1
      remainder=remainder-60

print(str(H) + " " + str(M))
'''
>>>>>>> e0b1c4e4a5ed2f02bcbe229f0e3e10ff3db5dc89
