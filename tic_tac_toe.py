import random

def conditions(string):
    count = 0
    winner = None
    if (string[0] == string[1] == string[2]):
        count += 1
        winner = string[0]
    if (string[3] == string[4] == string[5]):
        count += 1
        winner = string[3]
    if (string[6] == string[7] == string[8]):
        count += 1
        winner = string[6]
    if (string[0] == string[4] == string[8]):
        count += 1
        winner = string[0]
    if (string[0] == string[3] == string[6]):
        count += 1
        winner = string[0]
    if (string[1] == string[4] == string[7]):
        count += 1
        winner = string[1]
    if (string[2] == string[5] == string[8]):
        count += 1
        winner = string[2]
    if (string[2] == string[4] == string[6]):
        count += 1
        winner = string[2]
    if winner == 'X' or winner == 'O':
        return winner
    return None
        
def show(string):
    row1 = "| "+string[0]+" "+string[1]+" "+string[2]+" |"
    row2 = "| "+string[3]+" "+string[4]+" "+string[5]+" |"
    row3 = "| "+string[6]+" "+string[7]+" "+string[8]+" |"
    print("---------")
    print(row1)
    print(row2)
    print(row3)
    print("---------")

def result(string):
    winner = conditions(string)
    if winner != None:
        print("\n"+winner, "wins")
        return True
    elif "_" not in string:
        print("\nDraw")
        return True
    return False


def main():
    while True:
        print("1 for Player vs Player")
        print("2 for Player vs Computer")
        option = input("Enter option : ")
        if option == '1':
            flag = False
            break
        elif option == '2':
            flag = True
            break
        else:
            print("Enter valid option")

    print("\nGame Starts\n")

    string = "_________"
    show(string)
    all_moves = []
    i = 1
    while True:
        if i % 2 == 0:
            if flag == False:
                x, y = input("Enter the coordinates(Player 2) : ").split()
                x = int(x) -1
                y = int(y) -1
            else:
                while True:
                    x = random.randint(1, 3)
                    y = random.randint(1, 3)
                    x = int(x) -1
                    y = int(y) -1
                    if [x, y] in all_moves:
                        continue
                    else:
                        all_moves.append([x, y])
                        break
            move = 'O'
        elif i == 10:
            break
        else:
            x, y = input("Enter the coordinates(Player 1) : ").split()
            x = int(x) -1
            y = int(y) -1
            move = 'X'
            all_moves.append([x, y])
        if 0 <= x < 3 and 0 <= y < 3:
            row1 = [string[0], string[1], string[2]]
            row2 = [string[3], string[4], string[5]]
            row3 = [string[6], string[7], string[8]]
            moves = [row1, row2, row3]
            if moves[x][y] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                new_string = ""
                moves[x][y] = move
                for row in moves:
                    new_string += "".join(row)
                string = new_string
                show(string)
                check = result(string)
                if check:
                    break
            
        elif not (0 <= x < 3 and 0 <= y < 3):
            print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")
        i += 1

main()
        
