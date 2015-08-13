# input data
sudoku = "..5..79...2..9..4.3..8....66.....4...7.....3...8.....28....2..3.6..7..9...45....."

print len(sudoku)

def sudoku_grid(data):
    for i in range(len(data)):
        
        #print "%d>" % i,
        print data[i-1],    
        
        if i % 9== 0 and i > 0:
            print "\n"
        if i % 3 == 0 and i >0 and not i % 9 == 0:
            print "|",
        if i % 27 == 0 and i > 0: 
            print "- - - + - - - + - - -"
            
    return "Done"
    
print sudoku_grid(sudoku)

