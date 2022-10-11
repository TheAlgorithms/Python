#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n;
	cout<<"\nEnter number of process: ";
	cin>>n;
	
	int bt[n],wt[n],tat[n];
	float avwt=0,avtat=0;
	
	cout<<"Enter burst time: \n";
	for(int i=0;i<n;i++)
	{
		cout<<"p["<<i+1<<"]: ";
		cin>>bt[i];
	}
	
	wt[0]=0;
	//waiting time
	for(int i=1;i<n;i++)
	{
		wt[i]=bt[i-1]+wt[i-1];
	}
	
	//turnaround time
	for(int i=0;i<n;i++)
	{
		tat[i]=bt[i]+wt[i];
		avwt+=wt[i];
		avtat+=tat[i];
	}
	
	
	cout<<"\n\n--------------------------------------------------------------------\n\n";
	
	cout<<"Process ID\tBurst Time\tWaiting time\tTurnaround time\n";
	for(int i=0;i<n;i++)
	{
		cout<<i+1<<"\t\t"<<bt[i]<<"\t\t"<<wt[i]<<"\t\t"<<tat[i]<<"\n";
	}
	
	cout<<"\n\nAverarge waiting time: "<<float(avwt/n);
	cout<<"\nAverage turnaround time: "<<float(avtat/n);
	
	cout<<"\n\n--------------------------------------------------------------------\n\n";
	
	return 0;
}

