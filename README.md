IA Launcher (DOS)
=================

**A DOSBox frontend for the [Internet Archive MS-DOS games
collection](https://archive.org/details/softwarelibrary_msdos_games)**


Forked from https://github.com/rtts/ialauncher

Why I made my own fork: I wanted to make my own modifications, but since I don't play well with others, I prefer to work on my own fork rather than do pull requests to someone else's project.

What modifications are planned:
  1) Make the project compatible with Win XP, because I have a 512mb 32-bit laptop from 2004 that I would like to repurpose into a dedicated game machine. This requires backporting to Python 3.4.4
  2) Minor quality-of-life upgrades, such as better search function and a way to mark and recall favorites.
  3) Create other forks to support other systems such as Atari ST, Amiga, etc.

Why I am well-suited to this project: Decades of professional programming experience, with knowledge of a score of programming languages. I also have a BS in Computer Science.

Why I am ill-suited for this project: I hate the Python programming environment. Not the language itself so much, but everything else about it. Really makes my eyeballs ache anytime I have to struggle to get some random python app working. If I need an app for anything, I always choose apps written in something else, Python is always a last resort. So, it should come as no surprise that my Python skills are noob-level. Also, I am lazy....too lazy to re-write this project from scratch in a proper development environment. 

STATUS
======
 
This project has been backported to work with Python 3.4.4. I have tested the project on 32-bit XP with 512MB RAM, it's working fine. HOWEVER, my laziness and lack of Python skills caused some hacky modifications just to get things running. There is no windows installer, you will have to set things up manually. The next section details what you will need to do to get this puppy up and running in Windows.

I just made a modified version that runs on Android. Tested on RCA Viking 10 Pro running Android 5. Browsing and downloading works, but launching does not. Someday I will have to figure out how to launch to RetroArch DOS core. See INSTRUCTIONS FOR ANDROID section.

INSTRUCTIONS FOR WINDOWS
========================
 * I put the files in C:\ialauncher and develop from there. I had to fiddle with imports to get things to work, so I am not sure if running from a different file path will break things. So you might want to use the same file path just to be safe.
 * Installed python-3.4.4.msi
 * Installed Visual Studio Express 2010. This is only needed to compile the pygame module. I tried using a wheel for pygame instead, but no luck. Remember how I said that Python makes my eyeballs ache? Well, if somebody ever wants to point out a wheel that would work with my chosen system, then let me know, I would love to get rid of VS Express 2010.
 * Install pygame module from the Python Scripts directory. For my system, it was C:\Python34\Scripts>python -m pip install pygame==2.0.0
 * To run the app, open cmd window, navigate to the ialauncher directory, invoke the main file. On my system it looked like this:
  ![image](https://github.com/lazybearsoft/ialauncher-dos/assets/87294543/7599413a-7fcc-41ee-97a8-5b301e722b32)

 * IF you run into an SSL cert verify kind of error, this is what I did to work around: copy the request.py file from the project's urllib folder and overwrite the Python system version (save a copy of the original file somewhere before overwriting, just in case you want to restore it later). On my system it was at C:\Python34\Lib\urllib. This workaround probably makes downloading in Python less secure, so USE AT YOUR OWN RISK!
 
INSTRUCTIONS FOR ANDROID  
========================
 * I put the files in \Downloads\ialauncher on the sdcard and develop from there.
 * Installed Pydroid 3.
 * Installed pygame module from within Pydroid 3.
 * To run the app: In pydroid 3, open the python file named main and then click the button in the lower right to begin execution.
 
