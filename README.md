# taskcontrol
    Create named shared / isolated workflow task controls, and run them with respective before/after middlewares


taskcontrol is a python library to create tasks in and based on named workflow controls. It allows middlewares before and after each task. taskcontrol can run single or multiple tasks at a task run invocation.
  
It provides a simple decorator called `workflow` that takes the name, task_instance, task_order, shared, before, after arguments to set up the named workflow controls.

It also provides methods to create a plugin and work with tasks as a module and/or pre-created ordered task list.



# Features

* Create Named task controls (tasks) - instance and isolated
* Allows middlewares before / after each task (data fetch, auth, data save, logging, logout, cleanup, etc)
* Access read-only contexts and results of middlewares/tasks
* Allows Merging two instances of task controls with namespace clash handling
* Run instance, shared, and mix of tasks (individual or all groups)
* In-Development: Allows creating, registering, and using task controls as a plugin



# Installation


##### Command:

    pip3 install taskcontrol


##### Version:

    In Development: 1.2.0 (functional - production ready with most planned features with MVP)
    Current Version: 1.1.0 (functional - not production ready)


##### Package Link:
    
    https://github.com/apprepute/taskcontrol
    https://pypi.org/project/taskcontrol/




# Technical Specifications


##### Requirements:

* Python 3.x
* Any OS supporting Python 3.x


##### Package Dependencies:

* None


##### Quick Demo:

```python



```

##### Note:

Though it may support Python version 2.x. However, it has not been tested in 2.x. The Syntax and Features of the library supports Python version 2.x. Use at your own risk.

    Minor argument order change from 1.1.0 version
    ctx, and result is compulsary argument which are magically provided



# Wiki

* [Getting started](./docs/getting-started.md)
    
    Describes in short the usage of the package

* [taskcontrol `workflow` decorator](./docs/workflow.md)
    
    Describes how to use the taskcontrol workflow decorator in detail

* [taskcontrol `workflow` decorator argument details](./docs/workflow-arguments.md)
    
    Describes in detail the arguments of workflow decorator

* [taskcontrol `workflow` before / after argument declaration](./docs/workflow-middlewares.md)
    
    Describes creating, defining, and running middlewares

* [taskcontrol `workflow` instance and shared tasks argument](./docs/workflow-instance-shared-tasks.md)
    
    Describes creating a instance (isolated task) and an shared task (available to all instances)



##### Crazy Hint:
You can also create a simple workflow without taskcontrol using a simple list or nested list and loop through them using a for/while loop and invoke them during looping



```python


# Loop the lists below and invoke the functions 
lst = ["f1", "f2", "f3"]
nest_lst = [["f1", "f2"], "f3", "f4", ["f5"]]


# Use a reducer if you want to send args to next function like below
def test(a,b):
    print(a,b)
    return {"a":a, "b":b}
def tester(a,b):
    print(a,b)
    return None

kwargs_for_first_function_the_its_returns_or_other_value_for_next_func = {"a":"a", "b":"b"}
ls = [kwargs_for_first_function_the_its_returns_or_other_value_for_next_func, test, tester]
import functools 
def red(kwargs_for_first_then_func, p):
    i = p(kwargs.get("a"), kwargs.get("b"))
    return i
functools.reduce(red, ls)


```

# Todo

* e2e and Unit Tests - Add Tests (Structure of package created - to be cleaned after writing tests)
* Allows creating and registering a set of task controls as a plugin


# Status

* In Development


# License


The MIT License (MIT) - See [LICENSE](./LICENSE) for further details


Copyright © 2020 - till library works:
    Ganesh B <ganeshsurfs@gmail.com>

