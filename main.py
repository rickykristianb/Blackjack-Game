from art import logo

import random


# return 1 candom cards
def random_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = random.choice(cards)
    return cards


def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
        # 0 as blackjack
    elif sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        return sum(card_list)
    else:
        return sum(card_list)


def win_lose(user_score, comp_score):
    if user_score == comp_score and user_score > 21:
        return "Player Lose"
    elif user_score == comp_score and user_score <= 21 and user_score != 0 and comp_score != 0:
        return "Draw"
    elif user_score == comp_score and user_score <= 21 and user_score != 0 and comp_score != 0:
        return "Player and Computer have BlackJack, DRAW!!"
    elif user_score == 0:
        return "User Win with BlackJack"
    elif comp_score == 0:
        return "Comp win with BlackJack"
    elif user_score > 21:
        return "You went over, Player Lose"
    elif comp_score > 21:
        return "Computer went over, Player Win"
    elif user_score > comp_score:
        return "Player Win"
    else:
        return "You Lose"


# start play the game
def play_game():
    print(logo)

    user_cards = []
    computer_cards = []

    # Get the first 2 random cards
    for i in range(2):
        user_cards.append(random_cards())
        computer_cards.append(random_cards())

    # Game will continue if user type "y"
    game_over = False
    while not game_over:
        print("Test2")
        user_cards_total = calculate_score(user_cards)
        computer_cards_total = calculate_score(computer_cards)

        print(f"Your cards {user_cards}, with total is {user_cards_total}")
        print(f"Computer first cards is {computer_cards[0]}")

        # user score is blackjack
        if user_cards_total == 0:
            game_over = True
        elif user_cards_total < 21:
            get_another_card = input("Type \"y\" to get another card, type \"n\" to pass: ")
            if get_another_card == "y":
                user_cards.append(random_cards())
            else:
                game_over = True
        else:
            game_over = True

    comp_play = True
    while comp_play:
        if computer_cards_total < 17:
            computer_cards.append(random_cards())
            computer_cards_total = calculate_score(computer_cards)
        else:
            comp_play = False

    print("\nGame Over")
    if user_cards_total == 0:
        print(f"Your cards {user_cards}, with BLACKJACK")
        print(f"Computer cards {computer_cards}, with total is {computer_cards_total}")
        print(win_lose(user_score=user_cards_total, comp_score=computer_cards_total))
    else:
        print(f"Your cards {user_cards}, with total is {user_cards_total}")
        print(f"Computer cards {computer_cards}, with total is {computer_cards_total}")
        print(win_lose(user_score=user_cards_total, comp_score=computer_cards_total))


while input("Do you want to play a game of BlackJack? Type \"y\" or \"n\": ") == "y":
    play_game()