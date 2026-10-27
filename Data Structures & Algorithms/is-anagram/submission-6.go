func isAnagram(s string, t string) bool {
	var a, b [26]int
	for _, r := range s { a[r-'a']++}
	for _, r := range t { b[r-'a']++}
	return a == b
}
