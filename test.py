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