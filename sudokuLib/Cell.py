class Cell:
    
    def __init__(self, value):
        if value == 0:
            self.value = [1,2,3,4,5,6,7,8,9]
        else:
            self.value = value
            
    def is_lone_integer(self):
        return isinstance(self.value, int)
    
    def remove_from_possibilities(self, num_removal):
        if num_removal in self.value:
            self.value.remove(num_removal)
            if len(self.value) == 1:
                self.value = self.value[0]
    
    def add_to_list(self, single_numbers, is_single_number):
        if is_single_number:
            single_numbers.append(self.value)
        else:
            for element in self.value:
                single_numbers.append(element)
    
    def contains(self, single_number):
        if type(self.value) is list:
            return single_number in self.value

    def replace_cell(self, single_numbers):
        self.value = single_numbers
        
    def json_element_cell(self, json_block_array):
        json_block_array.append(self.value)