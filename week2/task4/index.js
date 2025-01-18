/**
 * Task 4:
    There is a number sequence: 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, …
    Find out the nth term in this sequence.
 * 
 */

function getNumber(index){
    // [4, 4, -1] 循環
    const x = Math.floor((index + 2) / 3);
    const y = Math.floor((index + 1) / 3);
    const z = Math.floor(index / 3);
    const values = (4 * x) + (4 * y) - (1 * z);
    console.log(values);
}
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70