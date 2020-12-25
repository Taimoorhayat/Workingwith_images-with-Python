from PIL import Image

mac = Image.open("example.jpg")

type(mac)

mac

mac.size

mac.filename

mac.crop

mac.format_description

mac.crop((0,0,100,100))

pencils = Image.open("pencils.jpg")
pencils

pencils.size         #(width-----,height |)
x =  0
y = 1100
w = 1950/3
h = 1300

pencils.crop((x,y,w,h))
halfway = 1993/2

x = halfway - 200

w = halfway + 200

y = 700

h = 1257

mac.crop((x,y,w,h))

computer = mac.crop((x,y,w,h))
mac.resize((3000,500))

mac.rotate(90)

################################Color Transperancy


red = Image.open("red_color.jpg")

red
blue = Image.open("blue_color.png")

blue

blue.putalpha(0)
red.putalpha(100)

blue.paste(red,box= (0,0),mask = red)

blue

blue.save("purple.jpg")


mac.paste(im= computer,box=(796,0))
