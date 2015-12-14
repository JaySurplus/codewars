#include <iostream>
#include <vector>
using namespace std;

class millionFib {
public:
	long long fib(int x){
		
		if ( x < 0)
			return ( (-x) %2 == 1)? double_fast(-x)[0] : -double_fast(-x)[0]; 

		else
			return double_fast(x)[0];
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

	vector<int64_t> double_fast(int n){
		vector<int64_t> r(2);
		if (n == 0){
			r[0] = 0;
			r[1] = 1;
			return r;
		}
		else{
			int64_t a = double_fast(n/2)[0];
			int64_t b = double_fast(n/2)[1];

			int64_t c = a * (2*b-a);
			int64_t d = a * a + b * b;

			if (n % 2 == 0){
				r[0] = c;
				r[1] = d;
				return r;
			} 
			else {
				r[0] = d;
				r[1] = c + d;
				return r;
			}

		}
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