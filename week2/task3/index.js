/**
 * Task 3:
    Find out whose middle name is unique among all the names, and print it. You can assume
    every input is a Chinese name with 2 ~ 5 words. If there are only 2 words in a name, the
    middle name is defined as the second word. If there are 4 words in a name, the middle name
    is defined as the third word.
 * 
 */

function func(...data){
    const mapData = new Map();

    data.forEach(value => {
        switch(value.length){
            case 2:
                mapData.set(value, value.slice(-1));
            break;
            case 4:
                mapData.set(value, value.slice(-2, -1));
            break;
            default:
                const targetIndex = (value.length - 1) / 2;
                mapData.set(value, value.split('')[targetIndex]);
        }
    });
    
    const middleNames = Array.from(mapData.values());
    const uniqueNames = [];
    mapData.forEach((value, key) => {
        const counts = middleNames.filter(name => name === value).length;
        if(counts === 1){
            uniqueNames.push(key) 
        }
    });
    if(uniqueNames.length === 0){
        console.log("沒有");
    }else{
        console.log(uniqueNames.join());
    }
}
func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安