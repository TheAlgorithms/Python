/*

Input:
1
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0

Output:
3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9

*/

#include<iostream>
using namespace std;
#define n 9

void print(int a[n][n])
{
    int i,j;
    
    for(i=0;i<9;i++)
       {
           for(j=0;j<9;j++)
            cout<< a[i][j]<<" ";
       } 
       
       cout<<"\n";
}

bool rowsafe(int a[n][n], int row, int num )
{
    int i,j;
    
    for(i=0;i<9;i++)
        if(a[row][i]==num)
            return false;
            
    return true;
}



bool colsafe(int a[n][n], int col, int num )
{
    int i,j;
    
    for(i=0;i<9;i++)
        if(a[i][col]==num)
            return false;
            
    return true;
}



bool boxsafe(int a[n][n], int row,int col, int num )
{
    int i,j;
    
    for(i=0;i<3;i++)
        for(j=0;j<3;j++)
            if(a[i+row][j+col]==num)
                return false;
            
    return true;
}


bool safe(int a[n][n], int row, int col, int num)
{
    if(rowsafe(a,row,num) && colsafe(a,col,num) && boxsafe(a,row-row%3,col-col%3,num) && a[row][col]==0)
        return true;
    
    return false;
}
bool notassigned(int a[n][n], int &r, int &c)
{
    int i,j;
    
    for(r=0;r<n;r++)
        for(c=0;c<n;c++)
            if(a[r][c]==0)
                return false;
                
    return true;
}

bool solve(int a[n][n])
{
    int r, c;
    
    if(notassigned(a, r, c))
        return true;
        
    
    int i,j;
    
    for(i=1;i<=9;i++)
    {
        if(safe(a,r,c,i))
        {
            a[r][c]=i;
            if(solve(a))
                return true;
            a[r][c]=0;
        }
    }
    return false;
    
    
}

int main()
 {
	//code
	
	int t;
	cin>>t;
	while(t--)
	{
	    int a[n][n];
	    
	    int i,j;
	    
	    for(i=0;i<n;i++)
	        for(j=0;j<n;j++)
	            cin>>a[i][j];
	    
	    
	   if(solve(a))
	        print(a);
	    
	   else
	    cout<<-1<<"\n";
	    
	}
	
	return 0;
}
