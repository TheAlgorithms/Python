#include<iostream>
using namespace std;
#define MAX 5

class sort
{
	public:
		int arr[MAX];
	
	void input_array();
	void selection_sort_ascen();
	void selection_sort_descen();
};


void sort :: input_array()
{
	cout<<"\nEnter elements in array: ";
	
	for(int i=0;i<MAX;i++)
	{
		cin>>arr[i];
	}
	
	cout<<"\nYour array is as follows: \n";
	for(int i=0;i<MAX;i++)
	{
		cout<<"|"<<arr[i]<<"|";
	}
}

void sort :: selection_sort_ascen()
{
	for(int i=0;i<=MAX-2;i++)
	{
		for(int j=i+1;j<MAX;j++)
		{
			if(arr[i]>arr[j])
			{
				int temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
	}
	
	cout<<"\n\nSorted array is as follows: \n";
	
	for(int i=0;i<MAX;i++)
	{
		cout<<"|"<<arr[i]<<"|";
	}
}


void sort :: selection_sort_descen()
{
	for(int i=0;i<=MAX-2;i++)
	{
		for(int j=i+1;j<MAX;j++)
		{
			if(arr[i]<arr[j])
			{
				int temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
	}
	cout<<"\n\nSorted array is as follows: \n";
	
	for(int i=0;i<MAX;i++)
	{
		cout<<"|"<<arr[i]<<"|";
	}
}



int main()
{
	int size,ch;
	char start='y';
	
	sort s;
	
	while(start=='y')
	{
		cout<<"\n\n1. Selection sorting (Ascending)\n2. Selection sorting (Descending)";
		cout<<"\n\nEnter your choice: ";
		cin>>ch;
		
		switch(ch)
		{
			case 1:
				s.input_array();
				s.selection_sort_ascen();
				
			    break;
			
			case 2:
				s.input_array();
				s.selection_sort_descen();
				
				break;
			
			default:
				cout<<"\nIncorrect choice !!!";
		}
		
		cout<<"\n\nDo you want to continue (y/n): ";
		cin>>start;
	}
	
	return 0;
}
