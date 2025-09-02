from datetime import datetime
from playsound import playsound
import winsound

alarm_date = input('Enter the date on which you want to set alarm: ')
alaram_time = ''.join(input("Enter the alarm time to beset HH:MM, AM/PM format : ").split())
music_or_beep = input("Enter m for a music or b for beep : ")
if music_or_beep == 'b':
    dur = int(input("duraton in second: "))*1000
    freq = int(input("frequency of the alaram: "))

alarm_hour = alaram_time[0:2]
alarm_minutes = alaram_time[3:5]
alarm_period = alaram_time[6:8].upper()

print('setting alarm....')

while True:
    current_time = datetime.now()
    current_hour = current_time.strftime('%I')
    current_minute = current_time.strftime('%M')
    current_period = current_time.strftime('%p')
    current_date = current_time.strftime('%d')

    if current_date == alarm_date and current_period == alarm_period and current_hour == alarm_hour and current_minute == alarm_minutes:
        print('*'*10)
        print('| '+'wake up'+' |')
        print('*'*10)
        if music_or_beep == 'm':
            playsound('audio.wav')
        else:
            winsound.Beep(freq, dur)
        break