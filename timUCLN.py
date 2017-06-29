def UCLN(a,b):
	m = a%b
	while(m!=0):

		a=b
		b=m
		m=a%b
	return b

if __name__=="__main__":
	m=int(raw_input('Nhap vao m: '))
	n = int(raw_input('Nhap vao n: '))
	print UCLN(m,n)
