class Solution {
public:

    vector<int> sortArrayByParityII(vector<int>& A) {
        vector<int> even, odd;
        for(int i = 0; i < A.size(); i++) { 
            if (A[i] % 2 == 0)
                even.push_back(A[i]);
            else
                odd.push_back(A[i]);
        }
        int idx_1 = 0, idx_2 = 0;
        for(int i = 0; i < A.size(); i++) {
            if(idx_1 == even.size() && idx_2 == odd.size())
                break;
            if (i % 2 == 0) {
                A[i] = even[idx_1];
                idx_1++;
            }
            else if (i % 2 != 0) {
                A[i] = odd[idx_2];
                idx_2++;
            }
        }
        return A;
    }
};