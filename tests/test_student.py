from school_schedule.student import Student
# from ..school_schedule.student import Student
# test:
# beyonce = Student("beyonce", "senior", ["PhD in music"])
# print(beyonce)

def test_class_added_to_class_list():
    #Arrange
    beyonce = Student("beyonce", "senior", ["PhD in music"])
    class_name = "PhD in dance"

    #Act
    result = beyonce.add_class(class_name)
    
    #Assert
    assert result == ["PhD in music", "PhD in dance"]