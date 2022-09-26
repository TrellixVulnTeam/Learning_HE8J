#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int findDuplicate(std::vector<int>& nums) {
    int n = nums.size();
        //highest number is n, n+1 size means last index position is n
        
    for (int i = 0; i < n ; i ++) {
        int index = nums[i] % n;
        nums[index] += n;
    }
    for (int i = 0; i < n; i++) {
        if (nums[i] - 2*n > 0) {
            return i;
        }
    }
    return nums[0];
    }



int main(void) {
    vector<int> a = {1,2,3,2,4};
 
    int i = findDuplicate(a);
    for (int i = 0; i < a.size(); i ++){
        cout << a[i];
    }
    cout << i;
}