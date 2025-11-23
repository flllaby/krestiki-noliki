import random
import os
from datetime import datetime

def ensure_stats_directory():
    stats_dir = "game_stats"
    if not os.path.exists(stats_dir):
        os.makedirs(stats_dir)
    return stats_dir

def save_game_result(winner, moves_count):
    stats_dir = ensure_stats_directory()
    stats_file = os.path.join(stats_dir, "tic_tac_toe_stats.txt")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(stats_file, "a", encoding="utf-8") as f:
        if winner == "Draw":
            f.write(f"{timestamp} | Ничья | Количество ходов: {moves_count}\n")
        else:
            f.write(f"{timestamp} | Победитель: {winner} | Количество ходов: {moves_count}\n")

def show_statistics():
    stats_dir = ensure_stats_directory()
    stats_file = os.path.join(stats_dir, "tic_tac_toe_stats.txt")
    
    if not os.path.exists(stats_file):
        print("Статистика пока отсутствует.")
        return
    
    print("\n---- СТАТИСТИКА ИГР ----")
    with open(stats_file, "r", encoding="utf-8") as f:
        games = f.readlines()
        if not games:
            print("Статистика пока отсутствует.")
            return
        
        total_games = len(games)
        x_wins = sum(1 for game in games if "Победитель: X" in game)
        o_wins = sum(1 for game in games if "Победитель: O" in game)
        draws = sum(1 for game in games if "Ничья" in game)
        
        print(f"Всего игр: {total_games}")
        print(f"Побед X: {x_wins}")
        print(f"Побед O: {o_wins}")
        print(f"Ничьих: {draws}")
        
        print("\nПоследние 5 игр:")
        for game in games[-5:]:
            print(game.strip())

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
    moves_count = 0
    
    print("--- КРЕСТИКИ-НОЛИКИ ----")
    print("Формат ввода: строка;столбец (например: 1;3 или 2;1)")
    print(f"Первым ходит игрок: {current_player}")
    
    while not game_over:
        print_board(board)

        row, col = get_player_move(current_player, board)
        make_move(board, row, col, current_player)
        moves_count += 1
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Поздравляем! Игрок {current_player} победил! 🎉")
            save_game_result(current_player, moves_count)
            game_over = True

        elif is_board_full(board):
            print_board(board)
            print("🤝 Ничья! Поле полностью заполнено! 🤝")
            save_game_result("Draw", moves_count)
            game_over = True
        
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def show_menu():
    print("\n---=\ГЛАВНОЕ МЕНЮ ---")
    print("1 - Начать новую игру")
    print("2 - Показать статистику")
    print("3 - Выйти из игры")

def main():
    clear_screen()
    print("Добро пожаловать в игру Крестики-Нолики!")
    print("Поле 3x3, формат ввода: строка;столбец (например: 1;3)")

    ensure_stats_directory()
    
    while True:
        show_menu()
        choice = input("Выберите действие (1-3): ").strip()
        
        if choice == '1':
            clear_screen()
            play_game()
        elif choice == '2':
            clear_screen()
            show_statistics()
        elif choice == '3':
            print("\nСпасибо за игру! До свидания!")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()

