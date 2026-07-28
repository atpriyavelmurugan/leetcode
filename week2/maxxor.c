#include <stdbool.h>
typedef struct {
    int key;
    bool used;
} HashSetItem;

int findMaximumXOR(int* nums, int numsSize) {
    int maxResult = 0;
    int mask = 0;
    for (int i = 30; i >= 0; i--) {
        mask = mask | (1 << i);
        int tableSize = numsSize * 2;
        HashSetItem* hashSet = (HashSetItem*)calloc(tableSize, sizeof(HashSetItem));
        
        for (int j = 0; j < numsSize; j++) {
            int prefix = nums[j] & mask;
            int hash = abs(prefix) % tableSize;
            while (hashSet[hash].used && hashSet[hash].key != prefix) {
                hash = (hash + 1) % tableSize;
            }
            hashSet[hash].key = prefix;
            hashSet[hash].used = true;
        }
        
        int greedyGuess = maxResult | (1 << i);
        for (int j = 0; j < numsSize; j++) {
            int prefix = nums[j] & mask;
            int target = prefix ^ greedyGuess;
            int hash = abs(target) % tableSize;
            bool found = false;
            while (hashSet[hash].used) {
                if (hashSet[hash].key == target) {
                    found = true;
                    break;
                }
                hash = (hash + 1) % tableSize;
            }
            
            if (found) {
                maxResult = greedyGuess;
                break;
            }
        }
        
        free(hashSet); 
    }
    
    return maxResult;
}
