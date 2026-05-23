class MyZoo(object):
    def __init__(self, dict=None):
        print("My Zoo!")
        if dict is None:
            self.animal = {}
        else:
            self.animal = dict.copy()

    def __str__(self):
        result = []
        for animal, count in self.animal.items():
            result.append(f"{animal}: {count}")
        return "\n".join(result)

    def __eq__(self, value):
        if isinstance(value, MyZoo):
            return set(self.animal.keys()) == set(value.animal.keys())
        return False

if __name__ == "__main__":
    myzoooo = MyZoo({"pig": 5, "dog": 6})
    print(myzoooo)
    print()
    
    myzoooo2 = MyZoo()
    print(myzoooo2)
   
    zoo1 = MyZoo({"pig": 5, "dog": 6})
    zoo2 = MyZoo({"pig": 3, "dog": 8})  
    zoo3 = MyZoo({"pig": 5, "cat": 6})  

    print(f"zoo1 == zoo2: {zoo1 == zoo2}")  
    print(f"zoo1 == zoo3: {zoo1 == zoo3}")