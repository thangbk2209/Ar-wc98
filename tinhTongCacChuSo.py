def tinhTong(a):
	dem,s=0,0
	while(a%10!=0):
		s+=a%10
		dem=dem+1
		a=a/10
	print 'Co ',dem,' chu so '
	print 'Tong cac chu so la: ', s
if __name__=='__main__':
	m=int(raw_input('Nhap vao m: '))
	tinhTong(m)
