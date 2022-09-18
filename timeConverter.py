from math import floor

def convertTime(time: int) -> str:
    """
    Takes an amount of time in seconds and returns it nicely formatted into years, days, hours, minutes and seconds.
    """

    if time == 0:
        return "0 seconds"
    
    if time < 0:
        return "<invalid time>"

    timeUnits = ['second', 'minute', 'hour', 'day', 'year']
    timeConversions = [60, 60, 24, 365, 0]

    timeBlocks = []
    for conversion in timeConversions:
        if time >= conversion and conversion != 0:
            time = time / conversion
            timeBlocks.append(round((time % 1) * conversion))
        else:
            timeBlocks.append(floor(time))
            break
    
    output = []
    for i in range(len(timeBlocks)):
        currentTimeBlock = timeBlocks[i]
        if currentTimeBlock < 1:
            continue
        output.append(f"{timeBlocks[i]} {timeUnits[i]}{'' if timeBlocks[i] == 1 else 's'}")
    
    output.reverse()
    if len(output) > 1:
        return f"{', '.join(output[0 : -1])} and {output[-1]}"

    else:
        return output[0]