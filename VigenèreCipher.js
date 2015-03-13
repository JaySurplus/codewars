//Vigenère Cipher Helper  ----- http://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/javascript

function VigenèreCipher(key, abc) {
 


  function repeat(k, s) {
  	var time = Math.ceil(s.length / k.length) ;
  	var newKey = Array(time+1).join(k) ;
  	return newKey.substring(0,s.length) ;
  };


  function encodeAndDecode(eAndD , str) { 
  	//eAndD == 1 , encode
  	//eAndD == -1 , decode	
  	var result = '';
   	this.newKey = repeat(key , str);
    for ( var i = 0 ; i < str.length ; i++){
    	shift = abc.indexOf(this.newKey.charAt(i))

    	if (abc.indexOf(str.charAt(i)) < 0){
        	result += str.charAt(i) ;
    	}
    	else {
    		result += abc.charAt((abc.indexOf(str.charAt(i)) + eAndD * shift + abc.length) % abc.length) ;
    	};	
    };
    return result
  } ;



  this.encode = function (str) {
  	return encodeAndDecode(1, str)
  };

  this.decode = function (str) {
    return encodeAndDecode(-1 , str)
  };

}



var abc, key;
abc = "abcdefghijklmnopqrstuvwxyz";
key = "password"
c = new VigenèreCipher(key, abc);

console.log(c.encode('it\'s a shift cipher!'))
console.log(c.decode('rovwsoiv'))