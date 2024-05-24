import math
import random

def start_game():
  money = 0
  mpc = 1
  mpcPrice = 10
  bonusMoney = 0
  bmUpgradeTxT = "1-Buy Bonus Money $1k"
  bmUpgradePrice = 100
  loans = 0
  newLoanAmount = 0
  interest = 1
  choice = ''
  while True:
    if loans > 0:
      money -= round((loans / 100) * interest)
    
    print("|-------Stats-------|")
    print("$"+str(money))
    print("$PerClick : $"+str(mpc))
    print("$PC Price : $"+str(mpcPrice))
    print("5 for more options")
    print("9 for information")
  
    choice = input()

    if choice == '':
      money += mpc
      print("+"+str(mpc))
      getBonus = round(random.random())
      if getBonus == 1:
        money += bonusMoney
        print("+$" + str(bonusMoney)+" From Bonus Money")
      
    if choice == '1':
      if money >= mpcPrice:
        money -= mpcPrice
        mpc *= 2
        mpcPrice = round(mpcPrice * 2.5)
        print("$PC Upgraded")
    if choice == '5':
      print("|--Pick An Option--|")
      print("1 - Special Shop")
      print("2 - Lottery Shop")
      print("3 - Intrusive Events")
      print("4 - Bank")
      print("EXE to go back")
  
      choice = input()

      if choice == '1':
        print("|-Special Upgrades-|")
        if bonusMoney == 0:
          print(bmUpgradeTxT)
        else:
          print(bmUpgradeTxT + str(bmUpgradePrice))
        print("Current BM: $" + str(bonusMoney))
        print("")
        print("")
        print("EXE to go to Stats")
  
        choice = input()

        if choice == '1' and bonusMoney == 0:
          if money >= 1000:
            print("Bought the bonus $PC upgrade")
            money -= 1000
            bonusMoney += 10
            bmUpgradeTxT = "1-Upgrade BM $"
        elif choice == '1':
          if money >= bmUpgradePrice:
            money -= bmUpgradePrice
            bonusMoney = round(bonusMoney * 2)
            bmUpgradePrice = round(bmUpgradePrice * 2.75)
      if choice == '2':
        money = lottery_shop(money)
      if choice == '3':
        money = intrusive_events(money)
      if choice == '4':
        print("|---Bank Options---|")
        print("1 - Get a loan")
        print("2 - Pay off a laon")
        print("")
        print("")
        print("EXE to go back")

        choice = input()

        if choice == '1':
          newLoanAmount = get_a_loan(newLoanAmount)
          money += newLoanAmount
          loans += newLoanAmount
          newLoanAmount = 0
        if choice == '2' and loans > 0:
          newLoanAmount = pay_off_a_loan(newLoanAmount, money, loans)
          money += newLoanAmount
          loans += newLoanAmount
          newLoanAmount = 0
    if choice == '9':
      display_second_page()

def display_second_page():
  print("|-----Info Menu-----|")
  print("1 - Controls")
  print("2 - Changelog")
  print("3 - Credits")
  print("4 - License N Ver")
  print("EXE to go back")

  choice = input()

  if choice == '1':
    print("|-----Controls-----|")
    print("EXE to gain money")
    print("-Only works in Stats")
    print("1 to upgrade $PC")
    print("")
    print("EXE to go to Stats")
    
    choice = input()

  if choice == '2':
    print("|----ChangeLog----|")
    print("1 - Version 1.0")
    print("2 - Version 1.1")
    print("")
    print("")
    print("EXE to go to Stats")
    
    choice = input()

    if choice == '1':
      print("|----Version 1.0----|")
      print("The base game has")
      print("been made in a")
      print("little over an hour")
      print("")
      print("EXE to go to Stats")
    
      choice = input()
    if choice == '2':
      print("|----Version 1.1----|")
      print("Introduced:")
      print("The Lottery Shop")
      print("Intrusive Events")
      print("9 for Next Page")
      print("EXE to go to Stats")
    
      choice = input()
      if choice == '9':
        print("|----Version 1.1----|")
        print("The Changelog")
        print("The Credits")
        print("License N Ver Screen")
        print("9 for Next Page")
        print("EXE to go to Stats")
        
        choice = input()
        if choice == '9':
          print("|----Version 1.1----|")
          print("The Bank")
          print("Fixed:")
          print("Some text overflow")
          print("9 for Next Page")
          print("EXE to go to Stats")
    
          choice = input()
          if choice == '9':
            print("|----Version 1.1----|")
            print("You can see your BM")
            print("In the Special Shop")
            print("-L bozo can't go to")
            print("the previous page XD")
            print("EXE to go to Stats")
    
            choice = input()

  if choice == '3':
    print("|------Credits------|")
    print("Made by Endper")
    print("-Testers-")
    print("Nathan Li")
    print("")
    print("EXE to go to Stats")
    
    choice = input()

  if choice == '4':
    print("|---License N Ver---|")
    print("Version 1.1")
    print("")
    print("2024 - Python Clicker")
    print("@All Rights Reserved")
    print("EXE to go back")
    
    choice = input()

