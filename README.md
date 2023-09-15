# 0x00. AirBnB clone - The console
![My Image](hbnb/hbnb.png)

## Table of contents

* [Overview](#Overview)
* [Console](#Console)
* [Testing](#Testing)
* [Usage](#Usage)
* [Examples](#Examples)

## Overview

This project is a simplified version of the popular accommodation booking platform, [AirBnB](https://www.airbnb.com/). It allows users to list their properties for rent and search for available accommodations based on their preferences.

This project is the first step towards building our first full application:the **AirBnB clone**.

## Console

The console (command interpreter) is a python script that provides a command-line interface (CLI) to interact with the **AirBnB clone** project. In this project the console will perform the following:
* create a new object
* retrive an object from a file
* do operations on objects
* update attributes of an object
* destroy an object

## Testing

To run the console.py file

In interactive mode

```bash
$ ./console.py
```

In non-interactive mode

```bash
$ echo "help" | ./console.py
```

```bash
$ cat test_help | ./console.py
```

## Usage

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

## Examples
> The commands are displayed in the following format *Command / usage / example with output*

* Create

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

```bash
create <class>

```

```bash
(hbnb) create BaseModel
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)
```

* Show

```bash
show <class> <id>
```

