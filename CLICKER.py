import random

def print_empty_lines(x):
  for n in range(0, x):
    print("")

def convert_number_to_unit(x):
  if x < 0:
      sign = '-'
      x *= -1
  else:
      sign = ''
  suffixes = ["", "K", "M", "B", "T", "Qa", "Qi"]
  values = {
      "": 0,
      "K": 1_000,
      "M": 1_000_000,
      "B": 1_000_000_000,
      "T": 1_000_000_000_000,
      "Qa": 1_000_000_000_000_000,
      "Qi": 1_000_000_000_000_000_000
  }
  for suffix in suffixes:
    if suffix != "Qi" and suffix != "":
      next_suffix = suffixes[suffixes.index(suffix) + 1 if suffixes.index(suffix) + 1 < len(suffixes) else -1]
      if x >= values[suffix] and x < values[next_suffix]:
        string = sign+str(round(x / values[suffix]))+suffix
        return string
    elif suffix == "Qi":
      if x >= values[suffix]:
        string = sign+str(round(x / values[suffix]))+suffix
        return string
  # Handle the case when x is equal to 0
  return sign+str(x)

def start_game():
  money = 0
  mpc = 1
  mpcPrice = 10
  bonusMoney = 0
  bonusMoneyChance = 10
  bmUpgradeTxT = "1-Buy Bonus Money $1k"
  bmUpgradePrice = 100
  bmChanceUpgradeTxT = "2-Upg BM Chance $"
  bmChanceUpgradePrice = 10000
  thieverySkill = 10
  thieveryPrice = 10000
  heistSkill = 10
  heistPrice = 25000
  loans = 0
  newLoanAmount = 0
  interest = 1
  choice = ''
  while True:
    if loans > 0:
      money -= round((loans / 100) * interest)
    
    print("|-------Stats-------|")
    print("$"+convert_number_to_unit(money))
    print("$PerClick : $"+convert_number_to_unit(mpc))
    print("$PC Price : $"+convert_number_to_unit(mpcPrice))
    print("5 for more options")
    print("9 for information")
  
    choice = input()

    if choice == '':
      money += mpc
      print("+"+convert_number_to_unit(mpc))
      if round(random.randrange(0, bonusMoneyChance)) == 1:
        money += bonusMoney
        print("+$" + convert_number_to_unit(bonusMoney)+" From Bonus Money")
      
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
      print("9 - Next Page")
      print("EXE to go back")
  
      choice = input()

      if choice == '1':
        print("|-Special Upgrades-|")
        if bonusMoney == 0:
          print(bmUpgradeTxT)
        elif bonusMoneyChance > 1:
          print(bmUpgradeTxT + convert_number_to_unit(bmUpgradePrice))
        else:
          print("Upgrade MAXED")
        print("Current BM: $" + convert_number_to_unit(bonusMoney))
        if bonusMoney == 0:
          print_empty_lines(2)
        else:
          print(bmChanceUpgradeTxT + convert_number_to_unit(bmChanceUpgradePrice))
          print("BM Chance: 1/" + convert_number_to_unit(bonusMoneyChance))
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
        elif choice == '2' and bonusMoneyChance > 1:
          if money >= bmChanceUpgradePrice:
            print("Upgraded chance of BM")
            money -= bmChanceUpgradePrice
            bmChanceUpgradePrice = round(bmChanceUpgradePrice * 3)
            bonusMoneyChance -= 1
      elif choice == '2':
        money = lottery_shop(money)
      elif choice == '3':
        money = intrusive_events(money, thieverySkill, heistSkill)
      elif choice == '9':
        print("|--Pick An Option--|")
        print("1 - Bank")
        print("2 - Train Skills")
        print_empty_lines(2)
        print("EXE to go back")

        choice = input()
        
        if choice == '1':
          print("|---Bank Options---|")
          print("1 - Get a loan")
          print("2 - Pay off a loan")
          print_empty_lines(2)
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
        elif choice == '2':
          print("|---Train Skills---|")
          print("1 - Theft Skills")
          print("2 - Heist Skills")
          print_empty_lines(2)
          print("EXE to go back")
          
          choice = input()
          
          if choice == '1':
            print("|---Theft Skills---|")
            if thieverySkill > 1:
               print("1 - Upgrade-$" + convert_number_to_unit(thieveryPrice))
            else:
              print("Upgrade MAXED")
            print("Current Skill-1" + "/" + str(thieverySkill))
            print_empty_lines(2)
            print("EXE to go back")
          
            choice = input()
            if choice == '1' and money >= thieveryPrice and thieverySkill > 1:
              money -= thieveryPrice
              thieveryPrice = round(thieveryPrice * 3.25)
              thieverySkill -= 1
          if choice == '2':
            print("|---Heist Skills---|")
            if heistSkill > 1:
               print("1 - Upgrade-$" + convert_number_to_unit(heistPrice))
            else:
              print("Upgrade MAXED")
            print("Current Skill-1" + "/" + str(heistSkill))
            print_empty_lines(2)
            print("EXE to go back")
          
            choice = input()
            if choice == '1' and money >= heistPrice and heistSkill > 1:
              money -= heistPrice
              heistPrice = round(heistPrice * 3.25)
              heistSkill -= 1
          
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
    print_empty_lines(1)
    print("EXE to go to Stats")
  if choice == '2':
    print("|----ChangeLog----|")
    print("1 - Version 1.0")
    print("2 - Version 1.1")
    print("3 - Version 1.2")
    print_empty_lines(1)
    print("EXE to go to Stats")
    choice = input()
    
    if choice == '1':
      print("|----Version 1.0----|")
      print("The base game has")
      print("been made in a")
      print("little over an hour")
      print_empty_lines(1)
      print("EXE to go to Stats")
    if choice == '2':
      print("|----Version 1.1----|")
      print("Introduced:")
      print("The Lottery Shop")
      print("Intrusive Events")
      print("9 for Next Page")
      print("EXE to go to Stats")
      if input() == '9':
        print("|----Version 1.1----|")
        print("The Changelog")
        print("The Credits")
        print("License N Ver Screen")
        print("9 for Next Page")
        print("EXE to go to Stats")
        if input() == '9':
          print("|----Version 1.1----|")
          print("The Bank")
          print("Fixed:")
          print("Some text overflow")
          print("9 for Next Page")
          print("EXE to go to Stats")
          if input() == '9':
            print("|----Version 1.1----|")
            print("You can see your BM")
            print("In the Special Shop")
            print("-L bozo can't go to")
            print("the previous page XD")
            print("EXE to go to Stats")
    if choice == '3':
      print("|----Version 1.2----|")
      print("Optimized the code")
      print("Heavily")
      print_empty_lines(1)
      print("9 for Next Page")
      print("EXE to go to Stats")
      if input() == '9':
        print("|----Version 1.2----|")
        print("Reduced the price for")
        print("BM upgrade (3->2.75)")
        print_empty_lines(1)
        print("9 for Next Page")
        print("EXE to go to Stats")
        if input() == '9':
          print("|----Version 1.2----|")
          print("The chance of getting")
          print("BM is now upgradeable")
          print_empty_lines(1)
          print("9 for Next Page")
          print("EXE to go to Stats")
          if input() == '9':
            print("|----Version 1.2----|")
            print("There's now an")
            print("Automatic number to")
            print("Unit conversion Sys")
            print("9 for Next Page")
            print("EXE to go to Stats")
            if input() == '9':
              print("|----Version 1.2----|")
              print("You can train your")
              print("Skills for a better")
              print("Luck at doing crimes")
              print("More banks to rob")
              print("EXE to go to Stats")

  if choice == '1' or choice == '2' or choice == '3':
    choice = input()

  if choice == '3':
    print("|------Credits------|")
    print("Made by Endper")
    print("-Testers-")
    print("Nathan Li")
    print_empty_lines(1)
    print("EXE to go to Stats")
    input()

  if choice == '4':
    print("|---License N Ver---|")
    print("Version 1.2")
    print_empty_lines(1)
    print("2024 - Python Clicker")
    print("@All Rights Reserved")
    print("EXE to go back")
    input()

