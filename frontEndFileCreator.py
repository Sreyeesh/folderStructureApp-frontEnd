import os
import shutil

#making directory structure

src = "src"
frontEnd = "www"
js_folder = "js"
css_folder = "css"
backEnd = "server"
parent_dir = "D:\Projects\CodingProjects\personalProjects"

indexFileName = "index.html"
cssFileName = "style.css"
jsFileName = "app.js"

src_path = os.path.join(parent_dir,src)
frontEnd_path = os.path.join(src_path,frontEnd)
js_folder_path = os.path.join(frontEnd_path,js_folder)
css_folder_path = os.path.join(frontEnd_path,css_folder)
backEnd_path = os.path.join(src_path,backEnd)

if not os.path.exists(src_path):
	os.mkdir(src_path)
print("Directory '% s' created" % src_path)
if not os.path.exists(frontEnd_path):
	os.mkdir(frontEnd_path)

if not os.path.exists(js_folder_path):
	os.mkdir(js_folder_path)
if not os.path.exists(css_folder_path):
	os.mkdir(css_folder_path)

if not os.path.exists(backEnd_path):
	os.mkdir(backEnd_path)



#file creation happens after  directories are made 	

indexFileName_path = os.path.join(frontEnd_path, indexFileName)
try:
	with open(indexFileName_path,'w') as html:
		html.write("""!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Document</title>
	</head>
	<body>
	</body>
	</html>""")
	
except:
	print("Folders are already created")	
	# print(file_html)
print('creating,{}!'.format(indexFileName)) # creating index.html

cssFileName_path = os.path.join(css_folder, cssFileName)

try:
	with open(cssFileName_path,'w') as css:
		css.write()
except:
	print("Folders are already created")	
	# print(file_html)
print('creating,{}!'.format(cssFileName)) # creating cssFileName

jsFileName_path = os.path.join(js_folder, jsFileName)
try:
	with open(jsFileName_path ,'w') as js:
		js.write()
except:
	print("Folders are already created")	
	# print(file_html)
print('creating,{}!'.format(cssFileName)) # creating cssFileName


# source = "D:\Projects\CodingProjects\personalProjects\src\www"

# jsSourceFile = "D:\Projects\CodingProjects\personalProjects\src\js"
# cssSourceFile = "D:\Projects\CodingProjects\personalProjects\src\css"

# jsDest = shutil.move(source,jsSourceFile)
# print('moving,{}!',format(jsSourceFile))
# cssDest = shutil.move(source,cssSourceFile)
# print('moving,{}!',format(cssDest))



