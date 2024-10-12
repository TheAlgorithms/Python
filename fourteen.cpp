/*14.Create a class called Addition with the member function findAddition() for
calculating the addition between the given numbers during the function
call. Write a program to create an object and call the findAddition()
function with two integer arguments,three integer arguments and two
double arguments to implement function overloading*/

#include <iostream>
using namespace std;

class Addition {
public:
    // Function to calculate addition of two integers
    int findAddition(int a, int b) {
        return a + b;
    }

    // Function to calculate addition of three integers
    int findAddition(int a, int b, int c) {
        return a + b + c;
    }

    // Function to calculate addition of two doubles
    double findAddition(double a, double b) {
        return a + b;
    }
};

int main() {
    Addition add_obj;

    // Call findAddition with two integer arguments
    int result1 = add_obj.findAddition(10, 20);
    
    // Call findAddition with three integer arguments
    int result2 = add_obj.findAddition(10, 20, 30);
    
    // Call findAddition with two double arguments
    double result3 = add_obj.findAddition(10.5, 20.5);

    // Print the results
    cout << "Addition of two integers: " << result1 << endl;
    cout << "Addition of three integers: " << result2 << endl;
    cout << "Addition of two doubles: " << result3 << endl;

    return 0;
}
