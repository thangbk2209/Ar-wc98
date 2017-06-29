def nhap(a,n):
	for i in range(n):
		a.append(int(raw_input("Nhap a[%d]= " % i)))
def search(K,a):
	"""tim kiem vi tri phan tu co gia tri bang a"""
	vi_tri=[]
	for i in range(len(K)):
		if K[i] == a:
			vi_tri.append(i+1)
	print vi_tri
if __name__ == "__main__":
	L = []
	nhap(L,5)
	n= int(raw_input("Nhap vao gia tri can tim: "))
	search(L,n)