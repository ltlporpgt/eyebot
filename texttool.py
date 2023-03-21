linkchars='qwertyuioplkjhgfdsazxcvbnmZXCVBNMASDFGHJKLPOIUYTREWQ1234567890%' # Percentages can be apart of the links! e.g. %20 is a space.
def grab_links(text):
	index=0
	state = 'nolink'
	links = []
	currentlink = ''
	while index < len(text): # TODO: This could absolutely be implemented as a regex, and it would likely be faster.
		if state == 'nolink':
			currentlink=''
			if text[index] == '/':
				state = 'link'
		elif state == 'link':
			if text[index] in linkchars:
				currentlink += text[index]
			elif text[index] == '/':
				if currentlink != '': # //hey should be detected as 'hey', /abc/def should be detected as 'abc/def'
					currentlink += '/'
			else:
				if len(currentlink) > 0:
					links.append(currentlink)
				currentlink = ''
				state = 'nolink'
		index += 1
	if currentlink != '':
		links.append(currentlink) # this lets us catch EOF links
	return links
