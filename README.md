# project
Hey team! I guess the first thing to do now that you are here is to 
make a clone of the project repository. After that, make a branch of that clone. 
This branch is where your changes will be made, which will then be merged in to the master
branch of the project.

Github has spaces for dialogue and advanced collaboration features. We probably won't need most
of them, but feel free to explore and report back if you spot anything you think we could use.
I am by no means a git pro, but we should be able to make this a good code base if we don't 
get too tricky. 

I think Windows has a desktop Git client too, so you may want to check that out.
---
## Running server
#### Requirements
In order to run this DJango server, you will need the following
1. [Python](https://www.python.org/downloads/)
2. Pip(Pre-installed with Python 2 and >)
3. DJango  

#### Running Live server
1. Make sure you are in the root folder of the imdb_search_engine project
	This directory will contain another folder named imdb_search_engine and a file titled "manage.py"
2. Run the following script: _python manage.py runserver_
3. Open web browser and type the following address: **127.0.0.1:8000**
	This should match the address that follows the command line/terminal prompt stating "Starting development server at..."
4. Pressing _CTRL + C_ or _CMD + C_ will result in the server terminating
