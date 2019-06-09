def binaryearch(a,ele,beg,end):
	if(ele>a[end]):
		return -1
	else:
		mid=int((beg+end)/2)
		if a[mid]==ele:
			return mid
		elif a[mid]>ele:
			end=mid-1
			return binarysearch(a,ele,beg,end)
		else:
			beg=mid+1
			return binarysearch(a,ele,beg,end)


print ("Welcome to program 3 ")
a=input("Enter a list of comma separated ordered numbers, \n").split(",")
for i in range(0,len(a)):
	a[i]=int(a[i])
ele=int(input("Enter the element to be found : "))
beg=0
end=len(a)-1
pos = int(Search(a,ele,beg,end))
if pos!=-1:
	print("The element ",ele," has been found at position ",pos)
else:
	print("Element not found")
