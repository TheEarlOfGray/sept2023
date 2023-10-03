control = int(input('''Time Calculator
1-	Add 2 times   
2-	Find the difference between 2 times  
3-	Convert to Hours  
4-	Convert to Minutes  
5-	Convert Minutes to Time  
6-	Convert Hours to Time  
7-	Convert Days to Time  
8-	Exit  
Enter an option:  '''))
'''
02:04:24
10:20:46
13:01:10
'''
if control in [1,2]:
    str1 = input("Please enter string 1: ")
    str2 = input("Please enter string 2: ")
    if control == 1:
        dayres = 0
        time1 = str1.split(":")
        time2 = str2.split(":")
        minres = int(time1[2]) + int(time2[2])
        if minres >= 60:
            hourres = (minres // 60)
            minres = (minres % 60)
        hourres += int(time1[1]) + int(time2[1])
        if hourres >= 24:
            dayres += (hourres // 24)
            hourres = (hourres % 24)
        dayres += int(time1[0]) + int(time2[0])
        print(f"{dayres}:{hourres}:{minres}")
    else:
        list1 = sorted([str1,str2])
        time1 = list1[0].split(":")
        mins1 = int(time1[2]) + (int(time1[1]) * 60) + (int(time1[0]) * 1440)
        time2 = list1[1].split(":")
        mins2 = int(time2[2]) + (int(time2[1]) * 60) + (int(time2[0]) * 1440)
        result = mins2 - mins1
        rem = result % 1440
        dayres = result // 1440
        minres = rem % 60
        hourres = rem // 60
        print(f"{str(dayres).zfill(2)}:{str(hourres).zfill(2)}:{str(minres).zfill(2)}")
        

elif control in [3,4]:
    pass
elif control in [5,6,7]:
    pass
elif control == 8:
    pass




