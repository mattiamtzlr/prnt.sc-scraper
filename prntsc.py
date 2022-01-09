import urllib.request
import urllib.error
import random

done = False
while not done:
    try:
        amount = int(input("How many pictures do you want? "))
        if amount < 2:
            print("Amount of pictures needs to be at least 2\n")
        else:
            done = True
    
    except ValueError:
        print("Please enter a number\n")
    
amount = int(amount)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

chars = "a b c d e f g h j i k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9".split()

codeList = []

while len(codeList) < amount:
    code = ""
    for i in range(6):
        code += random.choice(chars)
    if code[0] != "0" and code not in codeList:
        codeList.append(code)
        
        try:
            print(f"Trying code '{code}'...")
            pageURL = f"https://prnt.sc/{code}"
            pageRequest = urllib.request.Request(url=pageURL, headers=headers)
            pageContent = str(urllib.request.urlopen(pageRequest).read())

            imageURL = pageContent[int(pageContent.find("no-click screenshot-image") + 32) : len(pageContent)]
            imageURL = imageURL[0 : imageURL.find('"')]

            imageRequest = urllib.request.Request(url=imageURL, headers=headers)
            image = urllib.request.urlopen(imageRequest)

            with open(f"output/{code}.png", "wb") as f:
                f.write(image.read())
        
        except urllib.error.HTTPError:
            print(f"HTTP Error with code '{code}'")

        except:
            print(f"Error with code '{code}'")
