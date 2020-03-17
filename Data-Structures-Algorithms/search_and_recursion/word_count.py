# Write a map reduce word count function

# text = '''In a series of focused, practical tasks, you will start by launching a spark cluster on Amazon's EC2 cloud computing platform.
# As you progress to working with real data, you will gain exposure to a variety of useful tools, including RDFlib and SPARQL. 
# The practical tasks on this course make use of the Gutenberg Project data - the world's largest open collection of ebooks.
# This offers no end of opportunity for highly engaging and novel analyses. As the taught material and example code is given in Python,
# it is strongly recommended that all students have previous Python programming experience. Furthermore, launching and interacting with
# a cluster on EC2 requires basic knowledge of Unix command line, and some experience with a command-line editor such as vim or nano
# would also be advantageous. With these minimal prerequisites, this course is designed to get you up and running in Spark as quickly
# and painlessly as possible, so that by the end, you will be comfortable and competent enough to start engineering your own big data
# solutions.'''

# text1 = "My name is Praneesh. a a a of data data I'm a Data Scientist. I have a masters degree in Information systems from Univ of Maryland. best univ of m"
import sys

def word_count(text):

	for word in sys.stdin:
		text_words = [words.lower() for words in text.split(" ") if '\n' not in words]
	
	count=0
	mapper_dict={}
	for word in text_words:
		if word not in mapper_dict.keys():
			mapper_dict[word] = 1
		else:
			mapper_dict[word]+=1
	return mapper_dict

print(word_count(text))

# numbermap = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# [month[i] for i in sorted(month, key=numbermap.__getitem__)]


