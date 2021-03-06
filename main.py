# for git development repo
from taskcontrol.workflow import workflow, Tasks

# for package
# from taskcontrol.workflow import workflow, Tasks


# Instance of tasks and apis object
# Every instance will store it own list of tasks
#       with their before/after middlewares
sparrow = Tasks()


def nesttree(ctx, result, k, c, d, **kwargs):
    print("Running my Middleware Function: nesttree - task items", k, c, d, kwargs)
    return k, c, d


@workflow(
    name="taskname",
    task_order=1,
    task_instance=sparrow,
    shared=False,
    # TODO: Add authentication
    # authenticated=True,
    args=[1, 2],
    kwargs={},
    before=[
        # before middleware order followed will be of the list sequence
        {
            "function": nesttree,
            # TODO: Add authentication
            # authenticated=True,
            "args": [11, 12],
            "kwargs": {"d": "Before Testing message Middleware "},

            # options { error : str,  error_next_value: Object, error_handler: function }
            #
            # error { str }: [next, error_handler, exit]
            # error_handler { function }
            # error_next_value { object }
            #
            # Usage:
            # "options": {"error": "next", "error_next_value": "value"}
            # "options": {"error": "exit"}
            # "options": {
            #    "error": "error_handler", error_handler: func, "error_next_value": "value"
            #    }

            "options": {"error": "next", "error_next_value": ""}
        }
    ],
    after=[
        # after middleware order followed will be of the list sequence
        {
            "function": nesttree,
            # TODO: Add authentication
            # authenticated=True,
            "args": [13, 14],
            "kwargs": {"d": "After Middleware Testing message"},
            "options": {
                "error": "error_handler",
                "error_next_value": "value",

                #
                # Default error_handler implementation used internally, if no
                #           error_handler is provided
                #
                # Implementation One:
                #   if error_next_value defined
                #       lambda err, value: (err, error_next_value)
                # Implementation Two:
                #   if error_next_value not defined
                #       lambda err, value: (err, None)
                #
                # Returning the two value tuple in error_handler implementation is compulsary
                #       err is the error that occurred
                #       error_next_value is error_next_value provided in options
                #

                "error_handler": lambda err, value: (err, None)
            }
        }
    ],
    log=False
)
def taskone(ctx, result, a, b):
    print("Running my task function: taskone", a, b)


# Example two for decorator usage
@workflow(name="tasktwo",
          task_instance=sparrow,
          task_order=2,
          shared=False,
          args=[1, 2],
          kwargs={},
          # Declare before/after as an list or an object (if single middleware function)
          before={
              "function": nesttree,
              "args": [21, 22],
              "kwargs": {"d": "Before Testing message"},
              "options": {"error": "next", "error_next_value": ""}
          },
          after=[],
          log=False
          )
def tasktwo(ctx, result, a, b):
    print("Running my task function: tasktwo", a, b)
    return a, b


# Example two for decorator usage
@workflow(name="taskthree",
          task_instance=sparrow,
          task_order=2,
          shared=True,
          args=[1, 2],
          kwargs={},
          # Declare before/after as an list or an object (if single middleware function)
          before={
              "function": nesttree,
              "args": [21, 22],
              "kwargs": {"d": "Before Testing message"},
              "options": {"error": "next", "error_next_value": ""}
          },
          after=[],
          log=False
          )
def taskthree(ctx, result, a, b):
    print("Running my task function: taskthree", a, b)
    return a, b


# print(sparrow.get_tasks(task="tasktwo"))

# INVOKE BELOW WHERE NEEDED
# Example: Within some other function

run_0 = sparrow.run(tasks=["taskname", "tasktwo"])
print("run_0 2 Tasks [2I]", run_0)


# # Run all tasks
# # Multiple Workflow Tasks run
run_1 = sparrow.run(tasks=["1"])
print("run_1 2 Tasks [2I]", run_1)
run_2 = sparrow.run(tasks="1")
print("run_2 2 Tasks [2I]", run_2)


# # Run all shared tasks
# # Shared Workflow Tasks run
run_3 = sparrow.run(tasks=["shared:1"])
print("run_3 0 Tasks [1S]", run_3)
run_4 = sparrow.run(tasks="shared:1")
print("run_4 0 Tasks [1S]", run_4)


# # Multiple Workflow Tasks run
run_5 = sparrow.run(tasks=["shared:taskname", "tasktwo"])
# print("sparrow.ctx ", sparrow.ctx)
print("run_5 1 Tasks [1S,1I]", run_5)


# # Run Tasks run with mix of shared
# # Multiple Workflow Tasks run with mix of shared
run_6 = sparrow.run(tasks=["taskname", "tasktwo", "shared:taskname"])
print("run_6 2 Tasks [2I,1S]", run_6)


# # Single Workflow Tasks run
run_7 = sparrow.run(tasks="shared:taskname")
print("run_7 0 Tasks [1S]", run_7)


# # Single Workflow Tasks run
run_8 = sparrow.run(tasks="shared:taskthree")
print("run_8 0 Tasks [1S]", run_8)


# TODO:
# Run Precreated Tasks
# run_9 = sparrow.run(tasks="workflow:workflowname")
# print("run_9", run_9)
