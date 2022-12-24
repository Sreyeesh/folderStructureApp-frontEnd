import os

#making directory structure for css and js
if not os.path.exists("project/css"):
    os.makedirs("project/css")
else:
    print("css directory already exists!")    


if not os.path.exists("project/js"):
    os.makedirs("project/js")
else:
    print("js directory already exists!")

#creating the style.css, app.js, if they don already exist
if not os.path.exists("project/css/style.css"):
    with open("project/css/style.css", "w") as f:
        f.write("<!DOCTYPE html>")
else:
    print("index.html directory already exists!")        

if not os.path.exists("project/css/style.css"):
    open("project/css/style.css","w").close()
else:
    print("style.css file already exists")    

if not os.path.exists("project/js/app.js"):
    open("project/js/app.js","w").close()
else:
    print("app.js file already exists!")    

