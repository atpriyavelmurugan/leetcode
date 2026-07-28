char* longestPalindrome(char* s) {
    if (s == NULL || s[0] == '\0') {
        return "";
    }
    
    int length = 0;
    while (s[length] != '\0') {
        length++; 
    }
    
    int start = 0;
    int maxLength = 1;
    
    for (int i = 0; i < length; i++) {
        int left = i;
        int right = i;
        while (left >= 0 && right < length && s[left] == s[right]) {
            int currentLen = right - left + 1;
            if (currentLen > maxLength) {
                maxLength = currentLen;
                start = left;
            }
            left--;
            right++;
        }
        left = i;
        right = i + 1;
        while (left >= 0 && right < length && s[left] == s[right]) {
            int currentLen = right - left + 1;
            if (currentLen > maxLength) {
                maxLength = currentLen;
                start = left;
            }
            left--;
            right++;
        }
    }
    char* result = (char*)malloc((maxLength + 1) * sizeof(char));
    for (int i = 0; i < maxLength; i++) {
        result[i] = s[start + i];
    }
    result[maxLength] = '\0';
    
    return result;
}
