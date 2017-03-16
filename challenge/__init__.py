def new_phrase(words):
	import re

	#words = input()
	#get rid of punt. and spacing using a regex (regular expression) function
	re.sub('[^A-Za-z0-9]+', '', words)
	#print(wordse)


	