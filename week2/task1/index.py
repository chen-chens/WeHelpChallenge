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

    is_in_sub_line = False
    if current_station in green_line:
        current_main_station_index = green_line.index(current_station)
    elif current_station in sub_green_line:
        is_in_sub_line = True
        current_main_station_index = green_line.index(sub_green_line[0])  # 計算主線距離用

        
    min_distance = 0
    closestPerson = None
    for friend, message in messages.items():
        is_friend_in_sub_line = False
        sub_line_distance = 0
        friend_station_on_sub_line_index = -1

        # 先確認是否在副線上
        friend_station_on_sub_line = next((station for station in sub_green_line if station in message), None)
        if friend_station_on_sub_line:
            is_friend_in_sub_line = True
            friend_station_on_sub_line_index = sub_green_line.index(friend_station_on_sub_line)

        # 若是在副線上，計算副線與主線距離
        if friend_station_on_sub_line_index != -1:
            friend_station = sub_green_line[0]
            sub_line_distance = abs(friend_station_on_sub_line_index)
            friend_station_index = green_line.index(friend_station)
        else:
            friend_station = next((station for station in green_line if station in message), None)
            if friend_station:
                friend_station_index = green_line.index(friend_station)

        # 初始值
        if closestPerson == None:
            closestPerson = friend
            if(is_in_sub_line and is_friend_in_sub_line):
                min_distance = sub_line_distance
            else:
                min_distance = abs(friend_station_index - current_main_station_index) + sub_line_distance
            continue

        # print("🚀 ~ findAndPrint ~ min_distance:", min_distance)
        if(is_in_sub_line and is_friend_in_sub_line):
            distance = sub_line_distance
        else:
            distance = abs(friend_station_index - current_main_station_index) + sub_line_distance

        # 比較
        if distance < min_distance: 
            closestPerson = friend
            min_distance = distance
    
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
find_and_print(messages, "Xiaobitan") # print Leslie

# next((station for station in green_line if station in message), None)
# for station in green_line
#   if station in message
#       return station