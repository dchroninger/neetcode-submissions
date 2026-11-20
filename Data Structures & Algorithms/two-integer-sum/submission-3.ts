class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const seen:Record<number,number> = {}

        for (let i = 0; i < nums.length; i++){
            let needs = target - nums[i];

            if (needs in seen) {
                return [seen[needs],i]
            } else {
                seen[nums[i]] = i
            }
        }
    }
}
