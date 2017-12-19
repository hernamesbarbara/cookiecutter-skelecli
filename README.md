# cookiecutter-skelecli
generate a new python command line app that uses docopt for arg parsing


### usage

Run the cookiecutter command and use the skelecli template to generate 
a command line app project skeleton that uses docopt.

```
$   cookiecutter cookiecutter-skelecli
author_name [Austin Ogilvie]:
project_name []: my_project
project_slug [my_project]: my_slug
command_name [my_slug]: my_command
description [my_project generate a python cli app]: my_description
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 [1]: 1
```

`cd` into your new project. it should immediately be installable via pip like so.

```
$cd my_project/

$   pip3 install .
Processing /Users/hernamesbarbara/Desktop/my_project
Requirement already satisfied: docopt in /usr/local/lib/python3.6/site-packages (from my-project==1.0.0)
Installing collected packages: my-project
  Running setup.py install for my-project ... done
Successfully installed my-project-1.0.0
```

Now you should be able to run your new command from command line. In this example,
I called my command line app `my_project` and it has 1 sub-command called `my_command`

Invoke the CLI without arguments and you'll see the help from docopt.


```
$   cd ~/
$   my_project
Usage:
    my_project my_command
    my_project -h | --help
    my_project --version
```

Invoke the CLI with a valid command to print the arguments. 
In this case there's only 1 command called `my_command`.

```
$   my_project my_command
Hello, world!
You supplied the following options: {
  "--help":false,
  "--version":false,
  "my_command":true
}
```

You can make changes to the template it self here

```
cd ~/.cookiecutters/cookiecutter-skelecli/
```
