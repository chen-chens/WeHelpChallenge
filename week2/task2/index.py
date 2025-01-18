has_booked_consultants = []
def book(consultants, hour, duration, criteria):
    def get_price(x):
        return x.get('price')

    def get_rate(x):
        return x.get('rate')

    def handle_match(available_consultants, criteria):
        temp = [*available_consultants]
        if criteria == 'price':
            target = min(temp, key=get_price)

        if criteria == 'rate':
            target = max(temp, key=get_rate)

        has_booked_consultants.append({
            **target,
            'startHour': hour,
            'endHour': hour + duration
        })
        print(target.get('name'))

    if not has_booked_consultants:
        return handle_match(consultants, criteria)

    avaiables = []
    startHour = hour
    endHour = hour + duration
    for item in consultants:
        isNotExisted = all(consultant.get('name') != item.get('name') for consultant in has_booked_consultants)
        if isNotExisted:
            avaiables.append(item)
        else:
            filtered = []
            for consultant in has_booked_consultants:
                if consultant.get('name') == item.get('name'):
                    filtered.append(consultant)

            isAvaiable = all(endHour <= consultant.get('startHour') or startHour >= consultant.get('endHour') for consultant in filtered)
            if isAvaiable:
                avaiables.append(item)

    if not avaiables:
        print("No Service")
    else:
        # print('has_booked_consultants', has_booked_consultants)
        return handle_match(avaiables, criteria)


consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
]
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John