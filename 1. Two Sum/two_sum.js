/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    
    // create a map
    const d = {};

    // loop through nums; JavaScript does not provide something like Python's enumerate statement, just looping through the list
    for (let i = 0; i < nums.length; i ++){
        // create a variable, m, to represent the difference between the target and the starting value
        let m = target - nums[i];

        // if m exists in the map, d, we return the starting index, i, and the corresponding index of m;
        // otherwise, we add the index of m, which in this case, not exist in the map yet, to the map, to pair with should the value of m exists later in the list of values

        if (m in d){
            return [d[m], i] ;
        } else {
            d[nums[i]] = i ;
        }
    }
    return null;
};

