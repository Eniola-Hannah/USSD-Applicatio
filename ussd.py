print("- GLO... THE FAST NETWORK")
user = input("- Enter your USSD code - ")

if user == "*777#":
    dict1 = {
        'Register NIN': {
            'Enter NIN':'Enter your 11 digit NIN...\n And make sure it is not less or greater than 11 digit',
            'Check NIN Status':'Dear Subscriber you are yet to submit your NIN',
            'Cancel':'Thanks for choosing GLO'
        },
        'Data': {
            'Buy Data Plan':{
                'Mini Plans': ["1. N100=150MB 1 Day incl 35MB nite", "2. N200=350mb 2 Days incl 110MB nite", "3. N500=1.8GB 14 Days incl 1gb nite", "4. N50=50MB 1 Day incl 5MB nite", "0. Cancel"],

                'Monthly Plans': ["1. N1000 = 3.9GB 30Days incl 2GB nite", "2. N1500 = 7.5GB 30Days incl 4GB nite", "3. N2000 = 9.2GB 30Days incl 4GB", "4. N2500 = 10.8GB 30Days incl 4GB nite", "0. Cancel"],

                'Mega Plans': ["1. N10000 = 50GB 30Days incl 4GB nite", "2. N15000 = 75GB 30Days incl 7GB nite", "3. N18000 = 119GB 30Days incl 10GB nite", "4. N20000 = 138GB 30Days incl 12GB nite", "0. Cancel"],

                'Super Mega Plans': ["1. N30000 = 225GB 30Days", "2. N36000 = 300GB 30Days", "3. N50000 = 425GB 90Days", "4. N60000 = 525GB 120Days", "0. Cancel"]
            },
            'Gift Data Plan': 'Please select a plan to gift',
            'Share Data Plan': ["1. Share", "2. Unshare"],
            'Check Data Balance': "Dear Customer, your plan has expired and you do not have a data plan. To buy a data plan and continue browsing visit http://hsi.glo.com or dial *777#."
        },
        'E-top up': {
            'Airtime':{
                '5X Recharges':["1. N120", "2. N220", "3. N320", "4. N420", "0. Cancel"],
                'Regular Recharges':["1. Self", "2. Third party"]
            },
            'Data':{
                '1. Self':['1. N100 = 105MB 1Day incl 15MB nite', '2. N200 = 350MB 2Day incl 110MB nite', '3. N500 = 1.05GB 14Day incl 25M0B nite', '4. N1000 = 2.5GB'],
                '2. Third party':3,
                '00. Back':4
            }
        },
        'Berekete 10X': {
            "1. Migrate Now": "Dear Customer, you have been migrated from GLO_BEREKETE to BEREKETE_10X",
            "0. Back": 5,
            "00. Exit": 8,
        }
    }
    for index, dict in enumerate(dict1):
        print(index  +1, dict)
else:
    print("Invalid USSD Code")

user1 = input("--  ")
if user1 == '1':
    for index, registernin in enumerate(dict1['Register NIN']):
        print(index  +1, registernin)

    user2 = input("--  ")
    if user2 == "1":
        print(dict1['Register NIN']['Enter NIN'])
        
        user3 = input("---> ")
        if len(user3) == 11:
            print("you have successfully submitted your NIN, we will send you an SMS shortly after your NIN has been verified")
        elif len(user3) < 11:
            print("Dear Subscriber, you have input an incomplete NIN")
        elif len(user3) > 11:
            print("Dear Subscriber, you have input more than the 11 digit NIN number")
        else:
            print("Invalid Input") 

    elif user2 == "2":
        print(dict1['Register NIN']['Check NIN Status'])
    elif user2 == "3":
        print("Thanks for choosing GLO")
    else:
        print("WRONG INPUT!")

