#Written by Cameron Coles
#Written on July 25th 2023
#Program Purpose: To make a reciept for a car insurance company

###########
#LIBRARIES#
###########

import datetime

###########
#CONSTANTS#
###########

f = open('OSCIDef.dat','r')
POLICY_NUMBER = int(f.readline())
COST_BASIC_PREMIUM = float(f.readline())
ADD_CAR_RATE = float(f.readline())
COST_LIABILITY_COVERAGE = float(f.readline())
COST_GLASS_COVERAGE = float(f.readline())
COST_LOANER_COVERAGE = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())

f.close()

#################
#INPUT VARIABLES#
#################

while True:
    first_name = input("Enter Client's First Name: ").title()
    last_name = input("Enter Client's Last Name: ").title()
    address = input("Enter Client's Address: ").title()
    city = input("Enter Client's City: ")
    province = input("Enter Client's Province (i.e. NL): ")

    provinces = ["NS","NU","ON","PE","QC","SK","YT","AB","BC","MB","NB","NL","NT"]
    boolean_Val_P = False
    while boolean_Val_P == False:
        for i in provinces:
            if i == province:
                boolean_Val_P = True

        if boolean_Val_P != True:
            print()
            print("ERROR: INVALID PROVINCE")
            print()
            province = input("Enter Client's Province (i.e. NL): ")

    postal_code = input("Enter Client's Postal Code: ")
    phone_number = input("Enter Client's Phone Number: ")
    car_amount = int(input("Enter Number of Cars Being Insured: "))
    liability = input("Extra Liability up to $1,000,000 (Y/N)? ").title()

    while True:
        if liability != "Y" and liability != "N":
            print()
            print("ERROR: INVALID, ENTER (Y/N)")
            print()
            liability = input("Extra Liability up to $1,000,000 (Y/N)? ").title()

        else:
            break

    glass_coverage = input("Optional Glass Coverage (Y/N): ").title()

    while True:
        if glass_coverage != "Y" and glass_coverage != "N":
            print()
            print("ERROR: INVALID, ENTER (Y/N)")
            print()
            glass_coverage = input("Optional Glass Coverage (Y/N): ").title()

        else:
            break

    loaner_car = input("Optional Loaner Car (Y/N): ").title()

    while True:
        if loaner_car != "Y" and loaner_car != "N":
            print()
            print("ERROR: INVALID, ENTER (Y/N)")
            print()
            loaner_car = input("Optional Loaner Car (Y/N): ").title()

        else:
            break

    payment_type = input("Enter Payment Type (Full/Monthly): ").title()

######################
#CALCULATED VARIABLES#
######################

    premium = COST_BASIC_PREMIUM + ((car_amount - 1)* (COST_BASIC_PREMIUM * ADD_CAR_RATE))
    total_extra = 0

    if liability == "Y":
        total_extra += (COST_LIABILITY_COVERAGE * car_amount)

    if glass_coverage == "Y":
        total_extra += (COST_GLASS_COVERAGE * car_amount)

    if loaner_car == "Y":
        total_extra += (COST_LOANER_COVERAGE * car_amount)

    total_premium = premium + total_extra
    total_HST = total_premium * HST_RATE
    total_cost = total_HST + total_premium

    monthlyPayments = (total_cost + PROCESSING_FEE) / 8
    current_date = datetime.datetime.now()
    current_date = current_date.strftime('%m-%d-%Y')
    first_payday = f"{current_date[0]}{(int(current_date[1])+1)}-01-{current_date[6:]}"

###################
#OUTPUT FORMATTING#
###################


    print()
    print()
    print()
    print()
    print("       One Stop Insurance Company      ")
    print("            Invoice Reciept            ")
    print()
    print(" ------------------------------------- ")
    print(f" Invoice Date: {current_date}")
    print()
    print(" Client Name and Address:")
    print()
    print(f" {first_name} {last_name}")
    print(f" {address}")
    print(f" {city}, {province} {postal_code}")
    print()
    print(f" Phone: {phone_number} ")
    print()
    print(f" Payment Type:                   {payment_type}")
    print(f" Number of Cars:                {car_amount}")
    print(f" Liability Coverage:             {liability}")
    print(f" Glass Coverage:                 {glass_coverage}")
    print(f" Loaner Car Coverage:            {loaner_car}")
    print("                          ----------")
    print(f" Insurance Premiums:             {f'${premium:,.2f}':>10s}")
    print(f" Extra charges:                  {f'${total_extra:,.2f}':>10s}")
    print(f" Total Insurance Premiums:       {f'${total_premium:,.2f}':>10s}")
    print("                          ----------")
    print(f" Total HST:                      {f'${total_HST:,.2f}':>10s}")
    print(f" Total Cost:                     {f'${total_cost:,.2f}':>10s}")
    print()
    if payment_type == "Monthly":
        print("                          ----------")
        print(f" Monthly Total:                  {f'${monthlyPayments:,.2f}':>10s}")
        print(f" Total Number of Month's:          8")
        print(f" Date of First Payment:            {first_payday}")
    print(" ------------------------------------- ")
    print()
    print()
    print()

#################
#DATA COLLECTION#
#################

    print("Saving Policy Information...(0%)")
    f = open("Policies.dat","a")

    f.write("{}, ".format(str(POLICY_NUMBER)))
    f.write("{}, ".format(str(current_date)))
    f.write("{}, ".format(str(first_name)))
    f.write("{}, ".format(str(last_name)))
    f.write("{}, ".format(str(address)))
    f.write("{}, ".format(str(city)))
    f.write("{}, ".format(str(province)))
    print("Saving Policy Information...(50%)")
    f.write("{}, ".format(str(postal_code)))
    f.write("{}, ".format(str(phone_number)))
    f.write("{}, ".format(str(car_amount)))
    f.write("{}, ".format(str(liability)))
    f.write("{}, ".format(str(glass_coverage)))
    f.write("{}, ".format(str(loaner_car)))
    f.write("{}, ".format(str(payment_type)))
    f.write("{}".format(str(total_premium)))
    f.write("\n")

    f.close()


    print("Saving Policy Information...(100%)")
    print()
    print("Policy information processed and saved")
    print()

    POLICY_NUMBER += 1
    


    cont = input("Would You Like To Enter Another Invoice (Y/N) ?").title()
    if cont == "N":
        break

f = open("OSCIDef.dat","w")

f.write("{}\n".format(str(POLICY_NUMBER)))
f.write("{}\n".format(str(COST_BASIC_PREMIUM)))
f.write("{}\n".format(str(ADD_CAR_RATE)))
f.write("{}\n".format(str(COST_LIABILITY_COVERAGE)))
f.write("{}\n".format(str(COST_GLASS_COVERAGE)))
f.write("{}\n".format(str(COST_LOANER_COVERAGE)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(PROCESSING_FEE)))

f.close()




