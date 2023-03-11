'''
https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
'''


def format_duration(sec):
    if sec == 0:
        return 'now'
    else:
        year = sec // 31536000
        day = (sec % 31536000) // 86400
        hour = ((sec % 31536000) % 86400) // 3600
        minute = (((sec % 31536000) % 86400) % 3600) // 60
        second = (((sec % 31536000) % 86400) % 3600) % 60
        l = ['years', 'days', 'hours', 'minutes', 'seconds']
        l_time = [year, day, hour, minute, second]
        s = ''
        for i in range(len(l)):
            if l_time[i]:
                if l_time[i] > 1:
                    s += str(l_time[i]) + ' ' + l[i] + ', '
                else:
                    s += str(l_time[i]) + ' ' + l[i][:len(l[i]) - 1] + ', '

        s = s[:len(s) - 2]
        i = s.rfind(', ')
        if i != -1:
            return s[: i] + s[i:].replace(', ', ' and ', 1)
        else:
            return s
