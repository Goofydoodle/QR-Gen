import uuid
import pyqrcode 
import png

print("Welcome to QR code generator")

url = str(input("Enter the URL: "))

skip = str(input("do u want to skip the customization part? (y/n): "))
if skip == "y":
    color = "#000000"
    bgcolor = "#ffffff"
    print('''it's done check the folder''')
else:
    color = str(input("Enter the color in hex format: "))
    bgcolor = str(input("Enter the background color in hex format: "))
    print('''it's done check the folder''')

# now to generate the qr code

qr_code = pyqrcode.create(url)

#to make random name for the file
shotuuid = uuid.uuid4()
x = str(shotuuid)[:5]


filename = str(x) + ".png"

# now we need to save this qr code in our folder
qr_code.png(filename, scale = 8, module_color = (color), background = (bgcolor), quiet_zone = 1)