def lottery_shop(money):
  print("|----Lottery Shop----|")
  print("1 - 1K Ticket-$100")
  print("2 - 1M Ticket-$100K")
  print("3 - 1B Ticket-$100M")
  print("4 - 1T Ticket-$100B")
  print("EXE to go back")

  choice = input()

  chance = round(random.randint(0, 10))
  if choice == '1' and money >= 100:
    if chance == 1:
      print("|-----!YOU WON!-----|")
      print("You won $1,000")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")

      money += 900

      choice = input()
    else:
      print("|-----!YOU LOST!-----|")
      print("You lost $100")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")

      money -= 100

      choice = input()
  if choice == '2' and money >= 100000:
    if chance == 1:
      print("|-----!YOU WON!-----|")
      print("You won $1,000,000")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")

      money += 900000

      choice = input()
    else:
      print("|-----!YOU LOST!-----|")
      print("You lost $100,000")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")

      money -= 100000

      choice = input()
  if choice == '3' and money >= 100000000:
    if chance == 1:
      print("|-----!YOU WON!-----|")
      print("You won")
      print("$1,000,000,000")
      print("")
      print("")
      print("EXE to go to Stats")

      money += 900000000

      choice = input()
    else:
      print("|-----!YOU LOST!-----|")
      print("You lost")
      print("$100,000,000")
      print("")
      print("")
      print("EXE to go to Stats")

      money -= 100000000

      choice = input()
  if choice == '4' and money >= 100000000000:
    if chance == 1:
      print("|-----!YOU WON!-----|")
      print("You won")
      print("$1,000,000,000,000")
      print("")
      print("")
      print("EXE to go to Stats")

      money += 900000000000

      choice = input()
    else:
      print("|-----!YOU LOST!-----|")
      print("You lost")
      print("$100,000,000,000")
      print("")
      print("")
      print("EXE to go to Stats")

      money -= 100000000000

      choice = input()
      
  return money

def intrusive_events(money):
  print("|-Intrusive Events-|")
  print("1 - Rob a bank O_O")
  print("2 - Go on a heist =0")
  print("")
  print("")
  print("EXE to go to Stats")

  choice = input()

  if choice == '1':
    money = rob_a_bank(money)
  if choice == '2':
    money = plan_a_heist(money)
  
  return money

def rob_a_bank(money):
  print("|--Rob a bank O_O--|")
  print("1-$1M Bank - $10K")
  print("2-$10M Bank - $100K")
  print("3-$100M Bank - $1M")
  print("4-$1B Bank - $10M")
  print("EXE to go to Stats")

  choice = input()

  if choice != "":
    bankCost = 100
    for x in range(0, (int(choice) + 1)):
      bankCost *= 10

    chance = round(random.randint(0, 10))

    if money >= bankCost:
      print("You spent")
      print("$"+str(bankCost))
      print("To rob a bank")
      money -= bankCost
      if chance == 1:
        money += (bankCost * 100)
        print("-YOU ROBBED IT-")
        print("You got $"+str(bankCost * 100))
        print("From the bank")
      else:
        money -= (bankCost * 500)
        print("-YOU GOT CAUGHT-")
        print("You lost")
        print("$"+str(bankCost * 500))

      choice = input()
    
  return money
