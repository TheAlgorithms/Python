#This is a sigmoid function
# x i function sigmoid is function variable
#a is the gain
import math
def sigmoid(x,a):
    p = math.exp(-a*x);
    return 1/(1+p);

def main(): 
    #enter values of gain and x
    x=0.5;
    gain = 1;
    print(sigmoid(0.5,1));
if __name__=="__main__": 
    main();
