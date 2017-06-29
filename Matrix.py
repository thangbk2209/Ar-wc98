import numpy as np 
mang1 = np.array([1,2,3,4])
print mang1.ndim   #in ra so chieu
mang2 = np.zeros((2,3)) # tao ra mot mang ma toan bo phan tu cos gia tri bang 0
print mang2
print mang1 ** 2    # Binh phuong tat ca cac phan tu trong mang
# Cac phep toan binh thuong mac dinh la nhan tung phan tu voi nhau
# Nhan hai ma tran: np.dot(A,B)
#					np.inverse(A)
#Nhap vao tat ca cac phan tu cua mang
for i in range(2):
	for j in range(3):
		# mang2[i][j]= raw_input('Nhap mang2[%d][%d]' %(i,j))  Nhap vao tung phan tu mang tu ban phim
		mang2[i][j] = i+j

# Tao mot mang moi co kich thuoc va loai du lieu giong voi mot mang khac

y = np.ones_like(mang2)
print mang2
print y
print ("Ma tran don vi")
a = np.identity(4) # Dua ra ma tran don vi
print a
print("...")
b = np.eye(4, k=1) # Dua ra ma tran vuong bac 4 co cac vi tri ben tren duong cheo mot don vi co gia tri bang 1
print b
print("One-dimensional Arrays")
c= np.arange(0,11) # Tao mang 11 phan tu voi cac phan tu mang co gia tri tu 0-10
print c
print c[5:-1]
d= b[1:4,1:4].copy()
print d
print(" Fancy Indexing and Boolean-values Indexing")
e= np.linspace(0,2,11)  # Dua ra 11 phan tu tu 0-2 cac deu nhau
print e
print (e>0.5)
f=e[e>0.5]
print f
g = np.arange(10)
indices =[2,4,6]
h=g[indices]
print g 
print h
