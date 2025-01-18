def find_and_print(messages, current_station):
    green_line = [
        "Songshan",
        "Nanjing Sanmin",
        "Taipei Arena",
        "Nanjing Fuxing",
        "Songjiang Nanjing",
        "Beimen",
        "Ximen",
        "Xiaonanmen",
        "Chiang Kai-Shek Memorial Hall",
        "Guting",
        "Taipower Building",
        "Gongguan",
        "Wanlong",
        "Jingmei",
        "Dapinglin",
        "Qizhang",
        "Xindian City Hall",
        "Xindian"
    ]
    sub_green_line = [
        "Qizhang", 
        "Xiaobitan"
    ]

    currentStationIndex
    currentStationIndex = green_line.findIndex(station => station === currentStation)
    if currentStationIndex == -1:
        currentStationIndex = sub_green_line.findIndex(station => station === currentStation)

        
    minDistance = 0
    closestPerson
    friendStationIndex
    friendStation
    for friend in messages:
        subLineDistance = 0
        friendStationOnSubLineIndex = sub_green_line.findIndex(subStation => messages[friend].includes(subStation))

        # 若是在副線上，計算副線與主線距離
        if friendStationOnSubLineIndex != -1:
            friendStation = sub_green_line[0]
            subLineDistance = Math.abs(friendStationOnSubLineIndex)
            friendStationIndex = green_line.findIndex(station => station === friendStation)
        else:
            friendStation = green_line.find(station => messages[friend].includes(station))
            friendStationIndex = green_line.findIndex(station => messages[friend].includes(station))
        # print("🚀 ~ findAndPrint ~ friendStationIndex:", friendStationIndex)


        if not closestPerson:
            closestPerson = friend
            minDistance = Math.abs(friendStationIndex - currentStationIndex) + subLineDistance
            continue

        # print("🚀 ~ findAndPrint ~ minDistance:", minDistance)
        if Math.abs(friendStationIndex - currentStationIndex) + subLineDistance < minDistance: 
            closestPerson = friend
            minDistance = Math.abs(friendStationIndex - currentStationIndex) + subLineDistance
    
    print("🚀  closestPerson:", closestPerson)


messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian