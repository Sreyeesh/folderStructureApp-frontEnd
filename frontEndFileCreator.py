import os
import argparse,random, string
import subprocess
import shutil

# Create the argparse argument parser
parser = argparse.ArgumentParser()

# Add the project directory as a command line argument
parser.add_argument("name", type = str)
parser.add_argument("-index",  action="store_true", default=False,help=' use command -index to open up index.html before the folder name fooBar/')
parser.add_argument("-css",  action="store_true", default=False,help=' use command -css to open up style.css before the folder name fooBar/')
parser.add_argument("-js",  action="store_true", default=False,help=' use command -js to open up app.js before the folder name fooBar/')

# Parse the command line arguments
args = parser.parse_args()
# print(args)



# Create the css and js directories if they do not already exist
if not os.path.exists(args.name + "/css"):
    os.makedirs(args.name + "/css")
else:
    print("css directory already exists!")   

if not os.path.exists(args.name + "/js"):
    os.makedirs(args.name + "/js")
else:
        print("js directory already exists!")




#creating the style.css, app.js, if they don already exist
if not os.path.exists(args.name + "/index.html"):
    
else:
    print("index.html file already exists!")        


if not os.path.exists(args.name + "/css/style.css"):
    open(args.name + "/css/style.css","w").close()
else:
    print("style.css file already exists")    

if not os.path.exists(args.name + "/js/app.js"):
    open(args.name +"/js/app.js","w").close()
else:
    print("app.js file already exists!")    

# Open the index.html file if the -e flag is set
if args.index:
    subprocess.run(["code", args.name + "/index.html"])
    print("opening index.html file")

# Open the style.css file if the -css flag is set
if args.css:
    subprocess.run(["code", args.name + "/style.css"])
    print("opening the stylesheet")

# Open the style.css file if the -css flag is set
if args.js:
    subprocess.run(["code", args.name + "/app.js"])
    print("opening the app.js file")