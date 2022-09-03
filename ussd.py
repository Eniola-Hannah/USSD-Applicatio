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

                'Mega Plans': ["1. N10000 = 50GB 30Days incl 4GB nite", "2. N15000 = 7.5GB 30Days incl 7GB nite", "3. N18000 = 119GB 30Days incl 10GB nite", "4. N20000 = 138GB 30Days incl 12GB nite", "0. Cancel"],

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