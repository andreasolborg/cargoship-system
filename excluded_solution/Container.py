import random, string

class Container:
    def __init__(self, code, length, empty_weight, max_load, current_load=0):
        self.code = code
        self.length = length
        self.empty_weight = empty_weight
        self.max_load = max_load
        self.current_load = current_load

    def set_current_load(self, new_load):
        self.current_load = new_load

    def get_current_load(self):
        return self.current_load

    def get_max_load(self):
        return self.max_load
    
    def get_empty_weight(self):
        return self.empty_weight
    
    def get_length(self):
        return self.length
    
    def get_code(self):
        return self.code
    
    def __str__(self):
        return "Container: " + self.code + ", length: " + str(self.length) + ", empty weight: " + str(self.empty_weight) + ", max load: " + str(self.max_load) + ", current load: " + str(self.current_load)
        

def generate_container(code_length, load_range, length_range):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=code_length))
    length = random.randint(*length_range)
    empty_weight = 2 if length == 20 else 4
    max_load = 20 if length == 20 else 22
    current_load = random.randint(*load_range)
    return Container(code, length, empty_weight, max_load, current_load)
