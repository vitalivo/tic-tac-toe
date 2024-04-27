board_size = 3
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw_board():
    '''выводим игровое поле'''
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3],  '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)

def game_step(index, char):
    '''ход игрока'''
    if (index > 9 or index < 1 or board[index - 1] in ('x', 'o')):
        return False
    board[index - 1] = char
    return True

def check_winner():
    '''проверка на выигрыш'''
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]]:
            return board[combination[0]]
    return False

def check_draw():
    '''проверка на ничью'''
    return all(isinstance(space, str) for space in board)

def start_game():
    '''запуск игры'''
    current_player = 'x'
    step = 1
    draw_board()

    while (step < 10):
        index = input('ваш ход ' + current_player + ' Введите номер поля(0 - выход):')
        if (index == '0'):
            break
        if (game_step(int(index), current_player)):
            print('Удачный ход')
            if check_winner():
                print('Победитель: ', current_player)
                break
            elif check_draw():
                print('Ничья!')
                break
            if (current_player == 'x'):
                current_player = 'o'
            else:
                current_player = 'x'
            draw_board()
            step += 1
        else:
            print('Неверный ход! Повторите!')

print('Игра крестики нолики')
start_game()
