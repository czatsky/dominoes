# Write your code here
from random import choice
full_set = [[2, 5], [1, 2], [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4], [3, 4],
            [1, 5], [0, 4], [2, 6], [3, 3], [1, 1], [1, 4], [1, 3], [2, 3], [4, 5],
            [2, 2], [0, 3],[0, 6], [5, 5], [4, 4], [4, 6], [0, 1], [0, 5], [1, 6],[6, 6]]

stock_pieces = []
for i in range(14):
    i = choice(full_set)
    stock_pieces.append(i)
    full_set.remove(i)
player_pieces = []
for x in range(7):
    x = choice(full_set)
    player_pieces.append(x)
    full_set.remove(x)
computer_pieces = full_set
maxpp = max(player_pieces)
maxcp = max(computer_pieces)
dom_snake = []
if maxcp > maxpp:
    domino_snake = maxcp
    first = 'player'
    computer_pieces.remove(maxcp)
else:
    domino_snake = maxpp
    first = 'computer'
    player_pieces.remove(maxpp)
dom_snake.append(domino_snake)
while True:
    print('======================================================================')
    print('Stock size:',len(stock_pieces))
    # print(computer_pieces)
    if first == 'player':
        print('Computer pieces:',len(computer_pieces),'\n')
        if len(dom_snake) > 6:
            print(*dom_snake[0:3],'...',*dom_snake[-3:], sep="")
            print('')
        else:
            print(*dom_snake, sep="")
            print('')
        print('Your pieces:')
        print('')
        for l in range(len(player_pieces)):
            print(l+1,player_pieces[l],sep=':')
        print('')
        if len(computer_pieces) == 0:
            print('Status: The game is over. The computer won!')
            break
        print("Status: It's your turn to make a move. Enter your command.")
        while True:
            try:
                # while True:
                a = int(input())
                a2 = (abs(a))
                if a > 0:
                    newds = player_pieces[a2 - 1]
                    if (newds[0]) == ((((dom_snake[-1:])[0])[1])):
                        dom_snake.append(newds)
                        player_pieces.remove(newds)
                        # print('what')
                        first = 'computer'
                        break
                    elif (newds[1]) == ((((dom_snake[-1:])[0])[1])):
                        newds = newds[::-1]
                        dom_snake.append(newds)
                        newds = newds[::-1]
                        player_pieces.remove(newds)
                        # print('why')
                        first = 'computer'
                        break
                    else:
                        print('Illegal move. Please try again.')
                        # break
                if a < 0:
                    newds = player_pieces[a2 - 1]
                    if (newds[1]) == ((dom_snake[0])[0]):
                        dom_snake.insert(0, newds)
                        player_pieces.remove(newds)
                        first = 'computer'
                        break
                    elif (newds[0]) == ((dom_snake[0])[0]):
                        newds = newds[::-1]
                        dom_snake.insert(0, newds)
                        newds = newds[::-1]
                        player_pieces.remove(newds)
                        first = 'computer'
                        break
                if a == 0 and len(stock_pieces)>0:
                    newitem = choice(stock_pieces)
                    stock_pieces.remove(newitem)
                    player_pieces.append(newitem)
                    first = 'computer'
                    break
                elif a == 0 and len(stock_pieces) == 0:
                    first = 'computer'
                    break
            except (ValueError,IndexError):
                print('Invalid input. Please try again.')
            # if len(player_pieces) == 0:
            #     print('Status: The game is over. You won!')
            #     break
        # if len(stock_pieces) == 0:
        #     print("Status: The game is over.It's a draw!")
        #     break
    else:
        print('Computer pieces:', len(computer_pieces),'\n')
        if len(dom_snake) > 6:
            print(*dom_snake[0:3], '...', *dom_snake[-3:], sep="")
            print('')
        else:
            print(*dom_snake, sep="")
            print('')
        print('Your pieces:')
        print('')
        for l in range(len(player_pieces)):
            ind = l+1
            print(ind,player_pieces[l],sep=':')
        if len(player_pieces) == 0:
            print('Status: The game is over. You won!')
            break
        print('')
        print("Status: Computer is about to make a move. Press Enter to continue...")
        # print('>')
        b = input()
        # print(computer_pieces)
        while True:
            cpstr = str(computer_pieces)
            dsstr = str(dom_snake)
            all = cpstr+dsstr
            counting = {}
            counting['0'] = all.count('0')
            counting['1'] = all.count('1')
            counting['2'] = all.count('2')
            counting['3'] = all.count('3')
            counting['4'] = all.count('4')
            counting['5'] = all.count('5')
            counting['6'] = all.count('6')
            znachi = []
            for key, value in counting.items():
                znachi.append(value)
            scores = []
            for i in computer_pieces:
                scores.append(znachi[i[0]]+znachi[i[1]])
            # print(scores)
            ind = scores.index(max(scores))
            while True:
                # maxi = max(scores)
                ind = scores.index(max(scores))
                if (computer_pieces[ind])[0] == ((((dom_snake[-1:])[0])[1])):
                    dom_snake.append(computer_pieces[ind])
                    computer_pieces.remove(computer_pieces[ind])
                    # print('1')
                    first = 'player'
                    break
                elif (computer_pieces[ind][1]) == ((((dom_snake[-1:])[0])[1])):
                    item = computer_pieces[ind][::-1]
                    dom_snake.append(item)
                    item = item[::-1]
                    computer_pieces.remove(item)
                    first = 'player'
                    # print('2')
                    break
                elif (computer_pieces[ind][0]) == ((dom_snake[0])[0]):
                    item = computer_pieces[ind][::-1]
                    dom_snake.insert(0, item)
                    item = item[::-1]
                    computer_pieces.remove(item)
                    first = 'player'
                    # print('3')
                    break
                elif (computer_pieces[ind][1]) == ((dom_snake[0])[0]):
                    dom_snake.insert(0, computer_pieces[ind])
                    computer_pieces.remove(computer_pieces[ind])
                    first = 'player'
                    # print('4')
                    break
                # elif len(set(scores)) == 1 and 0 in (set(scores)):
                elif max(scores) == 0:
                    # print('ono?')
                    checking = set()
                    for q in computer_pieces:
                        if q[0] == ((((dom_snake[-1:])[0])[1])) or q[1] == ((((dom_snake[-1:])[0])[1])) or q[0] == (
                        (dom_snake[0])[0]) or q[1] == ((dom_snake[0])[0]):
                            checking.add(1)
                            break
                        else:
                            pass
                    if len(stock_pieces) == 0 and len(checking) == 0:
                        print("Status: The game is over.It's a draw!")
                        exit()
                        break
                    if len(checking) == 0 and len(stock_pieces) > 0:
                        newitem2 = choice(stock_pieces)
                        stock_pieces.remove(newitem2)
                        computer_pieces.append(newitem2)
                        first = 'player'
                        break
                    else:
                        checking.clear()
                    rand = choice(computer_pieces)
                    if (rand[0]) == ((((dom_snake[-1:])[0])[1])):
                        dom_snake.append(rand)
                        computer_pieces.remove(rand)
                        first = 'player'
                        break
                    elif (rand[1]) == ((((dom_snake[-1:])[0])[1])):
                        rand = rand[::-1]
                        dom_snake.append(rand)
                        rand = rand[::-1]
                        computer_pieces.remove(rand)
                        first = 'player'
                        break
                    elif (rand[0]) == ((dom_snake[0])[0]):
                        rand = rand[::-1]
                        dom_snake.insert(0, rand)
                        rand = rand[::-1]
                        computer_pieces.remove(rand)
                        first = 'player'
                        break
                    elif (rand[1]) == ((dom_snake[0])[0]):
                        dom_snake.insert(0, rand)
                        computer_pieces.remove(rand)
                        first = 'player'
                        break
                    break
                else:
                    scores[ind] = 0
                    # print(scores)
            znachi.clear()
            scores.clear()
            break
