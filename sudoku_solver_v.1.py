# input data

# I propose to change "sudoku" var to input_list_of_digits
input_list_of_digits = "..5..79...2..9..4.3..8....66.....4...7.....3...8.....28....2..3.6..7..9...45....."

print "Number of sudoku elements: %d" % len(sudoku)

def sudoku_grid(data):
    for i in range(len(data)):
        
        #print "%d>" % i,
        print data[i], 
        
        if (i+1) % 9 == 0 and i > 0:
            print
        if (i+1) % 3 == 0 and i > 0 and not (i+1) % 9 == 0:
            print "|",
        if (i+1) % 27 == 0 and i > 0 and i < 80: 
            print "- - - + - - - + - - -"
# As far as I read on the internet there always has to be something returned in a definition otherwise we get "None" if there is no return at all. So I'd say we go for "return ''" in my opinon
    return ""

# When you add "," at the end of "print" statement there is no extra line
#print sudoku_grid(input_list_of_digits),

# function to refer to a field as row/column index e.g. field 0 is A1, field 1 is A2 etc.
# Create list of keys e.g. A1, B1 etc.
row_column_list = []
temporary_string = ""
def create_row_column_index(data):
    for i in range(len(data)):
        #print row/column index that depends on position in "data"
        # every row is letter based (A-I), every column is number based (1-9)
        if i < 9:
            temporary_string = "A" + str(i + 1)
            row_column_list.append(temporary_string)
        if i >8 and i < 18:
            temporary_string = "B" + str(i - 8)
            row_column_list.append(temporary_string)
        if i >17 and i < 27:
            temporary_string = "C" + str(i - 17)
            row_column_list.append(temporary_string)
        if i >26 and i < 36:
            temporary_string = "D" + str(i - 26)
            row_column_list.append(temporary_string)
        if i >35 and i < 45:
            temporary_string = "E" + str(i - 35)
            row_column_list.append(temporary_string)
        if i >44 and i < 54:
            temporary_string = "F" + str(i - 44)
            row_column_list.append(temporary_string)
        if i >53 and i < 63:
            temporary_string = "G" + str(i - 53)
            row_column_list.append(temporary_string)
        if i >62 and i < 72:
            temporary_string = "H" + str(i - 62)
            row_column_list.append(temporary_string)
        if i >71 and i < 81:
            temporary_string = "I" + str(i - 71)
            row_column_list.append(temporary_string)
    return row_column_list
#print sudoku_grid(row_column_key_value_list)

# function to add values to indexed positions e.g. A1 becomes A1:. etc.
row_column_key_value_list ={}
def replace_index_with_key_value_list(data):
    for i in range(len(data)): 
        row_column_key_value_list
        #>>> d['mynewkey'] = 'mynewvalue'
        #>>> print d
        #{'mynewkey': 'mynewvalue', 'key': 'value'}
        #data.update({'a':1})
        row_column_key_value_list.update({row_column_list[i]:input_list_of_digits[i]})
        #row_column_key_value_list[row_column_list[i]] = input_list_of_digits[i]
    return row_column_key_value_list

replace_index_with_key_value_list(create_row_column_index(input_list_of_digits))
#for i in range(len(row_column_key_value_list)):
#    print row_column_key_value_list.itervalues().next(),

# print key/value pairs in sudoku matrix function
def sudoku_matrix_key_value(data):
    for i in range(len(data)):
    #for key, value in data.iteritems():  
        #print "%d>" % i,
        #print data[i], 
        print key, ":", value,
        
        if (i+1) % 9 == 0 and i > 0:
            print
        if (i+1) % 3 == 0 and i > 0 and not (i+1) % 9 == 0:
            print "|",
        if (i+1) % 27 == 0 and i > 0 and i < 80: 
            print "- - - + - - - + - - -"
    return ""

print sudoku_matrix_key_value(row_column_key_value_list)
#print range(len(row_column_key_value_list))
# validation test 

# check if a digit not duplicated in a square (3*3)



# list all squares

#square_top_lef = input_list_of_digits[0]
#print square_top_lef

#print replace_digits_with_row_column_index(input_list_of_digits),
