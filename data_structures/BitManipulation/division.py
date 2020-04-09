'''
Divide two integers without using multiplication, division and mod operator. Return the floor of the result of the division. Example:
5 / 2 = 2
'''
int Solution::divide(int x, int y) {
    
    long long int A,B;
    A=x;
    B=y;
    int s=1;
  if((A^B)<0)
    s=-1;
 //  cout<<s<<endl;
  
  int i;
  
  long long int p,q;
  if(A<=INT_MIN && B<0)
    A=INT_MAX;
   else if(A<=INT_MIN && B>0)
        A=INT_MIN;
        
  //  cout<<A<<" "<<B<<endl;    
    p=abs(A);
    q=abs(B);
    
  //  cout<<p<<" "<<q<<endl;
  long long int ans=0;
  long long int temp=0;
  
  for(i=31;i>=0;i--)
  {
      if(temp+(q<<i)<=p)
      {
          temp+=q<<i;
          ans|=1LL <<i;
      }
  }
   return s*ans;
}

