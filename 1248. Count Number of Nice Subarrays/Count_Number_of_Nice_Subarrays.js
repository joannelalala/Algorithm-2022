/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 var numberOfSubarrays = function(nums, k) {

    // initially, I used the hint in the problem: replacing even number with 0 and odd number with 1
    // later I checked others' thought processes
    // I realized we could just use two pointers to calculate the count of sub-arrays without doing the first step
    // however, I still keep the first step in the code, but that part was actually covered in the "two-pointers" step

    // start with the hint:
    // first, replace each even by 0 and odd by 1 in the list nums
    // if uncomment the below part, the result will still be accurate.
    
//    for(let i = 0; i < nums.length; i ++){
//        if(nums[i] % 2 === 0){
//            nums[i] = 0;
//        }else{
//            nums[i] = 1;
//        }
//    }
    
    // now we have nums only with 0 & 1
    // next step: use two pointers to count number of sub-arrays
    // the idea is:
    // use the right pointer to loop through nums: if encoutering an odd number, odd_cnt increments by 1
    // use the left pointer to loop through nums: if encoutering an odd number, odd_cnt decrements by 1

    let left; right = 0;
    let odd_cnt; cur_sub_cnt; ans = 0;

    for(let right = 0; right < nums.length; right ++){
        if(nums[right] % 2 == 1){ // it is an odd number
            odd_cnt += 1;
            cur_sub_cnt = 0;
        }

        while(odd_cnt == k){ // continue looping until odd_cnt == k
            if(nums[left] % 2 == 1){ // if nums[left] is odd, odd_cnt decrements by 1
                odd_cnt -= 1;
            }
            cur_sub_cnt += 1;
            left += 1; // continue the loop
        } // get out of the while loop
        ans += cur_sub_cnt;
    }

    return ans;
};