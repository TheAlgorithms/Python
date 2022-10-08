#include <bits/stdc++.h>
#define vi vector<int>
using namespace std;
void merge(vi &v,int e,int b,int a,int c,int r)
{
    vi v1,v2,v3,v4;
    for(int i=0;i<b-e+1;i++)
    v1.push_back(v[e+i]);
    for(int j=0;j<a-b;j++)
    v2.push_back(v[b+j+1]);
    for(int j=0;j<c-a;j++)
    v3.push_back(v[j+a+1]);
    for(int j=0;j<r-c;j++)
    v4.push_back(v[c+j+1]);


    v1.push_back(INT_MAX);
    v2.push_back(INT_MAX);
    v3.push_back(INT_MAX);
    v4.push_back(INT_MAX);

    int i=0,j=0,k=0,l=0;
    vector<int> x;
    while(i<v1.size() && j<v2.size() && k<v3.size() && l<v4.size())
    {
        if(v1[i]==INT_MAX && v2[j]==INT_MAX && v3[k]==INT_MAX  && v4[l]==INT_MAX)
        break;
        else if(v1[i]<v2[j] && v1[i]<v3[k] && v1[i]<v4[l])
       { x.push_back(v1[i]);
i++;
       }
        else if(v1[i]>v2[j] && v2[j]<v3[k] && v2[j]<v4[l])
      {  x.push_back(v2[j]);
j++;
      }
      else if(v1[i]>v3[k] && v2[j]>v3[k] && v4[l]>v3[k])
      {
        x.push_back(v3[k]);
        k++;

      }
      else
      {
        x.push_back(v4[l]);
        l++;
      }

    }
  
   for(int i=0;i<x.size();i++)
   {
    v[e+i]=x[i];

   }
}
void mergesort(vi &v,int l,int h)
{
    if(l<h)
    {
        int a=(l+h)/2;
        int b=(a+l)/2;
        int c=(a+h)/2;

       
        mergesort(v,l,b);
        mergesort(v,b+1,a);
        mergesort(v,a+1,c);
        mergesort(v,c+1,h);
        merge(v,l,b,a,c,h);

    }
}
int main(int argc, char const *argv[])
{

vector<int> v={23,1,100,987,-100,0,56};
mergesort(v,0,v.size()-1);
for(int i=0;i<v.size();i++)
cout<<v[i]<<" ";

    return 0;
}
