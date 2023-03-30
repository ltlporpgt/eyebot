#functions to interface with tikolu.net/edit/ itself, e.g. getting page content, overwriting page content

import requests
import html
import time

blacklist = [ # xgr's protection script seems to be ran locally, in certain hours of the day news/ is entirely unprotected. Useful! :P
]

headers = { # Make sure to change the user agent every now and then! :)
	'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
}

def get_page(page_name, print_log=True):
	if print_log:
		print(f"[*] Getting page {page_name}...")
	if len(page_name) > 128:
		if print_log:
			print("[*] Failed, page title is too long.")
		return ''
	# page_name takes the form of 'chatroom' for tikolu.net/edit/chatroom
	full_domain = f'https://tikolu.net/edit/.text/{page_name}' # Had no idea .text existed, thanks to .62.196 for letting me know
	try:
		req = requests.get(full_domain, headers=headers)
	except KeyboardInterrupt:
		exit()
	except:
		return ''
	if req.status_code != 200 and req.status_code != 414: # Unknown error code
		print("[!] OH GOD SOMETHINGS WRONG pageread")
		print(f"Page name:   {page_name}")
		print(f"Status code: {req.status_code}")
		f=open('errorpage.html','w')
		f.write(req.text)
		f.close()
		print("PAGE CONTENTS WRITTEN TO errorpage.html")
		exit()
	elif req.status_code == 414: # 414 URI Too Long
		if print_log:
			print("[!] Page title too long and len() didn't catch it, unicode title?")
		return ''
	else: # 200 OK
		return req.text

def edit(page_name, contents, print_log=True):
	if print_log:
		print(f"[*] Editing page {page_name}")
	if len(page_name) > 128:
		print("[*] Failed, page title is too long.")
		return
	for thing in blacklist:
		if page_name.startswith(thing):
			if print_log:
				print(f"[*] nvm, it's in the blacklist")
			return
	full_domain = f'https://tikolu.net/edit/{page_name}'
	timestamp = time.time()
	contents=contents.replace("\\","\\\\") # Replace \ with \\. We need to do this first!
	contents=contents.replace('"','\\"')
	contents=contents.replace("\n","\\n")
	payload = f'{{"content":"{contents}","ignoreconflict":true,"timestamp":"{timestamp}"}}'
	try:
		req=requests.post(full_domain, headers=headers, data=payload)
	except:
		return
	if req.status_code == 414:
		if print_log:
			print("[!] Page title too long and len() didn't catch it, unicode title?")
		return
	json_req = req.json()
	if json_req['status'] == "success":
		if print_log:
			print(f'[*] Edit success! ip: {json_req["ip"]} content size: {json_req["contentsize"]}')
	elif json_req['status'] == "error" and json_req['cause'] == 'unmodified':
		if print_log:
			print(f'[*] Warn: Editing page made no changes.')
	else:
		print("[!] OH GOD SOMETHINGS WRONG pagewrite") # i could probably easily consolidate this into an Exception but that would take effort. bleh
		print(f"Page name: {page_name}")
		print(f"Status:    {json_req['status']}")
		f=open('errorpage.html','w')
		f.write(req.text)
		f.close()
		print("PAGE CONTENTS WRITTEN TO errorpage.html")
		exit()
