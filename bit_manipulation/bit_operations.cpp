using namespace std;
#include<bits/stdc++.h>


//to get the value of ith bit
int getithbit(int x,int i)
{
	int v=1<<i;
	return (x&v)>0?1:0;

}

//to clear the value of ith bit i.e.. make it 0
void clearithbit(int &x,int i)
{

	int v=~(1<<i);	
	x= x&v;
}


//make last i bits equal to 0
void clearlastibits(int &x,int i)
{
	int v=(-1<<i);
	x=x&v;
}

//make bits lying between i and j to 0
void clearbitsinrange(int &x,int i,int j)
{
	int v=((1<<i)-1)|((~0<<j+1));
	x=x&v;
}

//reversing the value of ith bit
void setithbit(int &x,int i)
{
	int v=1<<i;
	x=x|v;
}


//updating the value of ith bit to val
void updateithbit(int &x,int i,int val)
{
	int v=val<<i;
	clearithbit(x,i);
	x=x|v;
	
}


//replace all bits between i and j with m
void replacerange(int &n,int m,int i,int j)
{
	while(i<=j)
	{
		int val=m&(1<<i);
		updateithbit(n,i,val);
		i++;
	}
}

//driver function
int main()
{
	int n,i;
	cin>>n>>i;
	cout<<getithbit(100100110,0)<<endl;
	clearithbit(n,i);
	cout<<n<<endl;
	clearlastibits(n,i);
	cout<<n<<endl;
	setithbit(n,i);
	cout<<n<<endl;
	updateithbit(n,i,1);
	cout<<n<<endl;
	
	replacerange(n,1,i,5);
	cout<<n<<endl;
	clearbitsinrange(n,i,5);

	cout<<n<<endl;
	return 0;
}

/*
Input
15
2
Output
0
11
8
12
12
0
0


*/
