
input_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

input_data = input_data.splitlines()
rows = len(input_data)
cols = len(input_data[0])

search_word = 'XMAS'

def search_horizontal(word_list, search_word, ind):
    if ind > len(word_list)-len(search_word):
        return 0

    search_words = [search_word, search_word[::-1]]
    if ''.join(word_list[ind:ind+len(search_word)]) in search_words:
        return 1

def search_vertical(word_lists, search_word, ind_x, ind_y):
    if ind_y > len(word_lists)-len(search_word):
        return 0
    search_words = [search_word, search_word[::-1]]
    if ''.join([word_lists[y][ind_x] for y in range(ind_y,ind_y+len(search_word))]) in search_words:
        return 1

print(search_horizontal("MSXMAS", search_word, 2))
print(search_vertical(input_data, search_word, 6, 1))
