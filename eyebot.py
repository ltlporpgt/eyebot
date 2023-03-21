import tikolutool
import texttool
import json
import time
import random
bruteforce = False # This is not a config option, don't edit this!

print("<(o)> tikolu.net/edit EYEBOT. for strike2, strike3, and strike4.")

eyef = open('eye.txt','r')
eye=eyef.read()
eyef.close()

print("<(makeyourchoice)>")
print("1>>strike2, manual page crawl")
print("2>>strike3, archive.org-based crawling") # TODO: Maybe get data directly from archive.org automatically? Processing the data took a while to figure out and I don't remember exactly what I had to do. :(
print("3>>strike4, dictionary+strike3 crawling")
print("4>>recover from crash")
choice=input(">>")
if choice == '1':
	print("input page")
	pagename = input("tikolu.net/edit/")
	scanned_pages = []
	unscanned = [pagename]
elif choice == '2':
	print("strike3 time woo")
	pagelistname=input("pagelist:")
	pagelistf=open(pagelistname,'r')
	pagelist=eval(pagelistf.read()) # Don't run this on untrusted data! :P
	pagelistf.close()
	unscanned = pagelist # It's that simple! strike 3 is just, like, 5 minutes of processing wayback machine json data and then 6 lines of code. honestly surprised so many pages survived
	scanned_pages = []
elif choice == '3':
	print("strike4 begins, i see.")
	print("enter comma seperated pagelists/wordlists")
	pagelists=input(">>")
	pagelists=pagelists.split(',')
	pagelists_real=[]
	for pagelistname in pagelists:
		pagelists_real.append(eval(open(pagelistname,'r').read()))
	unscanned = []
	for pagelist in pagelists_real:
		for name in pagelist:
			print(name)
			if name in unscanned:
				pass
			else:
				unscanned.append(name)
	random.shuffle(unscanned)
	scanned_pages = []
elif choice == '4':
	print("Oh no! Anyways...")
	f=open('savestate.json','r')
	savedict=json.loads(f.read())
	unscanned=savedict['unscanned']
	scanned_pages=savedict['scanned_pages']
	pagecount=savedict['pagecount']
	pagearchive=savedict['pagearchive']

print('pausing for test')
time.sleep(5)
def get_links_from_page(pagename):
	page_contents = tikolutool.get_page(pagename)
	#print(page_contents)
	return [texttool.grab_links(page_contents), page_contents]

print("[*] Starting loop...")
try:
	pagecount=pagecount
except NameError:
	pagecount=0
try:
	pagearchive=pagearchive
except NameError:
	pagearchive={} # :^)
while len(unscanned) != 0:
	savedict={'unscanned':unscanned,'scanned_pages':scanned_pages,'pagecount':pagecount,'pagearchive':pagearchive}
	f=open('savestate.json','w')
	f.write(json.dumps(savedict))
	f.close()
	pagename = unscanned[0]
	if pagename.startswith('/'):
		pagename = pagename[1:]
		if pagename in scanned_pages:
			pagename = ''
	if pagename.startswith('edit/'): # some links are tikolu.net/edit/xyz or htwins.net/edit/xyz
		pagename = pagename[len('edit/'):]
		if pagename in scanned_pages:
			pagename = ''
	if pagename.startswith('web/'): # false positive for wayback machine links, web.archive.org[/web/20201923812093801923/example].com is detected.
		pagename = ''
	if pagename == '':
		unscanned = unscanned[1:]
		pass
	links, page_contents = get_links_from_page(pagename)
	unscanned = unscanned[1:]
	scanned_pages.append(pagename)
	print(f"[*] We have scanned {len(scanned_pages)}/{len(scanned_pages)+len(unscanned)}. This is {(len(scanned_pages)/(len(scanned_pages)+len(unscanned)))*100}%.")
	for link in links:
		if link in scanned_pages:
			pass
		elif link in unscanned:
			pass
		else:
			unscanned.append(link)
			print(f"[*] New link discovered: {link}")
	if page_contents != '': # No use overwriting empty pages, eh?
		if not "$$  _|$$$$$$" in page_contents: # detect the funny eye <(o)>
			pagecount += 1
			pagearchive[pagename] = page_contents
			archivef=open('strike4.json','w')
			archivef.write(json.dumps(pagearchive))
			archivef.close()
			print(f"[*] Archived {pagename}. We've archived {pagecount} pages!")
			tikolutool.edit(pagename, eye.replace("%pagecount%",f'{pagecount}'))

print("[*] <(o)> Task Completed")