def plan_a_heist(money):
  print("|--Go on a heist =0--|")
  print("1-$1M Heist-$250K")
  print("2-$500M Heist-$125M")
  print("3-$1B Heist-$250M")
  print("4-$500B Heist-$125B")
  print("EXE to go to Stats")

  choice = input()

  if choice != "":
    if choice == '1':
      heistReward = 1000000
      heistCost = 250000
    if choice == '2':
      heistReward = 500000000
      heistCost = 125000000
    if choice == '3':
      heistReward = 1000000000
      heistCost = 250000000
    if choice == '4':
      heistReward = 500000000000
      heistCost = 125000000000
      
      
    chance = heistCost

    if money >= heistCost:
      print("You spent")
      print("$"+str(heistCost))
      print("To go on a heist")
      money -= heistCost
      if chance == 1:
        money += heistReward
        print("-SUCCESS-")
        print("You got $"+str(heistReward))
        print("From the heist")
      else:
        money -= (heistReward * 5)
        print("-FAILED-")
        print("You lost")
        print("$"+str(heistReward * 5))

      choice = input()

  return money
def get_a_loan(newLoanAmount):
  print("|----Get a Loan----|")
  print("1 - Get $1K Loan")
  print("2 - Get $100K Loan")
  print("3 - Get $1M Loan")
  print("4 - More Options")
  print("EXE to go to Stats")

  choice = input()

  if choice == '1':
    newLoanAmount += 1000
    print("|-You Borrowed $1K-|")
    print("")
    print("")
    print("")
    print("")
    print("EXE to go to Stats")
    
    choice = input()
  if choice == '2':
    newLoanAmount += 100000
    print("|You Borrowed $100K|")
    print("")
    print("")
    print("")
    print("")
    print("EXE to go to Stats")

    choice = input()
  if choice == '3':
    newLoanAmount += 1000000
    print("|-You Borrowed $1M-|")
    print("")
    print("")
    print("")
    print("")
    print("EXE to go to Stats")
    
    choice = input()
  if choice == '4':
    print("|----Get a Loan----|")
    print("1 - Get $100M Loan")
    print("2 - Get $1B Loan")
    print("3 - Get $100B Loan")
    print("4 - Get $1T Loan")
    print("EXE to go to Stats")

    choice = input()
    if choice == '1':
      newLoanAmount += 100000000
      print("|You Borrowed $100M|")
      print("")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")
      
      choice = input()
    if choice == '2':
      newLoanAmount += 1000000000
      print("|-You Borrowed $1B-|")
      print("")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")
      
      choice = input()
    if choice == '3':
      newLoanAmount += 100000000000
      print("|You Borrowed $100B|")
      print("")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")
      
      choice = input()
    if choice == '4':
      newLoanAmount += 1000000000000
      print("|-You Borrowed $1T-|")
      print("")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")
      
      choice = input()
  
  return newLoanAmount
def pay_off_a_loan(newLoanAmount, money, loans):
  print("|--Pay off a Loan--|")
  print("1 - Repay $1K")
  print("2 - Repay $100K")
  print("3 - Repay $1M")
  print("4 - More Options")
  print("EXE to go to Stats")

  choice = input()
  if choice == '1' and money >= 1000 and loans >= 1000:
      newLoanAmount -= 1000
      print("|--You Repaid $1K--|")
      print("")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")

      choice = input()
  if choice == '2' and money >= 100000 and loans >= 100000:
      newLoanAmount -= 100000
      print("|--You Repaid $100K--|")
      print("")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")

      choice = input()
  if choice == '3' and money >= 1000000 and loans >= 1000000:
      newLoanAmount -= 1000000
      print("|--You Repaid $1M--|")
      print("")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")
      
      choice = input()
  if choice == '4':
    print("|--Pay off a Loan--|")
    print("1 - Repay $100M")
    print("2 - Repay $1B")
    print("3 - Repay $100B")
    print("4 - Repay $1T")
    print("EXE to go to Stats")

    choice = input()
    if choice == '1' and money >= 100000000 and loans >= 100000000:
      newLoanAmount -= 100000000
      print("|--You Repaid $100M--|")
      print("")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")
      
      choice = input()
    if choice == '2' and money >= 1000000000 and loans >= 1000000000:
      newLoanAmount -= 1000000000
      print("|--You Repaid $1B--|")
      print("")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")
      
      choice = input()
    if choice == '3' and money >= 100000000000 and loans >= 100000000000:
      newLoanAmount -= 100000000000
      print("|--You Repaid $100B--|")
      print("")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")
      
      choice = input()
    if choice == '4' and money >= 1000000000000 and loans >= 1000000000000:
      newLoanAmount -= 1000000000000
      print("|--You Repaid $1T--|")
      print("")
      print("")
      print("")
      print("")
      print("EXE to go to Stats")
      
      choice = input()
      
  return newLoanAmount

start_game()
