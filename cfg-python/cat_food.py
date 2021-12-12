num_of_cats=10
daily_cans=.5
total_cans=num_of_cats*daily_cans

days=7

print(str(num_of_cats)+" cats eat "+str(total_cans)+" cans per day.")
print("For "+str(days)+" days, they eat "+str(int(days*total_cans))+" cans in total")

print("{} cats eat {} cans for {} days, at {} per day".format(num_of_cats, total_cans, days, daily_cans))