class CAR:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display_info(model,make,year):
        return f"The details of this car are 'Model':{model},'Make':{make},'Year':{year}"

car1 = CAR.display_info('mazda','Axela',2006)
print(car1)