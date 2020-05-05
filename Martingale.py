import streamlit as sl
import numpy as np
import pandas as pd
import random as rand

ROULETTE_VALS = []


cash_balances = []
all_bets = []
bet_index = []

#Sidebar Text
sl.sidebar.header("Martingale Simulation - American Roulette")
sl.sidebar.subheader("How this works : ")
sl.sidebar.text("You'll enter your own betting\nparameters. Once set, an x amount of "
                "\nsimulations will ran and you've be \nprovided with a summary of the results.")

#Sidebar - Retrieve User Inputs
cash_balance = sl.sidebar.number_input("Balance",min_value=1,step=1)
initial_balance = cash_balance
initial_bet = sl.sidebar.number_input("Initial Bet",min_value=1, step=1)
table_min = sl.sidebar.number_input("Table Min",min_value=1, step=1)
table_max = sl.sidebar.number_input("Table Max",min_value=1, step=1)
run_amount = sl.sidebar.number_input("How many hands would you like to play ? ",min_value=1,step=1)
#Need them to select their position - Red or Black
color_chosen = sl.sidebar.text_input("Color")

run_sim = sl.sidebar.button("Run Simulation")
sl.sidebar.text("The simulation is based strictly on\nAmerican Roulette ")



#Simply random select some index between [0,len(roulette)]
def pick_color():
    return rand.randint(0,len(ROULETTE_VALS)-1)


#Rearranges the spot for all elements in the array
def shuffle(arr):
    return np.random.shuffle(arr)

#Add the values inside the roulette array
def generate_roulette():
    for i in range(18):
        ROULETTE_VALS.append("red")
    for i in range(18):
        ROULETTE_VALS.append("black")
    for i in range(2):
        ROULETTE_VALS.append("green")


#Verify & Update Balance
def update(value, curr_bet):
    if(color_chosen == value):
        new_balance = cash_balance + curr_bet
        return new_balance,True

    #The user lost - Decrease their balance
    else:
        new_balance = cash_balance - curr_bet
        return new_balance,False


#This will be called last to display results.
def display_stats(arr_balance,arr_bets,curr_index):
    data = {'Balance':arr_balance,
            'Bet Size':arr_bets}

    df = pd.DataFrame(data,columns=['Balance','Bet Size'])
    sl.line_chart(df)






#Once button is clicked - execute the following:
if(run_sim):
    sl.header("Simulation has commenced")
    #Display user inputs
    sl.subheader("Simulation has commenced for the following data : ")
    sl.text("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sl.text("Your Initial Balance : "+ str(cash_balance))
    sl.text("Initial Bet : "+str(initial_bet))
    sl.text("Min - Max of table : "+str(table_min)+" - "+str(table_max))
    sl.text("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    generate_roulette()

    curr_bet = initial_bet

    for i in range(run_amount):
        if(cash_balance >= 0 and curr_bet <= cash_balance):
            cash_balances.append(cash_balance)
            all_bets.append(curr_bet)
            bet_index.append(i+1)

            #Now the gamble starts
            #Chose a index and set that value to update
            number_chosen = pick_color()
            color_picked = ROULETTE_VALS[number_chosen]
            results = update(color_picked,curr_bet)

            cash_balance = results[0]
            print(str(curr_bet) + " --- " + str(results[1]) + " --- " +str(cash_balance))

            if(results[1]):
                curr_bet = initial_bet
            else:
                if(curr_bet*2 >= table_max ):
                    curr_bet = table_max

                else:
                    curr_bet = curr_bet * 2



        else:
            print("You've ran out of money to continue to double - You need to add more :/ ")
            break



    sl.text("Showing Stastics")

    net_val = cash_balance - initial_balance

    if(cash_balance < initial_balance):
        sl.text("You've lost some money :/ ")
        sl.text("Amount lost : "+str(net_val)+"$")

    else:
        sl.text("You've gained some money ! ")
        sl.text("Amount gained : "+str(net_val)+"$")


    display_stats(cash_balances,all_bets,bet_index)
