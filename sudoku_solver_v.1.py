# input data
sudoku = "..5..79...2..9..4.3..8....66.....4...7.....3...8.....28....2..3.6..7..9...45....."

print "Number of sudoku elements: %d" % len(sudoku)

def sudoku_grid(data):
    for i in range(len(data)):
        
        #print "%d>" % i,
        print data[i], 
        
        if (i+1) % 9== 0 and i > 0:
            print "\n"
        if (i+1) % 3 == 0 and i >0 and not (i+1) % 9 == 0:
            print "|",
        if (i+1) % 27 == 0 and i > 0 and i < 80: 
            print "- - - + - - - + - - -"
            
    return "Done"
    
print sudoku_grid(sudoku)

