   $$\         $$$\          $$$\         $$\    
  $$  |       $$  _|$$$$$$\   \$$\        \$$\   
 $$  /       $$  / $$  __$$\   \$$\        \$$\  
$$  /        $$ |  $$ /  $$ |   $$ |        \$$\ 
\$$<         $$ |  $$ |  $$ |   $$ |        $$  |
 \$$\        \$$\  \$$$$$$  |  $$  |       $$  / 
  \$$\        \$$$\ \______/|$$$  /       $$  /  
   \__|        \___|         \___/        \__/   
                                                 
                                                 
                                                 
This is the code for eyebot, which is the tool used for strikes 2-4.

This code is for example/demonstration purposes only.
You'll probably have a hard time using it anyways.

====REQUIREMENTS====

STRIKE 2 REQUIRES:
The name of a starting page, e.g. /dict
It will then crawl the pages by scanning for links, so if a page contains "/hello" it will then scan /hello.

STRIKE 3 REQUIRES:
A list of pages in python list form. I.e. a text document that looks like the following:
['page1','page2','page3']

STRIKE 4 REQUIRES:
One or multiple of those lists of pages.
So, you would have two text documents that look like the following:
['page1','page2','page3']
['page3','page4','page5']
And the script will merge them automatically into:
['page1','page2','page3','page4','page5']

EYEBOT REQUIRES:
A text document named 'eye.txt' containing the ascii art/message to display on pages.
You can insert %pagecount% into said text document and the script will replace it with a number showing the amount of pages overwritten.
Also, the strike2/3/4 requirements and the tikolutool requirements.

TIKOLUTOOL REQUIRES:
The 'requests' library.

ARCHIVETOOL REQUIRES:
An archive, either one you build yourself or one I provide.
The links for mine are on /notahome and you can email me for a copy as well.

====NOTES====
Certain data, like pagelists and wordlists, are not something that I will provide.
I will not provide support for using eyebot, though I can provide support for using the *tools in your own project.
If you encounter a bug, file an issue!
The code isn't very robust and has a lot of inefficiencies that need to be resolved.
