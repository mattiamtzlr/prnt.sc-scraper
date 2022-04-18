# prnt.sc scraper

This python script will collect the given amount of images from the website [prnt.sc](https://prnt.sc/) using random 6-digit codes.  
Example: https://prnt.sc/jasdfj

The scraper works by getting the whole html using [urllib](https://docs.python.org/3/library/urllib.html) and cutting away anything around the image link. It sounds rudimental but works surprisingly well and fast.  
The images are saved in the folder _output/_ of the directory in which _prntsc.py_ is saved.

The scraper also collects information about how long it takes to gather the images. This value is updated after every run and stored in the file _timings.txt_ in the same directory as _prntsc.py_. Please don't delete it. This value might fluctuate quite a bit.

**WARNING:** I am not responsible for any damage done to your computer or network when using this script. Don't try to use threads to make the scraping faster, it will get you ip-banned from prnt.sc.  
I also take no responsibility if you get in trouble by using any of the data in the gathered images.
