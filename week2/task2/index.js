/**
 * Task 2:
    Assume we have consultants for consulting services. Help people book the best matching
    consultant in a day, based on hours, service durations, and selection criteria.
    1. Booking requests are one by one, order matters.
    2. A consultant is only available if there is no overlapping between already booked time
    and an incoming request time.
    3. If the criteria is "price", choose the available consultant with the lowest price.
    4. If the criteria is "rate", choose the available consultant with the highest rate.
    5. If every consultant is unavailable, print "No Service".
 * 
 */

const hasBookedConsultants = [];
function book(consultants, hour, duration, criteria){
    function handleMatch(availableConsultants, criteria){
        const temp = [...availableConsultants]; // 直接執行sort，會影響原本陣列順序
        if(criteria === 'price'){
            const [target, ...rest] = temp.sort((a, b) => a.price - b.price);
            hasBookedConsultants.push({
                ...target,
                startHour: hour,
                endHour: hour + duration
            });
            console.log(target.name);
            return;
        }
        if(criteria === 'rate'){
            const [target, ...rest] = temp.sort((a, b) => b.rate - a.rate);
            hasBookedConsultants.push({
                ...target,
                startHour: hour,
                endHour: hour + duration
            });
            console.log(target.name);
            return;
        }
    }

    if(hasBookedConsultants.length === 0){
        return handleMatch(consultants, criteria);
    }

    let avaiables = [];
    const startHour = hour;
    const endHour = hour + duration;
    consultants.forEach(item => {
        const isNotExisted = hasBookedConsultants.every(consultant => consultant.name !== item.name);
        if(isNotExisted){
            avaiables.push(item);
        }else{
            const filtered = hasBookedConsultants.filter(consultant => consultant.name === item.name);
            const isAvaiable = filtered.every(consultant => (endHour <= consultant.startHour || startHour >= consultant.endHour));

            if(isAvaiable){
                avaiables.push(item);
            }
        }
    });

    if(avaiables.length === 0){
        console.log("No Service");
    }else{
        return handleMatch(avaiables, criteria);
    }
}
const consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
];
book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John