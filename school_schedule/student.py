class Student:
    """ 
    How I'm approaching a problem before tackling code:
    attributes: 
        - name: str
        - grade: str
        - classes: list
    methods: 
        - add_class, param - str
        - get_num_classes
        - summary
        - pretty_print_each_class()

    """
    #make a Constructor
    #self represents the class and the instance of the class
    #if we make a default parameter with classes = [] and then add a class like claire.add_classes("Jazzercise")
    #Jazzercise will add to both claire and quinn's classes list. Instead we should set classes = None.
    def __init__(self, name, grade, classes=None):
        self.name = name
        self.grade = grade
        self.classes = classes if classes else []
    #dunder override - this is a dunder str(has to return because it is dunder)- asserts over dunder init
    def __str__(self):
        return(f"Student {self.name}, {self.grade}, {self.classes}")
    
    def greeting(self):
        print("Hi")
        self.compliment()

    def compliment(self):
        print("Wow")
    
    def add_class(self, class_name):
        self.classes.append(class_name)
        return self.classes
    
    def get_num_classes(self):
        return len(self.classes)

    #returns the string
    def summary(self):
        self.display_each_class()
        return self.__str__()


    def display_each_class(self):
        for name in self.classes:
            print(name)
