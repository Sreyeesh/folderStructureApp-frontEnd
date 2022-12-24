import os
import argparse


# Create the argparse argument parser
parser = argparse.ArgumentParser()

# Add the project directory as a command line argument
parser.add_argument("project_dir", help="the project directory")


# Parse the command line arguments
args = parser.parse_args()

# Create the css and js directories if they do not already exist
if not os.path.exists(args.project_dir + "/css"):
    os.makedirs(args.project_dir + "/css")
else:
    print("css directory already exists!")   


if not os.path.exists(args.project_dir + "/js"):
    os.makedirs(args.project_dir + "/js")
else:
    print("js directory already exists!")

#creating the style.css, app.js, if they don already exist
if not os.path.exists(args.project_dir + "/index.html"):
    with open(args.project_dir + "/index.html", "w") as f:
        f.write("<!DOCTYPE html>")
else:
    print("index.html file already exists!")        


if not os.path.exists(args.project_dir + "/css/style.css"):
    open(args.project_dir + "/css/style.css","w").close()
else:
    print("style.css file already exists")    

if not os.path.exists(args.project_dir + "/js/app.js"):
    open(args.project_dir +"/js/app.js","w").close()
else:
    print("app.js file already exists!")    

