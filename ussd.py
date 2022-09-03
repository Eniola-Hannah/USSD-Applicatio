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
            