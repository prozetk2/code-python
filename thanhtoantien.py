def main():
	can_nang_tao = float(input(" cân nặng táo là : " + " " + "Kg"+ " "))
	can_nang_tao = round(can_nang_tao,1)

	tien_khach_tra = float(input("tiền khách trả: " + " " + "VNĐ"+ " " ))
	tien_khach_tra = round(tien_khach_tra,1)

	gia_1_can_tao = 23000

	tong_tien_tao = gia_1_can_tao * can_nang_tao

	tien_du= tien_khach_tra - tong_tien_tao




	print(" tổng tiền của táo là " + str(tong_tien_tao) + " " + "VNĐ")
	print_input(can_nang_tao,tien_khach_tra)
	tien_tra(tien_du)

def print_input(can_nang_tao,tien_khach_tra):
	gia_1_can_tao = 23000 #23k/1kg

	tong_tien_tao = gia_1_can_tao * can_nang_tao
	tien_du= tien_khach_tra - tong_tien_tao
	if tien_khach_tra == tong_tien_tao:
		print("so tien tra của quý khách vừa đủ")
	elif tien_khach_tra <tong_tien_tao:
		tien_thieu = tong_tien_tao - tien_khach_tra
		print("số tiền khách cần trả thêm là " +str(tien_thieu) +"VNĐ")
	else :
		 
		print("số tiền cần trả lại khách là " + str(tien_du)+"VNĐ")
		tien_du = round(tien_du,0)

def tien_tra(tien_du):
	if tien_du >0 :
		tien_du_500 = tien_du // 500000
		if tien_du_500 != 0 :
				print(" số tờ 500K là "+ " " + str(tien_du_500))
		tien_du_200 = (tien_du % 500000) // 200000
		if tien_du_200 != 0 :
				print(" số tờ 200K là"+ " " + str(tien_du_200))
		tien_du_100 = (tien_du % 500000 % 200000) // 100000
		if tien_du_100 != 0 :
			print(" số tờ 100K là"+ " " + str(tien_du_100))
		tien_du_50 = (tien_du % 500000 % 200000 % 100000) // 50000
		if tien_du_50 != 0 :
			print(" số tờ 50K là" + " "+ str(tien_du_50))
		tien_du_20 = (tien_du % 500000 % 200000 % 100000 % 50000) // 20000
		if tien_du_20 != 0 :
			print(" số tờ 20K là"+ " " + str(tien_du_20))
		tien_du_10 = (tien_du % 500000 % 200000 % 100000 % 50000 % 20000) // 10000
		if tien_du_10 != 0 :
			print(" số tờ 10K là" + " "+ str(tien_du_10))
		tien_du_5 = (tien_du % 500000 % 200000 % 100000 % 50000 % 20000 % 10000) // 5000
		if tien_du_5 != 0 :
			print(" số tờ 5K là" + " "+ str(tien_du_5))
		tien_du_2 = (tien_du % 500000 % 200000 % 100000 % 50000 % 20000 % 10000 % 5000) // 2000
		if tien_du_2 != 0 :
			print(" số tờ 2K là" + " "+ str(tien_du_2))
		tien_du_1 = (tien_du % 500000 % 200000 % 100000 % 50000 % 20000 % 10000 % 5000 %2000) // 1000
		if tien_du_1 != 0 :
			print(" số tờ 1K là"+ " " + str(tien_du_1))
def tien_tra(tien_du):
	if tien_du > 0 :
		count = []
		value = [500000,200000,100000,50000,20000,10000,5000,2000,1000]
		for i in range(0,8):
			so_dem = tien_du//value[i]
			tien_du = tien_du - value[i]*so_dem 
			count.append(so_dem)
		for i in range(0,8):
			if count[i] > 0 :
				print(str(value[i]) +":" + str(count[i]))
		


main()