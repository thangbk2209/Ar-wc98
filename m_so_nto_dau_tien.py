def checkNto(m):
	if m<2:
		return 0
	elif m==2:
		return 1
	else:
		for i in range(2,m):
			if(m%i==0):
				return 0
		return 1
dem,k=0,0
if __name__=="__main__":
	m = int(raw_input('Nhap m: '))
	# for(i in range(2,m)):
	# 	if(checkNto(i)==1):
	# 		dem++
	# 		print i
	while dem<m-1:
		if(checkNto(k)==1):
			dem=dem+1
			print k,
		k=k+1

