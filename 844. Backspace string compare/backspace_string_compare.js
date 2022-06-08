/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var backspaceCompare = function(s, t) {

    return newEdits(s) == newEdits(t);

    // create a new function, to get the "counter" to store the skipping counts

    function newEdits(str){
        let result = ''; // create an empty string
        let backspaces = 0;

        for(let i = str.length - 1 ; i >= 0; i -=1){
            if(str[i] === '#'){
                backspaces += 1;
            }else if(backspaces > 0){
                backspaces -= 1;
            }else{
                result = str[i] + result;
            }
        }
        return result;
    }
 };