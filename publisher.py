import os
import pdb

def post_preview(file_name,path):
    with open(path+file_name,'r') as fp:
        data = fp.read()
        return "<a href='/personal_page/%s' class='post_preview'>%s...</a>"%(path+file_name,data[:60])

with open('blog/base.html','r+') as fp:
    html_index = fp.read()
    arr = os.listdir("blog/")
    list_previews = "".join([post_preview(entry,'blog/') for entry in arr if
                             entry.find("index")==-1 and
                             entry.find("base")==-1])
    html_index = html_index.replace("{% list_of_posts %}",list_previews)   
    
    with open('blog/index.html','w+') as fi:
        fi.write(html_index)



