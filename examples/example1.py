

import ttc
import time
from os import get_terminal_size
from math import cos
import time 
"""
color1 = ttc.rgb(255,200,0)
print(color1)


color2 = ttc.hsl(200,100,50)
print(color2)
"""




colorPallete = [
	ttc.colors["red"],
	ttc.colors["purple"],
	ttc.colors["orange"],
	ttc.colors["orange"],
	ttc.colors["orange"]
]



ttc.header(colorPallete, "─", ttc.banner("TTS",minus=-2), "Azcué", 1.0, "Terminal True Colors")


time.sleep(5)
ttc.csys(ttc.colors["green"],"[-]", "The program started smoothly")
time.sleep(1)
ttc.csys(ttc.colors["yellow"],"[~]", "Waiting for something... ", end='')
time.sleep(3)
ttc.csys(ttc.colors["green"],"[OK]")
time.sleep(0.5)
ttc.csys(ttc.colors["yellow"],"[~]", "Waiting for something else... ", end='')
time.sleep(3)
ttc.csys(ttc.colors["red"],"[x]")
time.sleep(1)
ttc.cgradprint(ttc.colors["red"],ttc.colors["purple"],"9vnpY<VB89PA\n    FHLEIFHLE8HU.89		3V<PHJ 4LVB		3V89PA\n    FHLEIFHLEIB7	sanFHLE8HU.89	9PA\n           FHLEI	3V<dwflvie93")
time.sleep(1)
ttc.csys(ttc.colors["red"],"[!]", "Something went wrong!")
time.sleep(2)
ttc.csys(ttc.colors["orange"],"[?]", "Resolving the problem ", end='')
time.sleep(3)
ttc.csys(ttc.colors["green"],"[OK]")
time.sleep(2)
ttc.csys(ttc.colors["green"],"[-]", "Everything is fine")
time.sleep(1)
ttc.csys(ttc.colors["green"],"[-]", "I'm fine")
time.sleep(1)
ttc.csys(ttc.colors["green"],"[-]", "You're fine")
time.sleep(2)
ttc.csys(ttc.colors["purple"],"[~]", "Executing raimbow_dash.exe ",end='')
time.sleep(3)
ttc.csys(ttc.colors["green"],"[OK]")
time.sleep(0.5)


while True:
	value =""
	for i in range(list(get_terminal_size())[0]):
		value+="█"
	color = ttc.hsl(round((cos(time.time())+1)*180),100,50)
	ttc.cprint(color, value)

"""
ttc.cprint(ttc.colors["orange"], "[!]")
ttc.cprint(ttc.colors["yellow"], "[?]")
ttc.cprint(ttc.colors["darkGreen"], "[~]")
ttc.cprint(ttc.colors["lightGreen"], "[¬]")
ttc.cprint(ttc.colors["grey"], "[→]")
ttc.cprint(ttc.colors["lightBlue"], "[-]")
ttc.cprint(ttc.colors["blue"], "[=]")
ttc.cprint(ttc.colors["darkBlue"], "[≡]")
ttc.cprint(ttc.colors["green"], "[+]")
ttc.cprint(ttc.colors["red"], "[x]")
ttc.cprint(ttc.colors["pink"], "[<]")
ttc.cprint(ttc.colors["purple"], "[>]")
"""






#for i in range(len(banner)):
#	ttc.cprint(ttc.hsl(  (i*(100/len(banner)))+300, 100, 50), banner[i], end='')


#ttc.cprint(ttc.colors["red"],figlet_format("Important!!",font='big'))


#ttc.cprint(ttc.colors["red"],"Important!!")