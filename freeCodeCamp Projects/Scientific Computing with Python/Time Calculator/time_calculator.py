def add_time(start, duration, dayOfWeek = "None"):

    # Variable initialization
    allDayFormatHours = ""
    allDayFormatMinutes = ""
    dayCount = 0
    splitStart = start.split()
    splitStartHour = splitStart[0].split(":")
    splitDuration = duration.split(":")

    # Switching to 24h format
    if splitStart[1] == "AM":
        allDayFormatHours = splitStartHour[0]
        allDayFormatMinutes = splitStartHour[1]
    else:
        allDayFormatHours = str(int(splitStartHour[0]) + 12)
        allDayFormatMinutes = splitStartHour[1]
    
    # Adding the duration
    allDayFormatHours = str(int(allDayFormatHours) + int(splitDuration[0]))
    allDayFormatMinutes = str(int(allDayFormatMinutes)+ int(splitDuration[1]))

    if int(allDayFormatMinutes) > 59:
        allDayFormatMinutes = str(int(allDayFormatMinutes) - 60)
        allDayFormatHours = str(int(allDayFormatHours) + 1)
    
    while int(allDayFormatHours) > 23:
        allDayFormatHours = str(int(allDayFormatHours) - 24)
        dayCount += 1

    # Working with dayOfWeek option
    selectedDayOfWeek = ""
    daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if dayOfWeek != "None":
        dayOfWeek = dayOfWeek.lower()
        index = daysOfTheWeek.index(dayOfWeek.capitalize())
        index = index + dayCount
        if index > len(daysOfTheWeek) - 1:
            while index > 6:
                index -= 7
        selectedDayOfWeek = daysOfTheWeek[index]

    # Preparing final output
    finalDayOfWeek = "" if dayOfWeek == "None" else (", " + selectedDayOfWeek)
    if dayCount == 0:
        finalDaysLaterFormat = ""
    else:
        finalDaysLaterFormat = " (next day)" if dayCount == 1 else " (" + str(dayCount) + " days later)"

    finalTimeFormat = ""
    if int(allDayFormatHours) < 12:
        if allDayFormatHours == "0":
            allDayFormatHours = "12"
        if int(allDayFormatMinutes) < 10:
            allDayFormatMinutes = "0" + allDayFormatMinutes
        finalTimeFormat = allDayFormatHours + ":" + allDayFormatMinutes + " AM"
    else:
        allDayFormatHours = str(int(allDayFormatHours) - 12)
        if allDayFormatHours == "0":
            allDayFormatHours = "12"
        if int(allDayFormatMinutes) < 10:
            allDayFormatMinutes = "0" + allDayFormatMinutes
        finalTimeFormat =  allDayFormatHours + ":" + allDayFormatMinutes + " PM"

    # Return statement :)
    return finalTimeFormat + finalDayOfWeek + finalDaysLaterFormat