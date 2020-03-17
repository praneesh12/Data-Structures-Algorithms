#mapper.py
import string
import os, sys
# text = "My name is Praneesh, !Praneesh is my name"

# Tokenize the line of data
def mapper():
	
	try: 
		for line in sys.stdin:
			data=text.strip(",").split(" ")
		for word in data:
			cleaned_data = word.translate(string.maketrans("", ""), string.punctuation)
			print("({0}\t{1})".format(cleaned_data, 1))
	except Exception as e:
		print(e)

def reducer():
	word_count=0
	old_key=None

	for line in sys.stdin:
		data = line.strip().split("")

		if len(data)!=2:
			continue

		this_key, count = data

		if old_key and old_key != this_key:
			print("{0}\t{1}".format(old_key, word_count))
			word_count=0

		old_key=this_key
		word_count+=float(count)

	if old_key!=None:
		print("{0}\t{1}".format(old_key, word_count))
















