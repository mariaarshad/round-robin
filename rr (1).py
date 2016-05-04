#include<stdio.h>
def main():
	arr=[]
	b_time=[]
	r_t=[]
	c_time=[]
	n=0
	p=int(input('enter the total no of processess :'))
	p1=p
	for i in xrange(p):
		print 'for process' ,i+1
		x=int(input('enter the arrivl time : '))
		arr.append(x)
		x=int(input('enter the burst time  : '))
		b_time.append(x)
		r_t.append(b_time[i])
		c_time.append(0)
	time_q=int(input('enter time quantum'))
	j=0
	t_time=0
	check=0
	ind=p
	while p!=0:
		if r_t[j]<= time_q and  r_t[j]>0:
			t_time=t_time+r_t[j]
			print r_t[j]
			r_t[j]=0
			c_time[j]=t_time
			check=1
			print 'hello'
			
		elif r_t[j] >0 and  r_t[j]>= time_q :
			r_t[j]=r_t[j]-time_q
			print r_t[j]
			t_time=t_time+r_t[j]
			print 'hello1'
		if r_t[j]==0 and check==1:
			p=p-1
			check=0
			print 'hello2'
		if j==p1-1:	
			j=0
			print 'hello3'
		elif arr[j+1]<=t_time:
			j=j+1
			print 'hello4'
		else:
			j=0
		
		
	print 'process \t arrivaltime \t bursttime \t waitingtime'
	for i in xrange(p1):
		print i+1,'\t\t', arr[i] , '\t\t', b_time[i],'\t\t',c_time[i]-arr[i]-b_time[i]
if __name__=="__main__":
	main() 
	






		
		
