func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false;
	}

	counts := make(map[rune]int);
	for _, l := range s {
		counts[l]++;
	}

	for _, tl := range t {
		counts[tl]--;
		if counts[tl] < 0 {
			return false;
		}
	}

	return true;
}
