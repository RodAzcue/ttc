import ttc
import time
from os import get_terminal_size
from math import cos, sin, tan
import time 


value =""
for i in range(list(get_terminal_size())[0]):
	value+="█"

while True:
	
	color = ttc.hsl(round((cos(time.time()*0.5)+1)*180),100,50)
	ttc.cprint(color, value)