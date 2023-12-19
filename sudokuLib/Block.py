class Block:
    
    def __init__(self, cells):
        self.cells = cells if type(cells) is list else None
        
    def _find_single_numbers(self):
        single_numbers = []
        for cell in self.cells:
            if cell.is_lone_integer():
                cell.add_to_list(single_numbers, True)
        return single_numbers

    def _remove_list_from_whole_row(self, single_numbers):
        for single_number in single_numbers:
            self._remove_number_from_whole_row(single_number)
            
    def _remove_number_from_whole_row(self, single_number):
        for cell in self.cells:
            if not cell.is_lone_integer():
                cell.remove_from_possibilities(single_number)
                
    def first_solver(self):
        single_numbers = self._find_single_numbers()
        self._remove_list_from_whole_row(single_numbers)
    
    def _find_single_number_in_list(self):
        single_number = []
        list_possible_numbers = self.add_possible_numbers_to_list()
        list_possible_numbers.sort()

        if list_possible_numbers and list_possible_numbers[0] != list_possible_numbers[1]:
            single_number.append(list_possible_numbers[0])

        for element in range(1, len(list_possible_numbers)-1):
            if list_possible_numbers[element] != list_possible_numbers[element-1] and list_possible_numbers[element] != list_possible_numbers[element+1]:
                single_number.append(list_possible_numbers[element])

        if list_possible_numbers and list_possible_numbers[-1] != list_possible_numbers[-2]:
            single_number.append(list_possible_numbers[-1])
            
        if single_number:
            for element in single_number:
                self.find_and_set_in_row(element)
                
    def add_possible_numbers_to_list(self):
        possible_numbers = []
        for cell in self.cells:
            if not cell.is_lone_integer():
                cell.add_to_list(possible_numbers, False)
        return possible_numbers
          
    def find_and_set_in_row(self, single_number):
        for element in self.cells:
            if element.contains(single_number):
                element.replace_cell(single_number)
        
    def second_solver(self):
        self._find_single_number_in_list()
        
    def count_cells(self):
        counter = 0
        for cell in self.cells:
            if cell.is_lone_integer():
                counter += 1
        return counter
    
    def is_block_valid(self):
        numbers = []
        for element in self.cells:
            element.add_to_list(numbers, True)
        numbers.sort()
        for number in range(len(numbers)-1):
            if numbers[number] == numbers[number+1]:
                return False
            
    def json_array_block(self):
        json_block_array = []
        for cell in self.cells:
            cell.json_element_cell(json_block_array)
        return json_block_array