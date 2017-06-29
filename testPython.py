def tinhTienDien(m1,ms,s):
	if s<=100:
		t=m1*s
	else:
		t=100*m1+m2*(s-100)
	print ('Tong so tien phai tra la: '), t

m1 = int(raw_input("Nhap gia cho 100 so dau: "))
m2 = int(raw_input("Nhap gia cho luong so dien con lai: "))
s = int(raw_input("Luong dien tieu thu la: "))
tinhTienDien(m1,m2,s)