def lottery_shop(money):
  print("|----Lottery Shop----|")
  print("1 - 1K Ticket-$100")
  print("2 - 1M Ticket-$100K")
  print("3 - 1B Ticket-$100M")
  print("4 - 1T Ticket-$100B")
  print("EXE to go back")

  choice = input()

  if choice == "1" or choice == "2" or choice == "3" or choice == "4":
    choice_to_lottery_cost = {
      1: 100,
      2: 100_000,
      3: 100_000_000,
      4: 100_000_000_000,
    }
    lotteryCost = choice_to_lottery_cost.get(int(choice), 0)
    chance = round(random.randint(0, 10))

    if money >= lotteryCost:
      if chance == 1:
        print("|-----!YOU WON!-----|")
        print("You won $" + convert_number_to_unit(lotteryCost * 10))
        print_empty_lines(3)
        print("EXE to go to Stats")
        money += lotteryCost * 9
      else:
        print("|-----!YOU LOST!-----|")
        print("You lost $" + convert_number_to_unit(lotteryCost))
        print_empty_lines(3)
        print("EXE to go to Stats")
        money -= lotteryCost
      choice = input()
  return money

def intrusive_events(money, thieverySkill, heistSkill):
  print("|-Intrusive Events-|")
  print("1 - Rob a bank O_O")
  print("2 - Go on a heist =0")
  print_empty_lines(2)
  print("EXE to go to Stats")

  choice = input()

  if choice == '1':
    money = rob_a_bank(money, thieverySkill)
  elif choice == '2':
    money = plan_a_heist(money, heistSkill)
  
  return money
