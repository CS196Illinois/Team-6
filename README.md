# team6
An Automotive Engineering Toolkit Powered by Deep Learning


@ branch frontbacklink 
Here you will locate the main program to be run to initialize our project. 
This branch consists of three notable components:

- servermain.py

The file which sets up the server using python program flask. Flask notably maps 
Http requests to python functions which can then execute backend code and then return 
results to the user. 

- templates directory 

Source of html files. Here servermain.py looks for the source of material to be returned 
to a web user.

- static directory 

Source of all CSS JS and other files which append you HTML templates. Fundamentally all which is 
not directly accessed by the python server code. 


NOTE: due to this organizational format, it would be desirable of frontend to commit their new work
into the proper directory as specified in this branch, as it would be redundant to repeatedly relocate 
files between branches and directories without any significant editing. Nontheless, there do exist a few 
modifications which must be taken upon to html files such that they are accessible to flask. One such is 
changing the url_source when referencing static files, for which examples may be found in the index.html 
file in templates.
