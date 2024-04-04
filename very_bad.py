class VeryBad:  
    def __eq__(self, other):
        return True
    

bbad = VeryBad()
if bbad is None:
    print("bbad is None")
else:
    print("bbad is not None")

if bbad == None:
    print("bbad equals None - VeryBad!")
else:
    print("bbad is not equal to None")

    