def calculate_bank_results(money, bankCost, thieverySkill):
  chance = round(random.randint(1, thieverySkill))

  if money >= bankCost:
    print("You spent")
    print("$"+convert_number_to_unit(bankCost))
    print("To rob a bank")
    money -= bankCost
    if chance == 1:
      money += (bankCost * 100)
      print("-YOU ROBBED IT-")
      print("You got $"+convert_number_to_unit(bankCost * 100))
      print("From the bank")
      print_empty_lines(2)
      print("EXE to go to Stats")
    else:
      money -= (bankCost * 500)
      print("-YOU GOT CAUGHT-")
      print("You lost $"+convert_number_to_unit(bankCost * 500))
      print_empty_lines(3)
      print("EXE to go to Stats")
    input()
  return money

def rob_a_bank(money, thieverySkill):
  print("|--Rob a bank O_O--|")
  print("1-$1M Bank - $10K")
  print("2-$10M Bank - $100K")
  print("3-$100M Bank - $1M")
  print("9 for Next Page")
  print("EXE to go to Stats")

  choice = input()

  if choice == '1' or choice == '2' or choice == '3':
    choice_to_bank_cost = {
      1: 10_000,
      2: 100_000,
      3: 1_000_000,
    }
    bankCost = choice_to_bank_cost.get(int(choice), 0)

    money = calculate_bank_results(money, bankCost, thieverySkill)
  elif choice == '9':
    print("|--Rob a bank O_O--|")
    print("1-$1B Bank - $10M")
    print("2-$10B Bank - $100M")
    print("3-$100B Bank - $1B")
    print("4-$1T Bank - $10B")
    print("EXE to go to Stats")

    choice = input()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
      choice_to_bank_cost = {
        1: 10_000_000,
        2: 100_000_000,
        3: 1_000_000_000,
        4: 10_000_000_000,
      }
      bankCost = choice_to_bank_cost.get(int(choice), 0)

      money = calculate_bank_results(money, bankCost, thieverySkill)
    
  return money
def plan_a_heist(money, heistSkill):
  print("|--Go on a heist =0--|")
  print("1-$1M Heist-$250K")
  print("2-$500M Heist-$125M")
  print("3-$1B Heist-$250M")
  print("4-$500B Heist-$125B")
  print("EXE to go to Stats")

  choice = input()

  if choice == '1' or choice == '2' or choice == '3' or choice == '4':
    choice_to_heist_cost = {
      1: 250_000,
      2: 125_000_000,
      3: 250_000_000,
      4: 125_000_000_000,
    }
    heistCost = choice_to_heist_cost.get(int(choice), 0)
    heistReward = heistCost * 4
      
    chance = round(random.randint(1, heistSkill))

    if money >= heistCost:
      print("You spent")
      print("$"+convert_number_to_unit(heistCost))
      print("To go on a heist")
      money -= heistCost
      if chance == 1:
        money += heistReward
        print("-SUCCESS-")
        print("You got $"+convert_number_to_unit(heistReward))
        print("From the heist")
      else:
        money -= (heistReward * 5)
        print("-FAILED-")
        print("You lost")
        print("$"+convert_number_to_unit(heistReward * 5))

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
  if choice == '1' or choice == '2' or choice == '3':
    loan_amount = {
      1: 1_000,
      2: 100_000,
      3: 1_000_000,
    }
    loan_amount = loan_amount.get(int(choice), 0)
  elif choice == '4':
    print("|----Get a Loan----|")
    print("1 - Get $100M Loan")
    print("2 - Get $1B Loan")
    print("3 - Get $100B Loan")
    print("4 - Get $1T Loan")
    print("EXE to go to Stats")

    choice = input()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
      loan_amount = {
        1: 100_000_000,
        2: 1_000_000_000,
        3: 100_000_000_000,
        4: 1_000_000_000_000,
      }
      loan_amount = loan_amount.get(int(choice), 0)
  if choice == '1' or choice == '2' or choice == '3' or choice == '4':
    newLoanAmount += loan_amount
    print("|You Borrowed $"+convert_number_to_unit(loan_amount)+"|")
    print_empty_lines(4)
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
  if choice == '1' or choice == '2' or choice == '3':
    loan_amount = {
      1: 1_000,
      2: 100_000,
      3: 1_000_000,
    }
    loan_amount = loan_amount.get(int(choice), 0)
  elif choice == '4':
    print("|--Pay off a Loan--|")
    print("1 - Repay $100M")
    print("2 - Repay $1B")
    print("3 - Repay $100B")
    print("4 - Repay $1T")
    print("EXE to go to Stats")

    choice = input()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
      loan_amount = {
        1: 100_000_000,
        2: 1_000_000_000,
        3: 100_000_000_000,
        4: 1_000_000_000_000,
      }
      loan_amount = loan_amount.get(int(choice), 0)
  if choice == '1' or choice == '2' or choice == '3' or choice == '4':
      if money >= loan_amount and loans >= loan_amount:
        newLoanAmount -= loan_amount
        print("|--You Repaid $"+convert_number_to_unit(loan_amount)+"--|")
        print_empty_lines(4)
        print("EXE to go to Stats")

        choice = input()
  return newLoanAmount

start_game()
