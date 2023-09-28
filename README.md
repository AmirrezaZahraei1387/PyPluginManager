# PyPluginManager

A python powerfully tool for managing application plugins
in a meaning full way.

### Installation

In order to install the PyPluginManager you can easily use the
pip with these shell commands.

For Windows:
```shell
pip install pmlion
```

For Linux:
```shell
python3 -m pip install pmlion
```


### Setting Up a Repository

Repository is the core part of the PyPluginManager, and in order to
set up one we need to do it manually. Go the PyPluginManager package
folder and open a folder called samplefiles, then copy the directory
Sample-Repo to whatever path you would like.


---
**NOTE**

In the repository directory go to folder Config and open config.json, and
double check if the PyPluginVersion is the same with the one installed or not.
---

### Interfaces
Once you established your repository you can start using it with
interfaces. Interfaces are an abstraction of what actually is
happening in the repository making it so much easier to manage your 
plugins. 

### Interface Types

Each interface you use have a special type, and each type 
will disable some features of the Core Interface. This feature
will come in handy when you want to allow access to repository to
someone else, but you want to make sure they will not accidentally 
for example remove a Plugin or even install one.

There are four types of Interfaces available described and
shown here.

| Type         | Description                                                                                             |
|--------------|---------------------------------------------------------------------------------------------------------|
| FullAccessRM | A complete access to whole the repository and operations can be done.                                   |
| LockedRM     | The four main operations including installation, uninstallation, getting db, and loading is disallowed. |
| NoDeleteRM   | An operation that requires or may requires deletion is disallowed.                                      |
| NoReadRM     | Any operations involving loading including loading, and getting db is disallowed.                       |

### Establishing an Interface

In order establish an interface first choose an interface that fulfill
your needs. then import it and initialize your repository with it.

```python
from pypluginmanager import minterfaces

Repo_Inter = minterfaces.FullAccessRM("the repo path here")
```


The above examples demonstrates how to establish a full access interface.
When the repository is accessed the information of the interface including its path, and
its type will be written in a file in repository called config.json.


---
**NOTE**

The little annotation RM at the end each interface type is a short name
for repository manager.
---

### Operations

When you have established your interface, and you already get the
interface object, there are some useful methods that you can use in condition
that those operations are not disallowed by the specific type of interface you 
are using.


| Method             | Description                                                                                        |
|--------------------|----------------------------------------------------------------------------------------------------|
| install(path)      | Installing the plugin in the specified path.                                                       |
| plugin_exist(name) | Return true if the specified plugin exist, false otherwise.                                        |
| uninstall(name)    | Uninstalling the plugin using the given name.                                                      |
| get_plugins()      | Returning the name and version of all installed plugins.                                           |
| load(name)         | Retuning the full path to the plugin.                                                              |
| get_db()           | Returning a read only file object of the file plugins.json which contains all the data of plugins. |
| get_version(name)  | Returning the version of the given plugin.                                                         |

