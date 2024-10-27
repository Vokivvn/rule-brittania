import os
from PIL import Image
import timeit

#by uncountably
#WHENEVER YOU CHANGE STATES, PLEASE RUN THIS PROGRAM AND COPY THE OUTPUT TO THE APPROPRIATE SECTION OF RB_anglo_count_on_actions.txt
#just change the states, defs, and provs to point to the correct directory for your system, change the output as well, and then double click to run

states = r"C:\Users\-----\Documents\Paradox Interactive\Hearts of Iron IV\mod\rule-brittania\history\states"
defs = r"C:\Users\-----\Documents\Paradox Interactive\Hearts of Iron IV\mod\rule-brittania\map\definition.csv"
provs = r"C:\Users\-----\Documents\Paradox Interactive\Hearts of Iron IV\mod\rule-brittania\map\provinces.bmp"
output = r"C:\Users\-----\eoa\onactions.txt"

state_sizes = {}
provinces = []
province_colors = {}

def get_prov_colors(defs):
	for line in defs.readlines():
		if "land" in line:
			vals = line.split(";")
			provinces.append(int(vals[0]))
			province_colors[(int(vals[1]), int(vals[2]), int(vals[3]))] = int(vals[0])
		else:
			vals = line.split(";")
			provinces.append(int(vals[0]))

with open(defs, "r") as f:
	get_prov_colors(f)

provs_image = Image.open(provs)
pixels = provs_image.load()
#print(province_colors)
statesl = provinces.copy()
max_id = 1

def get_prov_states(filepath,file):
	global max_id
	lines = file.readlines()
	for num, line in enumerate(lines):
		if "id=" in line:
			state_id = int("".join(filter(str.isdigit, line)))#
		if "provinces" in line:
			provs = [int(prov) for prov in lines[num+1].split() if prov.isdigit()]
	for num, prov in enumerate(provs):
		statesl[int(prov)] = state_id
	if state_id > max_id:
		max_id = state_id

for path, subdirs, files in os.walk(states):
	for file in files:
		filepath=os.path.join(path,file)
		with open(filepath, "r") as f:
			get_prov_states(filepath,f)

for num, state in enumerate(statesl):
	if state > max_id:
		statesl[num] = 0

#print(statesl)
#print(province_colors)

for state in range(max_id+1):
	state_sizes[state] = 0

start_time = timeit.default_timer()
for i in range(provs_image.size[0]):
	for j in range(provs_image.size[1]):
		try:
			prov_id = province_colors[pixels[i,j]]
			print(i,j)
			state_id = statesl[prov_id]
			state_sizes[state_id] += 1
		except KeyError:
			state_sizes[0] += 1

end_time = timeit.default_timer()
elapsed_time = end_time-start_time
print("Took "+str(round(elapsed_time*1000))+" ms")

def output_on_actions(state_sizes,file):
	for state in state_sizes:
		if state != 0:
			file.write("			"+str(state)+" = { set_variable = { RB_land_area = "+str(state_sizes[state])+" } }\n")

with open(output,"a") as f:
	output_on_actions(state_sizes,f)


