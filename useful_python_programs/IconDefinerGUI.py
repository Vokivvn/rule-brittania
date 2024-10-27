import os
import tkinter
import tkinter.filedialog as filedialog
import string
import timeit

this_path = os.path.realpath(__file__)
last_backslash_ind = this_path.rfind("\\")
this_path_folder = this_path[:last_backslash_ind]
input_folder = this_path_folder
output_folder = this_path_folder

class UI(tkinter.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.run_program = tkinter.Button(self)
		self.run_program["text"] = "Generate icon defs"
		self.run_program["command"] = self.gen_icon_defs
		self.run_program.pack(side="top")
		
		self.filename_label = tkinter.Label(self)
		self.filename_label["text"] = "Filename (normal):"
		self.filename_label.pack(side="top")
		
		self.filename_entry_box = tkinter.Entry(self)
		self.filename_entry_box.insert(0, "icon_defs.txt")
		self.filename_entry_box.pack(side="top")
		
		self.filename_label_2 = tkinter.Label(self)
		self.filename_label_2["text"] = "Filename (shine):"
		self.filename_label_2.pack(side="top")
		
		self.filename_entry_box_2 = tkinter.Entry(self)
		self.filename_entry_box_2.insert(0, "icon_defs_shine.txt")
		self.filename_entry_box_2.pack(side="top")
		
		self.input_label = tkinter.Label(self)
		self.input_label["text"] = "Current input dir: "+input_folder
		self.input_label["justify"] = "center"
		self.input_label["wraplength"] = 250
		self.input_label.pack(side="top")
		
		self.file_select_input = tkinter.Button(self)
		self.file_select_input["text"] = "Select an input folder"
		self.file_select_input["command"] = self.input_filedialog_wrapper
		self.file_select_input.pack(side="top")
		
		self.output_label = tkinter.Label(self)
		self.output_label["text"] = "Current output dir: "+output_folder
		self.output_label["justify"] = "center"
		self.output_label["wraplength"] = 250
		self.output_label.pack(side="top")
		
		self.file_select_output = tkinter.Button(self)
		self.file_select_output["text"] = "Select an output folder"
		self.file_select_output["command"] = self.output_filedialog_wrapper
		self.file_select_output.pack(side="top")
	
	def input_filedialog_wrapper(self):
		global input_folder
		input_folder = filedialog.askdirectory(initialdir=this_path,title="Select Input Folder")
		self.input_label["text"] = "Current input dir: "+input_folder
		self.input_label.pack(side="top")
	
	def output_filedialog_wrapper(self):
		global output_folder
		output_folder = filedialog.askdirectory(initialdir=this_path,title="Select Output Folder")
		self.output_label["text"] = "Current output dir: "+output_folder
		self.output_label.pack(side="top")
		
	def gen_icon_defs(self):
		icon_names = []
		for path, subdirs, files in os.walk(input_folder):
			for file in files:
				icon_names.append(file)
		output = open(os.path.join(output_folder,self.filename_entry_box.get()), "a")
		output_2 = open(os.path.join(output_folder,self.filename_entry_box_2.get()), "a")
		for icon in icon_names:
			output.write("	SpriteType = {\n		name = \"GFX_"+icon[:-4]+"\"\n		texturefile = \"gfx/interface/goals/"+icon+"\"\n	}\n\n")
		for icon in icon_names:
			output_2.write("	SpriteType = {\n		name = \"GFX_"+icon[:-4]+"_shine\"\n		texturefile = \"gfx/interface/goals/"+icon+"\"\n		effectFile = \"gfx/FX/buttonstate.lua\"\n		animation = {\n			animationmaskfile = \"gfx/interface/goals/"+icon+"\"\n			animationtexturefile = \"gfx/interface/goals/shine_overlay.dds\"\n			animationrotation = -90.0\n			animationlooping = no\n			animationtime = 0.75\n			animationdelay = 0\n			animationblendmode = \"add\"\n			animationtype = \"scrolling\"\n			animationrotationoffset = { x = 0.0 y = 0.0 }\n			animationtexturescale = { x = 1.0 y = 1.0 }\n		}\n		\n		animation = {\n			animationmaskfile = \"gfx/interface/goals/"+icon+"\"\n			animationtexturefile = \"gfx/interface/goals/shine_overlay.dds\"\n			animationrotation = 90.0\n			animationlooping = no\n			animationtime = 0.75\n			animationdelay = 0\n			animationblendmode = \"add\"\n			animationtype = \"scrolling\"\n			animationrotationoffset = { x = 0.0 y = 0.0 }\n			animationtexturescale = { x = 1.0 y = 1.0 }\n		}\n		legacy_lazy_load = no\n	}\n\n")

		
		


root = tkinter.Tk()
root.geometry("300x400")
root.title("Icon Definer")
app = UI(master=root)
app.mainloop()