elif user1 == '2':
    for index, data in enumerate(dict1['Data']):
        print(index  +1, data)

    user4= input("-- ")
    if user4 == "1":
        print("1. Proceed(Auto-Renew)\n" "2. Proceed(One-Off)")

        user5 = input("-- ")
        if (user5 == "1") or (user5 == "2"):
            for index, buydata in enumerate(dict1['Data']['Buy Data Plan']):
                print(index  +1, buydata)

            user6 = input("--  ")
            if user6 == "1":
                for miniplans in dict1['Data']["Buy Data Plan"]["Mini Plans"]:
                    print(miniplans)

                user7 = input("--  ")
                if user7 == "1":
                    print("CONGRATS!, you have succefully subscribed to N100 data plan giving 150MB (115MB+35MB night) valid for 1 day.")
                elif user7 == "2":
                    print("CONGRATS!, you have succefully subscribed to N200 data plan giving 350MB (350MB+110MB night) valid for 2 day.")
                elif user7 == "3":
                    print("CONGRATS!, you have succefully subscribed to N500 data plan giving 1.8GB (1.8GB+1GB night) valid for 14 day.")
                elif user7 == "4":
                    print("CONGRATS!, you have succefully subscribed to N50 data plan giving 50MB (50MB+5MB night) valid for 1 day.")
                elif user7 == "0":
                    print("Thank you for choosing Glo")
                else:
                    print("Invalid Input")
            elif user6 == "2":
                for monthlyplans in dict1['Data']["Buy Data Plan"]["Monthly Plans"]:
                    print(monthlyplans)
                user8 = input("--  ")
                if user8 == "1":
                    print("CONGRATS!, you have succefully subscribed to N1000 data plan giving 3.9GB (3.9GB+1GB night) valid for 30 day.")
                elif user8 == "2":
                    print("CONGRATS!, you have succefully subscribed to N1500 data plan giving 7.5GB (7.5GB+4GB night) valid for 30 day.")
                elif user8 == "3":
                    print("CONGRATS!, you have succefully subscribed to N4000 data plan giving 9.2GB (9.2GB+4GB night) valid for 30 day.")
                elif user8 == "4":
                    print("CONGRATS!, you have succefully subscribed to N2500 data plan giving 10.8GB (10.8GB+4GB night) valid for 30 day.")
                elif user8 == "0":
                    print("Thank you for choosing Glo")
                else:
                    print("Invalid Input")
            elif user6 == "3":
                for megaplans in dict1['Data']["Buy Data Plan"]["Mega Plans"]:
                    print(megaplans)
                user9 = input("--  ")
                if user9 == "1":
                    print("CONGRATULATIONS!, you have succefully subscribed to N10000 data plan giving 50GB (50GB+4GB night) valid for 30 day.")
                elif user9 == "2":
                    print("CONGRATULATIONS!, you have succefully subscribed to N15000 data plan giving 75GB (75GB+7GB night) valid for 30 day.")
                elif user9 == "3":
                    print("CONGRATULATIONS!, you have succefully subscribed to N18000 data plan giving 119GB (119GB+10GB night) valid for 30 day.")
                elif user9 == "4":
                    print("CONGRATULATIONS!, you have succefully subscribed to N20000 data plan giving 138GB (138GB+12GB night) valid for 30 day.")
                elif user9 == "0":
                    print("Thank you for choosing Glo")
                else:
                    print("Invalid Input")
            elif user6 == "4":
                for supermegaplans in dict1['Data']["Buy Data Plan"]["Super Mega Plans"]:
                    print(supermegaplans)
                user0 = input("--  ")
                if (user0 == "1") or (user0 == "2") or (user0 == "3") or (user0 == "4"):
                    print("SORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow data. To Borrow Data now, just dial *321#")
                elif user0 == "0":
                    print("Thank you for choosing Glo")
                else:
                    print("Invalid Input")   
        else:
            print("WRONG INPUT")
    elif user4 == "2":
        print(dict1['Data']['Gift Data Plan'])
        for index, buydata in enumerate(dict1['Data']['Buy Data Plan']):
            print(index  +1, buydata)
        input1 = input("--  ")
        if input1 == "1":
            print("Mini Plan")
            for miniplans in dict1['Data']["Buy Data Plan"]["Mini Plans"]:
                print(miniplans)
            input2 = input("--  ")
            if input2 == "1":
                print("CONGRATS!, you have succefully subscribed to N100 data plan giving 150MB (115MB+35MB night) valid for 1 day.")
            elif input2 == "2":
                print("CONGRATS!, you have succefully subscribed to N200 data plan giving 350MB (350MB+110MB night) valid for 2 day.")
            elif input2 == "3":
                print("CONGRATS!, you have succefully subscribed to N500 data plan giving 1.8GB (1.8GB+1GB night) valid for 14 day.")
            elif input2 == "4":
                print("CONGRATS!, you have succefully subscribed to N50 data plan giving 50MB (50MB+5MB night) valid for 1 day.")
            elif input2 == "0":
                print("Thank you for choosing Glo")
            else:
                print("Invalid Input")
        elif input1 == "2":
            print("Monthly Plan")
            for monthlyplans in dict1['Data']["Buy Data Plan"]["Monthly Plans"]:
                print(monthlyplans)
            input3 = input("--  ")
            if input3 == "1":
                print("CONGRATS!, you have succefully subscribed to N1000 data plan giving 3.9GB (3.9GB+1GB night) valid for 30 day.")
            elif input3 == "2":
                print("CONGRATS!, you have succefully subscribed to N1500 data plan giving 7.5GB (7.5GB+4GB night) valid for 30 day.")
            elif input3 == "3":
                print("CONGRATS!, you have succefully subscribed to N4000 data plan giving 9.2GB (9.2GB+4GB night) valid for 30 day.")
            elif input3 == "4":
                print("CONGRATS!, you have succefully subscribed to N2500 data plan giving 10.8GB (10.8GB+4GB night) valid for 30 day.")
            elif input3 == "0":
                print("Thank you for choosing Glo")
            else:
                print("Invalid Input")
        elif input1 == "3":
            print("Mega Plan")
            for megaplans in dict1['Data']["Buy Data Plan"]["Mega Plans"]:
                print(megaplans)
            input4 = input("--  ")
            if input4 == "1":
                print("CONGRATULATIONS!, you have succefully subscribed to N10000 data plan giving 50GB (50GB+4GB night) valid for 30 day.")
            elif input4 == "2":
                print("CONGRATULATIONS!, you have succefully subscribed to N15000 data plan giving 75GB (75GB+7GB night) valid for 30 day.")
            elif input4 == "3":
                print("CONGRATULATIONS!, you have succefully subscribed to N18000 data plan giving 119GB (119GB+10GB night) valid for 30 day.")
            elif input4 == "4":
                print("CONGRATULATIONS!, you have succefully subscribed to N20000 data plan giving 138GB (138GB+12GB night) valid for 30 day.")
            elif input4 == "0":
                print("Thank you for choosing Glo")
            else:
                print("Invalid Input")
        elif input1 == "4":
            print("Super Mega Plan")
            for supermegaplans in dict1['Data']['Buy Data Plan']['Super Mega Plans']:
                print(supermegaplans)
            input5 = input("--  ")
            if (input5 == "1") or (input5 == "2") or (input5 == "3") or (input5 == "4"):
                print("SORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow data. To Borrow Data now, just dial *321#")
            elif input5 == "0":
                print("Thank you for choosing Glo")
            else:
                print("Invalid Input")   
        else:
            print("WRONG INPUT")  
    elif user4 == "3":
        for sharedata in dict1['Data']['Share Data Plan']:
            print(sharedata)   
        input6 = input("--  ")
        if input6 == "1":
            print("Please enter subscriber\'s number:")
            input7 = input("-->  ")
            if len(input7) == 11:
                print("Your request for Data sharing has been sent")
            elif len(input7) < 11:
                print("You have input an incomplete number")
            elif len(input7) > 11:
                print("You have input more than 11 digit number")
            else:
                print("Invalid Input")
        elif input6 == "2":
            print("Please enter subscriber\'s number:")
            input8 = input("-->  ")
            if len(input8) == 11:
                print("Your request to unshare Data has been sent")
            elif len(input8) < 11:
                print("You have input an incomplete number")
            elif len(input8) > 11:
                print("You have input more than 11 digit number")
            else:
                print("Invalid Input") 
        else:
            print("WRONG INPUT") 
    elif user4 == "4":
        print(dict1['Data']['Check Data Balance'])
    else:
        print("Invalid Input")       
