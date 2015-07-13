#!/usr/bin/python
# TODO: complete this class
"""For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

http://www.codewars.com/kata/515bb423de843ea99400000a/train/python
"""

import math
class Pagehelper:

	# The constructor takes in an array of items and a integer indicating
	# how many items fit within a single page
	def __init__(self, collection, items_per_page):
			self.collection = collection
			self.items_per_page = items_per_page
			self.local = locals()
	
	# returns the number of items within the entire collection
	def item_count(self):
			return len(self.collection)
	
	# returns the number of pages
	def page_count(self):
			return int(math.ceil(1.0 * self.item_count() / self.items_per_page))			
	
	# returns the number of items on the current page. page_index is zero based
	# this method should return -1 for page_index values that are out of range
	def page_item_count(self,page_index):
			if (page_index+1) * self.items_per_page <= self.item_count():
					return self.items_per_page
			if page_index*self.items_per_page<self.item_count() and (page_index+1) * self.items_per_page > self.item_count():
					return self.item_count()%self.items_per_page
			return -1
	
	# determines what page an item is on. Zero based indexes.
	# this method should return -1 for item_index values that are out of range
	def page_index(self,item_index):
			if item_index < self.item_count() and item_index >= 0 :
					return item_index/self.items_per_page
			return -1
	

collection = range(1,25)
collection = ['a','b','c','d','e','f']
helper = Pagehelper(collection, 4)

print helper.page_count()
print helper.item_count()
print helper.page_item_count(0) 
print helper.page_item_count(1) 
print helper.page_item_count(2)
print helper.page_index(5)
print helper.page_index(2)
print helper.page_index(20)
