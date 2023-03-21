import json
from tqdm import tqdm

dict_threshold = 5 # How many times should a word appear to be counted as a word? This is a config option.

if __name__ == '__main__':
	print("Welcome to the standalone archivetool.")
	print("Please select an option.")
	print("\n[1] Archive2Dictionary")
	print("[99] Exit")
	choice=input(">>")
	if choice == '1':
		print("Enter archive name.")
		filename = input("./")
		file = open(filename,'r')
		unloaded = file.read()
		file.close()
		archive = json.loads(unloaded)
		page_contents = list(archive.values())
		dictionary = {}
		print("Scanning archive for wordlist...")
		for page_index in tqdm(range(len(page_contents))):
			page = page_contents[page_index]
			page=page.replace('\n','')
			words = page.split(' ')
			for word in words:
				if word == '':
					pass
				if word in dictionary:
					dictionary[word] += 1
				else:
					dictionary[word] = 1
		print("Filtering words...")
		good_wordlist = []
		for word_index in tqdm(range(len(list(dictionary.keys())))): # This is a very reasonable line of code
			word=list(dictionary.keys())[word_index]
			if dictionary[word] >= dict_threshold:
				if word.startswith('.'):
					pass
				else:
					good_wordlist.append(word)
		_=open("wordlist.txt",'w').write(repr(good_wordlist))
		print("Done. Written to wordlist.txt")
	else:
		print("Goodbye.")
