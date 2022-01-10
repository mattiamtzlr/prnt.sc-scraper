import urllib.request
import urllib.error
import random
import os

outputFolder = "output" # change if there is already a folder called output which is important

if not os.path.exists(outputFolder):
    os.mkdir(outputFolder)

print("prnt.sc image scraper")

done = False
while not done:
    try:
        amount = int(input("\nHow many pictures do you want? "))
        if amount < 2:
            print("Amount of pictures needs to be at least 2\n")
        else:
            amount = int(amount)

            # About 1.2 images per second
            timeToScrape = amount / 1.2
            timeUnit = "seconds"
            if timeToScrape > 60:
                timeToScrape = timeToScrape / 60
                timeUnit = "minutes"
            if timeToScrape > 60:
                timeToScrape = timeToScrape / 60
                timeUnit = "hours"

            print(f"It will take about {round(timeToScrape, 2)} {timeUnit} to gather {amount} images.")
            
            action = input("Continue? (y/n) ").lower()
            if action in ("yes", "y"):
                done = True
    
    except ValueError:
        print("Please enter a number\n")       

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

chars = "a b c d e f g h j i k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9".split()

i = 1
while i <= amount:
    code = ""
    for j in range(6):
        code += random.choice(chars)
    if code[0] != "0":        
        try:
            print(f"[#{i}] Trying code '{code}'...")
            pageURL = f"https://prnt.sc/{code}"
            pageRequest = urllib.request.Request(url=pageURL, headers=headers)
            pageContent = str(urllib.request.urlopen(pageRequest).read())

            imageURL = pageContent[int(pageContent.find("no-click screenshot-image") + 32) : len(pageContent)]
            imageURL = imageURL[0 : imageURL.find('"')]

            imageRequest = urllib.request.Request(url=imageURL, headers=headers)
            image = urllib.request.urlopen(imageRequest)

            with open(f"output/{code}.png", "wb") as f:
                f.write(image.read())
            
            i += 1
        
        except urllib.error.HTTPError:
            print(f"HTTP Error with code '{code}'")

        except:
            print(f"Error with code '{code}'")