elif user1 == '3':
    print("Welcome to Glo e-services \nPlease select an option")
    for index, etopup in enumerate(dict1['E-top up']):
        print(index  +1, etopup)
    input9 = input("--  ")
    if input9 == "1":
        for index, airtime in enumerate(dict1['E-top up']['Airtime']):
            print(index  +1, airtime)
        input0 = input("--  ")
        if input0 == "1":
            for recharges in dict1['E-top up']['Airtime']['5X Recharges']:
                print(recharges)
            enter = input("--  ")
            if (enter == "1") or (enter == "2") or (enter == "3") or (enter == "4"):
                print("Your request is being processed, we will send you an SMS shortly")
            elif enter == "0":
                print("Thanks for choosing GLO")
            else:
                ("Invalid Input")
        elif input0 == "2":
            print("Airtime Purchase")
            for regularrecharges in dict1['E-top up']['Airtime']['Regular Recharges']:
                print(regularrecharges)
            enter1 = input("--  ")
            if enter1 == "1":
                print("Please Enter Amount:")
                enter2 = input("-- ")
                if len(enter2) >= 2:
                    print("Your request is being processed, we will send you an SMS shortly \nThank you for using Glo e-services, the simplest way to recharge and buy data for family, friends and yourself")
                else:
                    print("Invalid input")
            elif enter1 == "2":
                print("Please enter phone number: \nGlo line only")
                enter3 = input("--  ")
                if len(enter3) == 11:
                    print("Enter Amount")
                    enter4 = input("--  ")
                    if len(enter2) >= 2:
                        print("Your request is being processed, we will send you an SMS shortly  \nThank you for using Glo e-services, the simplest way to recharge and buy data for family, friends and yourself")
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")
            else:
                print("invalid input")
        else:
            print("invalid input")
    elif input9 == "2":
        print('Data Plan Purchase')
        for  data in dict1['E-top up']['Data']:
            print(data)
        enter5 = input("--  ")
        if enter5 == "1":
            for selfplan in dict1['E-top up']['Data']['1. Self']:
                print(selfplan)
            userInput = input("> ")
            if (userInput == "1") or (userInput == "2") or (userInput == "3") or (userInput == "4"):
                print("Your request is being processed, we will send you an SMS shortly  \nThank you for using Glo e-services") 
            else:
                print("Invalid Input")
        elif enter5 == "2":
            print("Please enter phone number: \nGlo line only")
            enter6 = input("--  ")
            if len(enter6) == 11:
                print("Enter Amount")
                enter7 = input("--  ")
                if len(enter7) >= 2:
                    print("Your request is being processed, we will send you an SMS shortly  \nThank you for using Glo e-services, the simplest way to recharge and buy data for family, friends and yourself")
                else:
                    print("Invalid input")
            else:
                print("WRONG INPUT")
        elif enter5 == "00":
            print("Thank you for using Glo e-services, the simplest way to recharge and buy data for family, friends and yourself")
        else:
            print("WRONG INPUT")
    else:
        print("WRONG INPUT")

elif user1 == '4':
    for berekete in dict1['Berekete 10X']:
        print(berekete)
    enter0 = input("--  ")
    if enter0 == "1":
        print(dict1['Berekete 10X']['1. Migrate Now'])
    elif (enter0 == "0") or (enter0 == "00"):
        print("Thank you for choosing Glo")
else:
    print("INVALID INPUT!")
            
            