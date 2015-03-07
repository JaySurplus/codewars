/*Coordinates Validator    http://www.codewars.com/kata/5269452810342858ec000951/train/javascript */


function isValidCoordinates(coordinates){
	var re = /-?\d+(?:\.\d+)?, -?\d+(?:\.\d+)?$/
	
	
	if (re.test(coordinates)){
		var La_Lo = coordinates.split(', ')
		La_Lo_num = La_Lo.map(function(str) {return Math.abs(Number(str))})
		return  La_Lo_num[0] <= 90 && La_Lo_num[1] <= 180 
	}
	return false; // do your thing!
}

function isValidCoordinates2(coordinates){
	//return /-?((\d)|([0-8]\d)|(90))(\.\d+)?, -?((\d)|([0-8]\d)|(90))(\.\d+)?)$/.test(coordinates)
	return /^-?((\d|[0-8]\d)(\.\d+)?|90), -?((\d\d?|[01][0-7]\d)(\.\d+)?|180)$/.test(coordinates)
	//return /^(-?((\d|[0-8]\d)(\.\d+)?)|90),\s?(-?((\d\d?|[01][0-7]\d)(\.\d+)?)180)$/.test(coordinates);
}



console.log(isValidCoordinates2("43.91343345, 143"));
console.log(isValidCoordinates2("43.91343345, 143"));
/*
var ValidCoordinates = [
		"-23, 25",
		"4, -3",
		"24.53525235, 23.45235",
		"04, -23.234235",
		"43.91343345, 143"
	];
for( i in ValidCoordinates ) {
	Test.expect(isValidCoordinates(ValidCoordinates[i]), ValidCoordinates[i] + " validation failed.");
}

var InvalidCoordinates = [
		"23.234, - 23.4234",
		"2342.43536, 34.324236",
		"N23.43345, E32.6457",
		"99.234, 12.324",
		"6.325624, 43.34345.345",
		"0, 1,2",
		"0.342q0832, 1.2324",
		"23.245, 1e1"
	];
for( i in InvalidCoordinates ) {
	Test.expect(!isValidCoordinates(InvalidCoordinates[i]), InvalidCoordinates[i] + " validation failed.");
}
*/