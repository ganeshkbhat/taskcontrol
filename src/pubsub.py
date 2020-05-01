# Actions and Hooks Base
# TODO: Create structure


# Inherit shared and logging
class ActionsBase():

    # list of registered actions/events
    actions = []
    # list of actions/events listeners
    action_listeners = []

    def action_state(self):
        pass

    def register_event(self):
        pass

    def register_listener(self):
        pass

    def unregister_listener(self):
        pass

    def message(self):
        pass

    def listen(self):
        pass


# Inherit shared and logging
class HooksBase():

    # list of registered web hooks
    hooks = []
    # list of web hooks listeners
    # check if this is needed
    hook_listeners = []

    def hook_state(self):
        pass

    def run_hook_service(self):
        pass

    def stop_hook_service(self):
        pass

    def register_hook(self):
        pass

    # check if this is needed
    def register_receiver(self):
        pass

    def send(self):
        pass

    def receive(self):
        pass
