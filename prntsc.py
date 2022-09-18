import urllib.request
import urllib.error
import random
import os
from datetime import datetime
from numberFormatter import formatNum
from timeConverter import convertTime
from sys import argv

def timeInSecs(x):
    return (x.hour * 3600) + (x.minute * 60) + (x.second)

outputFolder = "output" # change if there is already a folder called output which is important

if not os.path.exists(outputFolder):
    os.mkdir(outputFolder)

print("prnt.sc image scraper")

done = False
while not done:
    try:
        if len(argv) == 1:
            amount = int(input("\nHow many pictures do you want? "))
        else:
            amount = int(argv[1])

        if amount < 1:
                print("Amount of images must be at least 1.")
        else:
            try:
                with open("timings.txt") as f:
                    averageTime = f.read()

                averageTime = float(averageTime)
            
            except FileNotFoundError:
                averageTime = 1.1 # default, about 1.1 images per second
            
            except ValueError:
                print("Warning: File 'timings.txt' is corrupted, deleting file...\n")
                os.remove("timings.txt")
                averageTime = 1.1

            timeToScrape = amount / averageTime

            print(f"It will take about {convertTime(timeToScrape)} to gather {amount} images.")
            
            action = input("Continue? (y/n) ").lower()
            if action in ("yes", "y"):
                done = True
    
    except ValueError:
        print("Please enter a number\n")

startTime = datetime.now().time()

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
}

chars = "a b c d e f g h j i k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9".split()

codeList = []

i = 1
while i <= amount:
    code = ""
    for j in range(6):
        code += random.choice(chars)
    if code[0] != "0" and code not in codeList:
        codeList.append(code)
        try:
            print(f"[#{formatNum(i, 'lz', len(str(amount)) - len(str(i)))}] Trying code '{code}'...")
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
            print(f"[!] HTTP Error with code '{code}'")

        except:
            print(f"[!] Error with code '{code}'")
            
    elif code in codeList:
        print(f"[!] Error: code '{code}' has already been saved")
        i += 1

endTime = datetime.now().time()
timeDiff = timeInSecs(endTime) - timeInSecs(startTime)

with open("timings.txt", "w") as f:
    f.write(str((averageTime + (amount / timeDiff)) / 2))
    
input(f"\n{amount} images were gathered in about {convertTime(timeDiff)}. Press 'Enter' to close program.")
