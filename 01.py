firstname = input(" your firstname: ")


lastname = input(" your lastname: ")

age = int(input("age: "))
chieu_cao = float(input("chieu cao: "))
gender_input = input(" giới tính của bạn là ?:")

namsinh= 2022 - age 
Chieu_cao_quoc_te = chieu_cao * 3.281 
Chieu_cao_quoc_te = round(Chieu_cao_quoc_te,1)


print("\n-----------")

print("ten cua ban la :",firstname + " " +lastname)
print(" nam sinh cua {1} la :{0}".format(namsinh,firstname))
print("chieu cao quốc tế của bạn là : " + str(Chieu_cao_quoc_te) + " " +"feet")

gioi_tinh= None 

if (gender_input == "nam") or (gender_input == "Nam") or (gender_input == "NAM") :
	gioi_tinh = True 
elif (gender_input == "nữ") or (gender_input == "Nữ") or (gender_input == "NỮ") :
	gioi_tinh = False 
else :
	gioi_tinh = None 

if gioi_tinh == None :
	print(" bạn là 3D gòi phở hông")

elif gioi_tinh == True :
	if Chieu_cao_quoc_te > 6.0: 
		print(" Bạn là 1 thằng ", end="")
		for i in range(10):
		# in 10 từ cao khi sử dụng vòng lặp for	
			print("cao", end=" ")
		print("vãi loz luôn")
	elif Chieu_cao_quoc_te > 5.5: 
		print(" Bạn là một người cao bình thường")
	else: 
		print(" Bạn là một thằng ", end="")
		# in 10 từ lùn khi sử dụng vòng lặp while
		i=0
		while i<10:
			print("lùn ", end="")
			i+=1 
		print("vãi loz luôn")

elif gioi_tinh == False: 
	if Chieu_cao_quoc_te >= 5.2: 
		print("bạn là một cô gái cao vãi loz ")
	else: 
		print(" Bạn là một cô gái lùn dễ thương ")
else: 
	print(" mày nhập sai rồi thằng nhóc")


