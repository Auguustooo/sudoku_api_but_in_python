from .Cell import Cell
from .Block import Block
from .SudokuInterface import SudokuInterface

import json

class Sudoku(SudokuInterface):       

    def __init__(self, given_array = None):
        self.array = [[None for _ in range(9)] for _ in range(9)]
        self.blocks = [None for _ in range(27)]
        self.cell_array = given_array 

    def _init_cell_array_(self):
        i = 0
        for inner_array in self.cell_array:
            j = 0
            for _ in inner_array:
                self.array[i][j] = Cell(self.cell_array[i][j])
                j += 1
            i += 1
        
    def _read_rows_or_columns(self, cells, is_row, index):
        for element in range(len(self.array)):
            if is_row == True:
                cells.append(self.array[int(index)][element])
            else:
                cells.append(self.array[element][int(index)])
        
    def _add_row_or_column_to_blocks(self, is_row, counter):
        i = 0
        for _ in self.array:
            cells = []
            self._read_rows_or_columns(cells, is_row, i)
            self.blocks[counter] = Block(cells)
            counter += 1
            i += 1
            
    def _read_block(self, cells, i, j):
        row_max = i + 3
        column_max = j + 3
        while i < row_max:
            while j < column_max:
                cells.append(self.array[i][j])
                j += 1
            j -= 3 
            i += 1
    
    def _add_block_to_blocks(self, counter):
        row_number = 0
        column_number = 0
        while row_number <= 9 and column_number <= 6:
            if row_number <= 6:
                cells = []
                self._read_block(cells, row_number, column_number)
                self.blocks[counter] = Block(cells)
                counter += 1
                row_number += 3
            else:
                column_number += 3
                row_number = 0   
        
    def given_array_convert_to_cells(self):
        self._init_cell_array_()
        self._add_row_or_column_to_blocks(True, 0)
        self._add_row_or_column_to_blocks(False, 9)
        self._add_block_to_blocks(18)

    def last_validation(self):
        for block in self.blocks:
            return_value = block.is_block_valid()
            if return_value == False: 
                return False
        
    def solve_sudoku(self):
        solved_cells = 0
        while solved_cells != 243:
            for block in self.blocks:
                block.first_solver()
                block.first_solver()
                block.second_solver()
            for block in self.blocks:
                solved_cells += block.count_cells()
            if solved_cells != 243:
                solved_cells = 0
        
    def solve(self):
        self.solve_sudoku()
        whole_json_array = []
        for i in range(9):
            whole_json_array.append(self.blocks[i].json_array_block())
        json_string = json.dumps(whole_json_array)
        return json_string
        
    def toJSON(self):
        return self.solve()