#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n;
	
	cout<<"Enter number of process: ";
	cin>>n;
	
	int at[n],bt[n],ct[n],tat[n],wt[n];
	float avwt=0,avtat=0;
	
	cout<<"\n\nEnter arrival time: \n";
	
	for(int i=0;i<n;i++)
	{
		cout<<"p["<<i+1<<"]: ";
		cin>>at[i];
	}
	
	cout<<"\nEnter burst time: \n";
	for(int i=0;i<n;i++)
	{
		cout<<"p["<<i+1<<"]: ";
		cin>>bt[i];
	}
	
	int temp;
	
	for(int i=0;i<n;i++)
	{
		for(int j=i+1;j<n;j++)
		{
			if(bt[i]>bt[j])
			{
				temp=bt[i];
				bt[i]=bt[j];
				bt[j]=temp;
				
				temp=at[i];
				at[i]=at[j];
				at[j]=temp;
			}
		}
	}
	
	
	int min,d;
	min=at[0];
	
	for(int i=0;i<n;i++)
	{
		if(min>at[i])
		{
			min=at[i];
			d=i;
		}
	}
	
	int tt;
	tt=min; //pointer
	ct[d]=tt+bt[d];
	tt=ct[d];
	
	for(int i=0;i<n;i++) //calculate completion time
	{
		if(at[i]!=min)
		{
			ct[i]=tt+bt[i];
			tt=ct[i];
		}
	}	
	
	for(int i=0;i<n;i++)  //calculate tat and wt
	{
		tat[i]=ct[i]-at[i];
		wt[i]=tat[i]-bt[i];
		avtat+=tat[i];
		avwt+=wt[i];
	}
	
	cout<<"\n\n------------------------------------------------------------------------------\n\n";
	
	cout<<"Process ID\tArrival time\tBurst Time\tWaiting time\tTurnaround time\n";
	for(int i=0;i<n;i++)
	{
		cout<<i+1<<"\t\t"<<at[i]<<"\t\t"<<bt[i]<<"\t\t"<<wt[i]<<"\t\t"<<tat[i]<<"\n";
	}
	
	cout<<"\n\nAverarge waiting time: "<<float(avwt/n);
	cout<<"\nAverage turnaround time: "<<float(avtat/n);
	
	cout<<"\n\n------------------------------------------------------------------------------\n\n";
	
	
	return 0;
}
