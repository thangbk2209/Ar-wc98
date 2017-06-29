# in ra day so fibonaci co phan tu cuoi cung nho hon n
def fibo(n):
	a = b = 1
	print "Chuoi fibonaci can tim la : "
	print a , b , 
	while a+b<=n:
		h = a+b
		a=b
		b=h
		print h,
def nhap(a,n):
	for i in range(n):
		a[i] = int(raw_input("Nhap a[%d]= " % i))
def sapxep(K):
	# Sap xep list L
	K.sort()
	print K
if __name__== "__main__":
	n = int(raw_input("Nhap vao gia tri n: "))
	fibo(n)
	m = int(raw_input("Nhap vao so phan tu mang: "))
	L=[1,4,3,2,5,7,2]
	L.sort()
	print L
	x=L.count(2)
	print x
	K=[]
	nhap(K,m)
	print K
	# sapxep(K)