from datetime import date
import locale

locale.setlocale(locale.LC_TIME, "de-DE")


def getDate():
    day = date.today()
    day = day.strftime("%A %d. %B")
    return str(day)
