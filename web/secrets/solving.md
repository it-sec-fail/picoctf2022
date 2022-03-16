 1. Visiting the website does not really help... but the *hint* tells that there are some folders. Because gobuster or other fuzzing tools in CTF is not really nice to the infrastructure I tested the usual things:
   - robots.txt -> nothing there
   - sitemap.xml -> nothing there
 1. After some further tests I tried the obvious '/secret/' folder... and bam!
 1. In the sourcecode of this page, we can see a '/hidden/' folder.

	'''html
		<link rel="stylesheet" href="hidden/file.css" />
	'''
 1. Goto the hidden folder, we get a new page where we can see a '/superhidden/' folder.

	'''html
		<link href="superhidden/login.css" rel="stylesheet" />
	'''

 1. The new page in the superhidden folder tells us *Finally. You found me. But can you see me* 
 1. Quick look at the source code or selecting everything on the side, will reveal the flag :)
