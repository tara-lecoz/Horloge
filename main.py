import time

# permet de régler l'heure souhaitée quand on appelle la fonction
def afficher_heure():
    global hour, minute, second
    hour = int(input("Enter the hour : ")) 
    minute = int(input("Enter the minute : "))
    second = int(input("Enter the second : "))
    
# permet de régler l'heure souhaitée pour l'alarme quand on appelle la fonction   
def set_alarm():
    global alarm_hour, alarm_minute, alarm_second, alarm_on
    alarm_hour = int(input("Enter the hour for the alarm : "))
    alarm_minute = int(input("Enter the minute for the alarm : "))
    alarm_second = int(input("Enter the second for the alarm : "))
    alarm_on = True

# permet de choisir le format de l'heure affichée quand on appelle la fonction
def set_time_format():
    global time_format
    time_format = input("Enter time format (12 or 24) : ")
    if time_format != "12" and time_format != "24":
        time_format = input("Enter a valid time format (12 or 24) : ")
    
hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
second = int(time.strftime("%S"))
# permet de vérifier si l'alarme a été initialisée ou non
alarm_hour = -1 
alarm_minute = -1
alarm_second = -1.0
alarm_on = False

time_format = "24"

# ici les fonctions sont appelées, si ce n'était pas le cas le programme afficherait uniquement l'heure actuelle
afficher_heure()
set_alarm()
set_time_format()

while True:
    if time_format == "12" and hour < 12:
        if hour == 0:
            hour = 12
            print("\r%02d:%02d:%02d AM" % (hour, minute, second), end="")
        elif time_format == "12" and hour > 12:
            hour -= 12
            print("\r%02d:%02d:%02d PM" % (hour, minute, second), end="")
    if time_format == "24":
        print("\r%02d:%02d:%02d" % (hour, minute, second), end="")
    print("\r%02d:%02d:%02d" % (hour, minute, second), end="")

    time.sleep(1)
    second += 1
    # fonctionnement d'une horloge manuellement
    if second == 60:
        second = 0
        minute += 1
    if minute == 60:
        minute = 0
        hour += 1
    if hour == 24:
        hour = 0
    if alarm_on:
        # permet de vérifier les conditions qui vont permettre à l'alarme de s'activer
        if hour == alarm_hour or hour == alarm_hour - 12 and minute == alarm_minute and second == alarm_second:
            print("\nAlarm! Wake up!")
            alarm_on = False
            if alarm_hour > 12:
                print("\r%02d:%02d:%02d PM" % (hour, minute, second), end="")
            else:
                print("\r%02d:%02d:%02d AM" % (hour, minute, second), end="")