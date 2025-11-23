import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print("\n   1   2   3")
    for i in range(3):
        row = f"{i+1}  "
        for j in range(3):
            row += f" {board[i][j]} "
            if j < 2:
                row += "|"
        print(row)
        if i < 2:
            print("   -----------")

def is_valid_move(board, row, col):
    if 1 <= row <= 3 and 1 <= col <= 3:
        return board[row-1][col-1] == ' '
    return False

def get_player_move(player, board):
    while True:
        try:
            move = input(f"Игрок {player}, введите ваш ход (формат: строка;столбец): ")

            if ';' not in move:
                print("Ошибка! Используйте формат: номер_строки;номер_столбца (например: 1;3)")
                continue

            coordinates = move.split(';')
            if len(coordinates) != 2:
                print("Ошибка! Введите две координаты через точку с запятой")
                continue
            
            row, col = int(coordinates[0]), int(coordinates[1])
            
            if is_valid_move(board, row, col):
                return row-1, col-1
            else:
                print("Неверный ход! Клетка занята или координаты вне диапазона 1-3.")
                
        except ValueError:
            print("Ошибка! Введите числа в формате: номер_строки;номер_столбца")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

def make_move(board, row, col, player):

    board[row][col] = player

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X' if random.choice([True, False]) else 'O'
    game_over = False
    
    print("КРЕСТИКИ-НОЛИКИ")
    print("Формат ввода: строка;столбец (например: 1;3 или 2;1)")
    print(f"Первым ходит игрок: {current_player}")
    
    while not game_over:
        print_board(board)

        row, col = get_player_move(current_player, board)
        make_move(board, row, col, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Поздравляем! Игрок {current_player} победил! 🎉")
            game_over = True

        elif is_board_full(board):
            print_board(board)
            print("🤝 Ничья! Поле полностью заполнено! 🤝")
            game_over = True

        else:
            current_player = 'O' if current_player == 'X' else 'X'

def ask_for_new_game():
    while True:
        choice = input("\nХотите сыграть еще раз? (да/нет): ").lower().strip()
        if choice in ['да', 'д', 'yes', 'y', '1']:
            return True
        elif choice in ['нет', 'н', 'no', 'n', '0']:
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'!")

def main():
    clear_screen()
    print("Добро пожаловать в игру Крестики-Нолики!")
    print("Поле 3x3, формат ввода: строка;столбец (например: 1;3)")
    
    while True:
        play_game()
        
        if not ask_for_new_game():
            print("\nСпасибо за игру! До свидания!")
            break
        else:
            clear_screen()
            print("Начинаем новую игру!")

if __name__ == "__main__":
    main()