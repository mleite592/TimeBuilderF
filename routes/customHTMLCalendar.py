import calendar
from flask import url_for

class CustomHTMLCalendar(calendar.HTMLCalendar):
    def formatday(self, day, weekday, year, month):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            day_link = url_for('timesheets.index', year=year, month=month, day=day)
            return f'<td class="{self.cssclasses[weekday]}"><a href="{day_link}">{day}</a></td>'
        
    def formatmonth(self, theyear, themonth, withyear=True):
        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, theyear, themonth))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

    def formatweek(self, theweek, year, month):
        s = ''.join(self.formatday(d, wd, year, month) for (d, wd) in theweek)
        return f'<tr>{s}</tr>'