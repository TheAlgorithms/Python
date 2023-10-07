#Program to multiply two complex numbers and returning it in the 
#form - 'a + bi' where a is the real part and b is the imaginary part
#if b is negative we write it as 'a + -bi'

num1 = '1+-2i'  
num2 = '1+1i'

real1, imag1 = map(int, num1[:-1].split('+'))
real2, imag2 = map(int, num2[:-1].split('+'))

real_result = real1 * real2 - imag1 * imag2
imag_result = real1 * imag2 + imag1 * real2 

print(str(real_result)+'+'+ str(imag_result)+'i')
