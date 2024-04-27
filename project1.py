from lib2to3.pygram import Symbols
import random



MAX_LINES=5
MAX_BET=100
MIN_BET=5
rows=3
cols=3
symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

def check_winnings(columns,lines,bet,values):
    winning=0
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
            else:
                winnning+= values[symbol]*bet
    return winning   



def  get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():#(symbol.item)this gives you keys and values 
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns=[]
    for col in range(cols): 
        column=[]
        current_symmbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symmbols.remove(value)
            column.append(value)

            columns.append(column)

    return columns
 
def print_solt_machine(columns):
    for row in range(len(columns[0])):
        for column in columns:
            for i, column in enumerate(columns):
                if i!=len(columns)-1:
                    print(column[row],end="|")
                else:
                     print(column[row],end=" ")
        print()


def deposit(): ##this funnction stcrture.
    while True: ##loop.
        amount=input("enter the amount$:")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("enter the number greater than zero")
        else:
            print("enter the valid digits")
    return amount


def get_number_of_lines():
    while True:
        lines=input("enter the number of lines to bet on(1-"+str(MAX_LINES)+")+?")
        if lines.isdigit():#this works for string olny wether it is having the digit in the string
            lines=int(lines)#this converte the given string in integre
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("enter  valid number")
        else:
            print("enter the number")
    return lines#

def get_bet():
    while True:
        amount=input("enter the bet:")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET}-${MAX_BET}.")#coverting to string in statments
        else:
            print("enter the number")
    return amount
#The statements after the return() statement are not executed
#return() statement can not be used outside the function.
#The return() statement, like in other programming languages ends the function call and returns the result to the caller. It is a key component in any function or method in a code which includes the return keyword and the value that is to be returned after that.

    
    
    
    
def main():
    balance = deposit()   #function call
    lines= get_number_of_lines()
    bet=get_bet()
    total_bet= bet * lines
    if total_bet > balance:
        print(f"you do not have enough to bet thst amount, your current balance is: ${balance}")
    else:
        print ("low balances")
    print(f"your are betting is ${bet} on ${lines}lines . total bet is equal to:${total_bet}")
    print(lines,balance)
    slots=get_slot_machine_spin(rows,cols,symbol_count)
    print_solt_machine(slots)

main() 