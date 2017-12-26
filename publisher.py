import os
import pdb

with open('blog/base.html','r+') as fp:
    html_index = fp.read()
    arr = os.listdir("blog/")
    html_index = html_index.replace("{% list_of_posts %}","".join([ "<li><a href='personal_page/blog/%s'>%s</a></li>"%(entry,entry) for entry in arr if entry != 'index.html' and entry != 'base.html']))   
    
    with open('blog/index.html','w+') as fi:
        fi.write(html_index)



