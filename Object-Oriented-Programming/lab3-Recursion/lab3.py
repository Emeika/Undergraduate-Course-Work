# 1
def combination(n,k):
	if k == 1:
		return n
	elif n < k:
		return 0
	else:
		return combination(n-1,k-1)+combination(n-1,k)
print(combination(6,2))


# 2

def big(lists, mini , maxi):
	if mini == maxi:
		return lists[mini]
	else:
		maxi = big(lists,mini +1, maxi)
		if lists[mini]>=maxi:
			return lists[mini]
		else:
			return maxi
print(big([8,3,9,5,1],0,4))