/**
 * 
    Task 1:
    We just received messages from 5 friends in JSON format, and we want to take the green
    line, including Xiaobitan station(小碧潭), of Taipei MRT to meet one of them. Write code to find out
    the nearest friend and print name, based on any given station currently located at and
    station count between two stations
 *  
 */

function findAndPrint(messages, currentStation){
    // (1) 陣列：列出所有綠線捷運站，小碧潭站先算成主線再加+副線站數
    // (2) 找出messages內的捷運站
    // (3) 找出離 currentStation 最近的捷運站
    // (4) 印出人名

    const green_line = [
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
    ];
    const sub_green_line = [
        "Qizhang", 
        "Xiaobitan"
    ];

    let currentStationIndex;
    currentStationIndex = green_line.findIndex(station => station === currentStation);
    if(currentStationIndex === -1){
        currentStationIndex = sub_green_line.findIndex(station => station === currentStation);
    }
    // console.log("🚀 ~ findAndPrint ~ currentStationIndex:", currentStationIndex)


    let minDistance = 0;
    let closestPerson;
    let friendStationIndex;
    let friendStation;
    for(var friend in messages){
        let subLineDistance = 0;
        // 先確認是否在副線上
        let friendStationOnSubLineIndex = sub_green_line.findIndex(subStation => messages[friend].includes(subStation));

        // 若是在副線上，計算副線與主線距離
        if (friendStationOnSubLineIndex !== -1) {
            friendStation = sub_green_line[0];
            subLineDistance = Math.abs(friendStationOnSubLineIndex);
            friendStationIndex = green_line.findIndex(station => station === friendStation);
        }else{
            friendStation = green_line.find(station => messages[friend].includes(station));
            friendStationIndex = green_line.findIndex(station => messages[friend].includes(station));
        }  
        // console.log("🚀 ~ findAndPrint ~ friendStationIndex:", friendStationIndex)

        if(closestPerson === undefined){
            closestPerson = friend;
            minDistance = Math.abs(friendStationIndex - currentStationIndex) + subLineDistance;
            continue;
        }

        // console.log("🚀 ~ findAndPrint ~ minDistance:", minDistance)
        if(Math.abs(friendStationIndex - currentStationIndex) + subLineDistance < minDistance){
            closestPerson = friend;
            minDistance = Math.abs(friendStationIndex - currentStationIndex) + subLineDistance;
        }
    }
    console.log("🚀  closestPerson:", closestPerson);
}

const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Leslie":"I'm at home near Xiaobitan station.",
    "Vivian":"I'm at Xindian station waiting for you."
};
findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian