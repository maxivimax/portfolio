# So interesting

one = "INSERT INTO patricipation(id, user_id, event_id, datetime) VALUES ("
two = ", '125', '"
three = "', '2023-03-03 "
four = "03:"
five = ":"
eight = "');"

id = 1236
minute = 4
second = 10

time = 55

while time < 101:
    if time != 76 and time != 57 and time != 59:
        if minute < 10 and second < 10:
            string = (
                str(one)
                + str(id)
                + str(two)
                + str(time)
                + str(three)
                + str(four)
                + str("0")
                + str(minute)
                + str(five)
                + str("0")
                + str(second)
                + str(eight)
            )
            print(string)
        elif second > 9 and minute < 10:
            string = (
                str(one)
                + str(id)
                + str(two)
                + str(time)
                + str(three)
                + str(four)
                + str("0")
                + str(minute)
                + str(five)
                + str(second)
                + str(eight)
            )
            print(string)
        elif minute > 9 and second < 10:
            string = (
                str(one)
                + str(id)
                + str(two)
                + str(time)
                + str(three)
                + str(four)
                + str(minute)
                + str(five)
                + str("0")
                + str(second)
                + str(eight)
            )
            print(string)
        else:
            string = (
                str(one)
                + str(id)
                + str(two)
                + str(time)
                + str(three)
                + str(four)
                + str(minute)
                + str(five)
                + str(second)
                + str(eight)
            )
            print(string)
        second = second + 3
        id = id + 1
        if second > 59:
            second = 0
            minute = minute + 1
    time = time + 1
