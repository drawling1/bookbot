import os

file_path = os.path.expanduser("/home/drawling/workspace/github.com/Drawling1/bookbot/books/frankenstein.txt")




with open(file_path) as f:
	file_contents = f.read()

frankenstein = file_contents

def counting_words(book):
	words = book.split()
	counter = 0
	for word in words:
		counter += 1
	return f"There is {counter} number of words in the book"


def counting_char(book):
	lowered_string = book.lower()
	char_counter = {}
	for char in lowered_string: 
		if char in char_counter:
			char_counter[char] += 1
		else:
			char_counter[char] = 1

	return char_counter



def print_report(book):
	char_counter = counting_char(book)
	word_counter = counting_words(book)
	clean_dict = {}

	for key, value in char_counter.items():
		clean_key = "".join(filter(str.isalpha, key))
		if clean_key:
			clean_dict[clean_key] = value

	book_list = "\n".join(f" the {key} character was found {value} times" for key, value in clean_dict.items())

	return  f"--the report of the book--\n there is {word_counter} words found in the book \n {book_list}\n -- End report --"

test_report = print_report(frankenstein)


print(test_report)




#def main():
	#print(file_contents[:500])
#main() 