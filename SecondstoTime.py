Seconds = int (input('enter the seconds: '))
hour= int (Seconds / 3600)
minute= int ((Seconds % 3600 ) / 60)
seconds = int (Seconds % 60)
if hour > 9 and minute > 9 and seconds > 9 :
    print(f"hour:minute:seconds  --> {(hour)}:{(minute)}:{(seconds)}")
elif hour > 9 and minute > 9 and seconds < 10 :
    print(f"hour:minute:seconds  --> {(hour)}:{(minute)}:0{(seconds)}")
elif hour > 9 and minute < 10 and seconds > 9 :
    print(f"hour:minute:seconds  --> {(hour)}:0{(minute)}:{(seconds)}")
elif hour > 9 and minute < 10 and seconds < 10 :
    print(f"hour:minute:seconds  --> {(hour)}:0{(minute)}:0{(seconds)}")
elif hour < 10 and minute > 9 and seconds > 9 :
    print(f"hour:minute:seconds  --> 0{(hour)}:{(minute)}:{(seconds)}")
elif hour < 10 and minute > 9 and seconds < 10 :
    print(f"hour:minute:seconds  --> {0(hour)}:{(minute)}:0{(seconds)}")
elif hour < 10 and minute < 10 and seconds > 9 :
    print(f"hour:minute:seconds  --> 0{(hour)}:0{(minute)}:{(seconds)}")
elif hour < 10 and minute < 10 and seconds < 10 :
    print(f"hour:minute:seconds  --> 0{(hour)}:0{(minute)}:0{(seconds)}")
