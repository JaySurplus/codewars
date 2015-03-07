/*
function validBraces(braces){
	//TODO 
	
	pos = {'(':1  , '[':1 , '{':1 }
	rel = {')' : '(' , ']' : '[' , '}' : '{'}
	empt = []
			
	list = braces.split('')
	len = list.length
	
	for ( var i = 0 ; i < list.length ; i++){
		if (list[i] in pos){
			empt.push(list[i])
		//	console.log('A')
		}		
		else {
			if (empt[empt.length - 1] ==rel[list[i]])
				empt.pop()
			else 
				return false
		}	
		//console.log(empt)
	}
	return empt.length == 0 ? true : false
	
}
*/




function validBraces(braces){
	//TODO 
	list = { '(' : ')' , '[':']' , '{' : '}' }
	stack = []
	current = ''
	
	for (var i in braces){
		
		current = braces[i]
		
		if (list[current]){
			stack.push(current)
			} 
		else {
			 if (current !== list[stack.pop()]){
				 return false
			}
	
		}
	
	}
	return stack.length === 0
}



str = '()()()'
console.log(validBraces(str))