#include <iostream>
#include <vector>
using namespace std;

class millionFib {
public:
	long long fib(int x){
		if (x == 0 || x == 1)
			return x;
		else if ( x < 0)

			return ( (-x) %2 == 1)? fib(-x) : -fib(x); 

		else
			return x;
	};

	vector<int> matrix_multi(vector<int> &a , vector<int> &b){
		int size = 4;
		vector<int> c(size);
		c[0] = a[0]*b[0]+a[1]*b[2];
		c[1] = a[0]*b[1]+a[1]*b[3];
		c[2] = a[2]*b[0]+a[3]*b[2];
		c[3] = a[2]*b[1]+a[3]*b[3];
		return c;
	};


	

};


int main () {
	millionFib mf;
	int nth;
	cout << "Enter the n-th Fib number you want :" << endl;
	cin >> nth ;
	cout << "The " << nth << " th Fib number is " << mf.fib(nth) << endl;
	return 0;	
}