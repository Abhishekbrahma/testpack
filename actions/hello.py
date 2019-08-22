import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, message):
        print(message)
        print("working")
        return(True,message)
