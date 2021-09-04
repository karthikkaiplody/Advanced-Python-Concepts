"""
Abstract base classes and abstract methods
"""
# Template of states and events

from abc import ABC, abstractmethod

class State(ABC):

    @abstractmethod
    def in_state(self):
        pass


class HappyState(State):

    def in_state(self):
        print("I am in Happy State")

class SadState(State):

    def in_state(self):
        print("I am in a Sad State")


class Event(ABC):

    @abstractmethod
    def in_event(self):
        pass

class RecvMoney(Event):

    def in_event(self):
        print("I got Money") 

class SpentMoney(Event):

    def in_event(self):
        print("I spent money")



class StateMachine():

    def __init__(self):
        self.currState = HappyState()

    def current_state(self):
        print(self.currState.in_state())

    def recv_event(self, event):
        if isinstance(event, SpentMoney()):
            self.currState = SadState()

        elif isinstance(event, RecvMoney()):
            self.currState = HappyState()


sm = StateMachine()
sm.current_state()
sm.recv_event(SpentMoney())
sm.current_state()

sm.recv_event(RecvMoney())
sm.current_state()

    
