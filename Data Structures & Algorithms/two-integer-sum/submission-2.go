func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)

	for i, num := range nums {
		
		need := target - num
		val, ok := seen[need];

		if (ok) {
			return []int{val,i}
		} else {
			seen[num] = i
		}
	}
	return []int{}
}
