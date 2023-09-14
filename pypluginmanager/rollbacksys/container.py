from pypluginmanager.rollbacksys.maintainer import Action
from pypluginmanager.rollbacksys.maintainer import ActionPass


class ActionCon:

    __actions: dict = {}
    __action_passes: list = []
    __max_action_pass: int

    def get_length(self):
        return len(self.__action_passes)

    def add_action(self, action: Action):
        self.__actions.update({action.name: action})

    def add_action_pass(self, action_path: ActionPass):
        self.__action_passes.append(action_path)

    def clear(self):
        self.__action_passes.clear()

    def rollback(self):
        length = len(self.__action_passes)

        self.__actions[self.__action_passes[length - 1].name]\
            (*self.__action_passes[length - 1].parameters)
        self.__action_passes.pop(length-1)

    def rollbackAll(self):
        length = len(self.__action_passes)
        for i in range(length):
            self.rollback()

