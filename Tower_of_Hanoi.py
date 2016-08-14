F=[];
U=[];
T=[];

def show():
	print "\n\nF : ", F;

	print "U : ", U;

	print "T : ", T;


def mov(From, To):
	To.append(From.pop());

def TOH(n, From, Using, To):
	if n==1:
		mov(From, To);
		show();
	else:
		TOH(n-1, From, To, Using);
		mov(From, To);
		show();
		TOH(n-1, Using, From, To);

n=input("Enter The Height of Hanoi Tower : ");
F=range(n,0,-1);
show();	

TOH(n, F, U, T);



