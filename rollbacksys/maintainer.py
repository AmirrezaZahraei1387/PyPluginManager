import dataclasses
import types
import inspect


class Action:
    all_names: list = []

    __name: str = ""
    __parameters_num: int = 0
    __rollback_func: types.FunctionType

    def __init__(self, name: str, rollback_func: types.FunctionType, argument_num: int = None):

        if name in self.all_names:
            raise NameError("Duplicated names forbidden")

        self.__name = name
        self.all_names.append(self.__name)

        if argument_num is not None:
            self.__parameters_num = argument_num
        else:
            self.__parameters_num = len(inspect.signature(rollback_func).parameters)
        self.__rollback_func = rollback_func

    @property
    def name(self):
        return self.__name

    @property
    def parameters_num(self):
        return self.__parameters_num

    @property
    def rollback_func(self):
        return self.__rollback_func

    def __call__(self, *args):
        if len(args) != self.__parameters_num:
            raise ValueError("the number of arguments passed is not equal to what expected")
        print(len(inspect.signature(self.__rollback_func).parameters))
        return self.__rollback_func(*args)


@dataclasses.dataclass
class ActionPass:
    name: str
    parameters: list





