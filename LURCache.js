//LRU Cache-----http://www.codewars.com/kata/53b406e67040e51e17000c0a/train/javascript
function LRUCache(capacity, init) {
// TODO: Program Me
	var obj = new Object()
	Object.defineProperty(this , 'capacity' ,{
		set : function(capacity) { this.capacity = capacity} ,
		get : function(){ return this.capacity}
	 })


}


var store = new LRUCache(3, {a: 1});
console.log(store.capacity)
store.capacity = 4
console.log(store.capacity)
console.log(store.size)
