//   http://www.codewars.com/kata/52bd8335d9aca8fb16000341/train/javascript


function bitCount(n) {
var c = 0  
  // Count the bits
while(n){
	temp = n >> 1 <<1
	c += temp ^ n
	n = n >>1
  }
return c
}


//console.log(n&=n-1);


function bitCount2(n) {
	for (var c = 0 ; n ; c++)
		n &= n - 1
	return c
}


console.log(bitCount2(1023))