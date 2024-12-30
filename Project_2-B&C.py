"""
Project_2-B&C: Druhý projekt do ENGETO Python akademie - Verze Bulls&Cows

Author: Jan Navrátil
E-mail: navratill.jann@gmail.com
"""

import random
separ = '–' * 50

def welcome():              # Uvítání uživatele a vypsání pravidel hry
    
    print(separ,
      'Hello there!',
      "Let's play Bulls & Cows! Here is how it goes:",
      separ,
      'I have generated a random 4-digit number for you.',
      'Your task is to guess the number - but do not worry, you will get hints along the way!',
      'When you guess a number, you will get a number of Bulls and Cows.',
      'Bulls are correct numbers in correct places;',
      'Cows are correct numbers in wrong places.',
      'Good luck!',
      separ, sep='\n')

def input_control(inp: str) -> bool:            # Kontrola, zda vstup splňuje všechny potřebné podmínky + vypsání jednotlivých chyb vstupu
    unique_num = []
    input_ok = True
    if not inp.isnumeric():                     # Kontrola, že vstup jsou pouze numerismy
        print('Enter only numbers!')
        input_ok = False
    elif len(inp) != 4:                         # Kontrola dodržení délky vstupu
        print('You must enter exactly four digits.')
        input_ok = False
    elif inp[0] == '0':                         # Kontrola, že vstup nezačíná číslicí 0
        print('The first digit cannot be 0!')
        input_ok = False
    else:
        for num in inp:
            if num in unique_num:               # Kontrola, že vstup neobsahuje opakující se číslice
                print('The number must contain unique digits!')
                input_ok = False
                break
            else:
                unique_num.append(num)
    return input_ok

def num_generator(digits: int) -> str:          # Generátor hádaného čísla
    i = 1
    num_str = str()
    while i <= digits:
        gen_num = str(random.randrange(0,10))   
        if gen_num not in num_str:              # Kontrola generování, aby výsledné číslo obsahovalo pouze unikátní číslice
            num_str += gen_num
            i += 1
    return num_str

def bc_counter(gue: str, ans: str):             # Počítadlo 'Bulls and Cows'
    bull_num = 0
    cow_num = 0
    pos = 0
    bull_str = ''
    cow_str = ''
    while pos < len(ans):
        if gue[pos] == ans[pos]:                # Kontrola, dza se jedná o 'Bull' nebo 'Cow'
            bull_num += 1
        elif gue[pos] in ans:
            cow_num += 1
        pos += 1
    bull_str = 'Bull' if bull_num == 1 else 'Bulls'     # Úprava textu na výstupu, aby množné tvary odpovídaly ksutečnému počtu
    cow_str = 'Cow' if cow_num == 1 else 'Cows'
    print(f'There are {bull_num} {bull_str} and {cow_num} {cow_str}.', separ, sep='\n')

def win_condition(gue: str, ans: str) -> bool:  # Kontrola, zda bylo uhádnuto celé hádané číslo
    g_run = True
    if gue == ans:
        print(separ,
              f'Congratulations! {gue} is the correct number!', 
              separ, 
              sep='\n')
        g_run = False
    return g_run
    
welcome()
game_run = True
answer = num_generator(4)
while game_run:
    if not input_control(guess := input('Enter your guess: ')):     # Smyčka běží do té doby, dokud vstup není v pořádku
        continue
    else:
        if (game_run := win_condition(guess, answer)):      # V případě, že číslo nebylo uhodnuto, spustí se funkce očítání 'Bulls and Cows'
            bc_counter(guess, answer)
           


