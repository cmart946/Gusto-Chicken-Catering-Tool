import math


safety_buffer = 1.10 # 10% extra chicken to be safe, (extra portions, waste, unexpected sales)


#function for converting cooked pounds of chicken into uncooked (raw)
def cooked_to_raw(total_cooked):
      return total_cooked * 1.25 # 1.25 is the conversion factor from cooked to raw chicken pounds




number_of_cases_currently = int(input("Enter number of cases of chicken currently in stock: "))

number_of_catering_orders_this_week = int(input("Enter number of catering orders this week (as of now): "))


if number_of_catering_orders_this_week == 0:
        print("No catering as of now, no need to order more than usual. ")
else:
        number_of_catering_orders_this_week > 0
        day_for_catering = []
        for i in range(number_of_catering_orders_this_week):
            day = input(f"Enter day for catering order {i+1}: ")
            day_for_catering.append(day)
            print(day_for_catering)


# new inventroy comes in on monday, wednesday, and friday
total_lbs = number_of_cases_currently * 40
# on average a pound of raw chicken turns into .75 lbs of cooked chicken (16 oz to 12 oz after cooking)


current_stock = total_lbs; #lbs of chicken
avg_daily_usage = 18 # lbs of chicken used on average per day 
days_until_delivery = 3 #number of days until the next delivery



if number_of_catering_orders_this_week == 0:
        print ("no need to order extra cases of chicken (normal usage will suffice)")
else:
        number_of_catering_orders_this_week > 0
        lbs_per_order = [] #created an empty list for number of
        print("please enter number of lbs of chicken needed for each catering order")
        for i in range(number_of_catering_orders_this_week):
            lbs_needed = int(input(f"Enter lbs needed for catering order {i+1}: "))
            lbs_per_order.append(lbs_needed)

#this is taking the sum of all the lbs from the catering orders and resulting how many extra cases of chicken are neeed 
print(lbs_per_order)
total = sum(lbs_per_order)
print ("total lbs needed for these catering orders is: ", total)


rawchicken_conversion = 1.25 # to convert cooked chicken lbs to raw chicken lbs
print("\n")
print("\n")
print("Based on the catering orders entered, the amount of cooked chicken needed converts to needing " , round((total * rawchicken_conversion) * safety_buffer), " lbs of raw chicken.\n") #"round" means to round the deciaml

#enter here the function (def) to calculate cases needed to order (rounded up)
rounded_raw_chicken_calculation =round((total * rawchicken_conversion) * safety_buffer)
net_weight_per_case = 40 # lbs of raw chicken per case


def cases_for_catering(rounded_raw_chicken_calculation, net_weight_per_case):
    cases_needed = math.ceil(rounded_raw_chicken_calculation / net_weight_per_case)
    return cases_needed


extra_cases = cases_for_catering(rounded_raw_chicken_calculation, net_weight_per_case)

print("extra cases needed for catering orders: ", extra_cases)

     



""" old logic for extra cases needed based on lbs needed, was not realistic, would have to include every case manually
if total * rawchicken_conversion <= 40:
    print("this means for the catering orders, you should order 1 extra case of chicken.")
elif total * rawchicken_conversion > 40 and total * rawchicken_conversion <= 80:
    print("this means for the catering orders, you should order 2 extra cases of chicken.")
print("this means for the catering orders, you should order ")
"""

catering_orders = [20, 15] # LIST of lbs of chicken needed for each catering order


adjusted_stock = current_stock - sum (lbs_per_order)
projected_usage = avg_daily_usage * days_until_delivery
final_stock = adjusted_stock - projected_usage 

print(final_stock)


if final_stock < 0:
    print("Critical: Will rin out of chicken before delivery!")
else:
    print("Stock level sufficient until delivery.")




