import os
from colorama import init, Fore
init()

def s(num):
    r = ""
    for i in range(0,num+1):
        r += " "
    return r

current_dir = os.getcwd()
print(u"\u2554" + s(len(current_dir)) + u" \u2557\n" 
    + s(1) + current_dir 
    + u"\n\u255a" + s(len(current_dir)) + u" \u255d")
tree = Fore.LIGHTCYAN_EX + u"\u2550\u2550\u2550\u2566\n"

MAX_DEPTH = 3
EXCLUSIONS = ["node_modules", ".git", ".vscode", ".idea"]

class File():

    def __init__(self, path, name, typ):
        self.path = path
        self.name = name
        self.typ = typ
    
    def __repr__(self):
        return "{}/{} ({})".format(self.path, self.name, self.typ)

def expand_dir(dir):
    f=[]
    for file in os.listdir(dir):
        t = "file"
        if os.path.isdir(os.path.join(dir, file)):
            t = "dir"
        f.insert(-1, File(dir,file,t))
    return f

def tab(num):
    global tree
    for i in range(0,1):
        tree += "   "
    if num > 0:
        tree += Fore.LIGHTCYAN_EX + u"\u2563"
    for i in range(0,num):
        tree += "   "

def add_file(file, level):
    global tree
    colour = Fore.LIGHTGREEN_EX
    if level is 0:
        colour = Fore.LIGHTCYAN_EX
    tab(level)
    if level is 0:
        tree += colour + u"\u2560"
    tree += colour + u"\u2023"
    tree += colour + " {}\n".format(file.name) # u00d7 => ×

def build_tree(start, base_depth):
    global tree
    global MAX_DEPTH
    global EXCLUSIONS

    base = expand_dir(start)
    for f in base:
        level = len(f.path.split(os.sep)) - base_depth
        if level < MAX_DEPTH:
            add_file(f, level)
            if f.typ == "dir" and f.name not in EXCLUSIONS:
                build_tree(os.path.join(f.path,f.name), base_depth)

build_tree(os.getcwd(), len(os.getcwd().split("/")))
tree += Fore.LIGHTCYAN_EX + u"\u2550\u2550\u2550\u2569"
print(tree)