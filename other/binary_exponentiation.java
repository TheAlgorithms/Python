/**
* Binary Exponentiation
* This is a method to find a^b in a time complexity of O(log b)
* This is one of the most commonly used methods of finding powers.
* Also useful in cases where solution to (a^b)%c is required,
* where a,b,c can be numbers over the computers calculation limits.
*/

/**
 * @author chinmoy159
 * @version 1.0 dated 10/08/2017
 */
public class bin_expo
{
    /**
    * function :- b_expo (int a, int b)
    * returns a^b
    */
    public static int b_expo(int a, int b)
    {
        /*
         * iterative solution
         */
        int res;
        for (res = 1; b > 0; a *=a, b >>= 1) {
            if ((b&1) == 1) {
                res *= a;
            }
        }
        return res;
        /*
         * recursive solution
        if (b == 0) {
            return 1;
        }
        if (b == 1) {
            return a;
        }
        if ((b & 1) == 1) {
            return a * b_expo(a*a, b >> 1);
        } else {
            return b_expo (a*a, b >> 1);
        }
        */
    }
    /**
    * function :- b_expo (long a, long b, long c)
    * return (a^b)%c
    */
    public static long b_expo(long a, long b, long c)
    {
        /*
         * iterative solution
         */
        long res;
        for (res = 1l; b > 0; a *=a, b >>= 1) {
            if ((b&1) == 1) {
                res = ((res%c) * (a%c)) % c;
            }
        }
        return res;
        /*
         * recursive solution
        if (b == 0) {
            return 1;
        }
        if (b == 1) {
            return a;
        }
        if ((b & 1) == 1) {
            return ((a%c) * (b_expo(a*a, b >> 1)%c))%c;
        } else {
            return b_expo (a*a, b >> 1)%c;
        }
        */
    }
}
