func hasDuplicate(nums []int) bool {
    out := false;
	found := make(map[int]bool);

	for _, num := range nums {
		_, exists := found[num];

		if exists {
			out = true;
			break;
		} else {
			found[num] = true;
			continue;
		}
	}

	return out;
}
