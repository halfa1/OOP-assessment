class Engine:
    def __init__(self):
      pass
    def start(self):
        print('The engine is starting')

    def stop(self):
        print('the engine is stoping')

class Car:
    def __init__(self):
        #showing car has an engine
        self.engine = Engine()

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()


#demonstarating composition
car1 = Car()
car1.start_engine()
car1.stop_engine()