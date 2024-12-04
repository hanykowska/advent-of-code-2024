import os


input_name = "input_4.txt"
input_path = "inputs/" + input_name
# in macOS or pycharm, ".." is needed to get out of "code" directory,
# in Windows or VSCode, the starting point is the repository directory

file = open(os.path.abspath(input_path), "r")
input_data = file.read()
file.close()

# input_data = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""

input_data = input_data.splitlines()
rows = len(input_data)
cols = len(input_data[0])

search_word = 'XMAS'

def search_horizontal(word_list, search_word, ind):

    search_words = [search_word, search_word[::-1]]
    try:
        if ''.join(word_list[ind:ind+len(search_word)]) in search_words:
            return 1
    except IndexError:
        return 0
    return 0

def search_vertical(word_lists, search_word, ind_x, ind_y):
    search_words = [search_word, search_word[::-1]]
    try:
        if ''.join([word_lists[y][ind_x] for y in range(ind_y,ind_y+len(search_word))]) in search_words:
            return 1
    except IndexError:
        return 0
    return 0
    
def search_diagonal(word_lists, search_word, ind_x, ind_y):
    search_words = [search_word, search_word[::-1]]
    found_word = ''

    try:
        for i in range(len(search_word)):
            found_word += word_lists[ind_y+i][ind_x+i]
        
        if found_word in search_words:
            return 1
    except IndexError:
        return 0
    return 0

def search_diagonal_up(word_lists, search_word, ind_x, ind_y):
    
    search_words = [search_word, search_word[::-1]]
    found_word = ''
    try:
        for i in range(len(search_word)):
            found_word += word_lists[ind_y-i][ind_x+i]
        if found_word in search_words:
            return 1
    except IndexError:
        return 0
    
    return 0
    

# print(search_horizontal("MSXMAS", search_word, 2))
# print(search_vertical(input_data, search_word, 6, 1))
# print(search_diagonal(input_data, search_word, 3, 2))

found_words_total = 0

for y in range(len(input_data)):
    for x in range(len(input_data[0])):
        horizontal = search_horizontal(input_data[y], 
                                              search_word,
                                              x) 
        vertical = search_vertical(input_data,
                                          search_word,
                                          x,
                                          y)
        diagonal = search_diagonal(input_data,
                                          search_word,
                                          x,y)
        diagonal_up = search_diagonal_up(input_data,
                                          search_word,
                                          x,y)
        pass
        found_words_total = found_words_total +\
                            horizontal +\
                            vertical +\
                            diagonal +\
                            diagonal_up
        
print(found_words_total)
