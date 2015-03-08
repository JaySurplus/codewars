// Catching Car Mileage Numbers --- http://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/javascript
// Catching Car Mileage Numbers --- http://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/javascript
function isInteresting(number, awesomePhrases) {
	// Go to town!
	var re = /\d+\.\d+/
	
	if (number < 98 || number > 1e9 || re.test(number.toString())){
		return 0
	}
	
	if (test(number ,awesomePhrases) && number > 99 ){
		return 2
	}

	if (test(number + 1, awesomePhrases) || test(number+2 , awesomePhrases)){
		return 1
	}
	
	return 0
	
	function test(num , awesomePhrases) {
		return isPalindrome(num) || (awesomePhrases.indexOf(num) !== -1) || num % 100 === 0 || sameDigit(num) || seq(num)
	}
	
	function isPalindrome(num) {
		return num.toString() === num.toString().split('').reverse().join('')
	}
	
	function sameDigit(num) {
		var cur = num % 10
		num = parseInt( num / 10 )
		
		while (num !== 0) {
			if (cur !== num % 10)
				return false
			num = parseInt( num / 10 )
		}
		return true
	}
	
	
	function seq(num) {
		var inc_seq = '1234567890'
		var deinc_seq = '9876543210'
		var num_str = num.toString()
		
		for (var i = 0 ; i + num_str.length <= 10  ; i ++){
			if (inc_seq.substring(i , i + num_str.length) === num_str ||  deinc_seq.substring(i , i + num_str.length) == num_str)
				return true
		}
    return false
	}
}




//console.log(isInteresting(2.3, []));
console.log(isInteresting(100.1, []));
console.log(isInteresting(100, []));
console.log(isInteresting(111, []));
console.log(isInteresting(1221, []));
console.log(isInteresting(1231, [1231]));
console.log(isInteresting(10000, []));
console.log(isInteresting(1111111, []));