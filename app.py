from flask import Flask, request, jsonify
from sudokuLib.Sudoku import Sudoku

app = Flask(__name__)

json_string = None
@app.route("/")
def start():
    return "It shows something i guess"

@app.route('/insertAndSolveSudoku', methods = ['POST'])
def post_given_sudoku():
    data = request.get_json()
    sudoku = Sudoku(data)
    sudoku.given_array_convert_to_cells()
    global json_string
    json_string = sudoku.toJSON()
    if sudoku.last_validation() == False:
        json_string = None
        return "Sudoku not solvable", 400
    else:
        return json_string
    
@app.route('/solvedSudoku', methods = ['GET'])
def get_sudoku():
    global json_string
    if json_string != None:
        return jsonify(json_string)
    else:
        return "Failed to GET", 400

if(__name__ == "__main__"):
    app.run()
    