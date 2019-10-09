import os

current_dir = "."
tree = ""
MAX_DEPTH = 2
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
    for i in range(0,3):
        tree += "  "
    if num > 0:
        tree += u"\u01c1"
    for i in range(0,num):
        tree += "  "

def add_file(file, level):
    global tree
    tab(level)
    tree += u"\u01c1`\u00d7 {}\n".format(file.name) # u00d7 => ×

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
print(tree)