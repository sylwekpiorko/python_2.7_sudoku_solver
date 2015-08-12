# input data
sudoku = "..5..79...2..9..4.3..8....66.....4...7.....3...8.....28....2..3.6..7..9...45....."

def sudoku_grid(data):
    for i in range(len(data)+1):
        print data[i-1],
        if i % 27 == 0: 
            print "\n- - - + - - - + - - -"
            
        elif i % 9== 0:
            print "\n"
            
        elif i % 3 == 0:
            print "|",
        
        
    return "Done"
    
print sudoku_grid(sudoku)

