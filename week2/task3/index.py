def func(*data):
    map_data = {}
    
    for value in data:
        length = len(value)
        if length == 2:
            map_data[value] = value[-1]
        elif length == 4:
            map_data[value] = value[-2]
        else:
            target_Index = (length - 1) // 2
            map_data[value] = value[target_Index]

    middle_names = list(map_data.values())
    unique_names = []

    for key, value in map_data.items():
        counts = middle_names.count(value)
        if counts == 1:
            unique_names.append(key)

    if not unique_names:
        print("沒有")
    else:
        print(",".join(unique_names))


func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安



#|語言   |用法             |遍歷目標                      |結果|
#|Python|for value in data|List、Tuple、Set、Dict、String|直接取 值（但字典預設取 鍵）|
#|JS    |for key in obj   |Object 或 Array              |取 key（物件）或索引（陣列）|
#|JS    |for value of arr |陣列（Array）或其他可迭代物件    |取 值|