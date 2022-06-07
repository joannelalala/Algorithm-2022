/**
 * @param {string} s
 * @return {number}
 */
 var romanToInt = function(s) {
    const transformation = {
        I:1,
        V:5,
        X:10,
        L:50,
        C:100,
        D:500,
        M:1000
    };
    let number = 0;
    for (let i=0 ; i< s.length ; i++){
        if (transformation[s[i]] < transformation[s[i+1]]){
            number += transformation[s[i+1]] - transformation[s[i]];
            i ++;
        } else {
            number += transformation[s[i]];
        }
       
    }
    return number;
    
};
