# rtl_rafcon_lib - Rafcon Install Tutorial

RAFCON (RMC advanced Flow Control) State machines can easily be reused in form of library states. All you have to do for this is telling RAFCON the path to your state machine and give this path a name.

## Start Rafcon
**Important**
- Always update your librarys before you start Rafcon (**rtl_rafcon_lib** and **rtl_rafcon_sm**! 
- Make sure you are working on correct branch, where your state machines are!

1. open a Terminal
2. (optional) activate a virtual enviorment (e.g. for FollowMe)
3. Enter `rafcon` in the Terminal

## Prerequisite for Installing - Important Notes
1. Rafcon with Simulation - Then you need Ubuntu 16.04 with ROS Kinetic
1. If you don't want/need the simulation - Ubuntu 18.04 and/or ROS Melodic is also fine


## Install Rafcon
1. Install [Rafcon](https://github.com/DLR-RM/RAFCON/blob/master/README.rst#installation-preparations) and follow the Instructions 
* Importnat notices
    * If you use a virtual envioremnt don't use *--user* option
    * If you use Anaconda you still have to install it with *pip*

## Configure Rafcon
#### Add this repository as library in RAFCON
1. open `RAFCON`
1. in `LIBRARIES` right-click (the left top pane) 
1. `Add library root`
1. navigate to this repository folder
1. **ATTENTION NOW**  
make sure you put *this exact folder name* (rtl_rafcon_lib) as the  
`Name: insert your mounting key here` --> `Name: rtl_rafcon_lib`  
at the top in the dialog, else things will explode!

#### Enable library recovery mode
1. Open Preferences
1. Go to core config
1. Check *Library_Recovery_Mode*
1. **Important notice** If this is not activated, it can happen that you can't load a state machine anymore if there was a change in a library you used, e.g. if there was an input type change (int to str). If enabled, Rafcon will delete the connection and will print a notify in the 'Debug Console' and can then load the complete state machine.

#### Add visual studio code as externel editor (optional)
It is possible to add external editors in rafcon for programming the states, e.g. visual studio code
1. Open preferences
1. Go to GUI Config
1. Insert `code` into *DEFAULT_EXTERNAL_EDITOR*

   The *code* argument will open the file with visual studio code, when you the user clicks on *open externally*.

## Troubleshooting while installing
During the installation multiple errors can occur. Here are the most common ones:

* *error:  invalid command ’bdist wheel'* - Check [this](https://stackoverflow.com/questions/34819221/why-is-python-setup-py-saying-invalid-command-bdist-wheel-on-travis-ci) out

* *error:  command ’x86-64-linux-gnu-gcc’ failed with exit status 1* 
   
   Install this: `sudo apt-get install python3-dev` (if you use python 3)

   More about this [here](https://stackoverflow.com/questions/26053982/setup-script-exited-with-error-command-x86-64-linux-gnu-gcc-failed-with-exit)

* *ERROR: Could not build wheels for PyGObject which use PEP 517 and cannot be installed directly*

   Try installing this: `sudo apt install libgirepository1.0-de`

* *Required gtk+ version 3.20, current version is 3.X* (While starting Rafcon)

   Do this:
   - `sudo add-apt-repository ppa:gnome3-team/gnome3-staging`
   - `sudo add-apt-repository ppa:gnome3-team/gnome`
   - `sudo apt update`
   - `sudo apt dist-upgrade`

   More infos about this [here](https://askubuntu.com/questions/933010/how-to-upgrade-gtk-3-18-to-3-20-on-ubuntu-16-04)

* *TypeError:  Couldn’t find foreign struct converter for ’cairo.Context*

   Do this: `sudo apt-get install python-gi-cairo`



## Rafcon Documentation
This section highlights the most important documentary about Rafcon, which you should read to get started.

* [Concepts](https://rafcon.readthedocs.io/en/latest/concepts.html) - Read this to understand the concepts of Rafcon, e.g. the states and how data is being transmitted between states.

* [Basic Tutorial](https://rafcon.readthedocs.io/en/latest/tutorials.html#bottles-of-beer-or-how-to-create-a-simple-state-machine-containing-a-loop) - To get to know the basic workflow of Rafcon.

* [ROS Tutorial](https://rafcon.readthedocs.io/en/latest/tutorials.html#starting-the-basic-turtle-demo-state-machine-using-ros) - o get know how a connection can be established between Rafcon and ROS.

* mportant to learn is how to use states as a Library. There is a [Tutorial](https://rafcon.readthedocs.io/en/latest/tutorials.html#how-to-create-and-re-use-a-library-state-machine) but it is not so clear. Try to make a state machine and save it and re-use it again in another state machine as a library. This concept is very important because re-using library's is a key concept of Rafcon.


## Rafcon with Simulation
Todo

---

tw 2019-06-11T11:37
