class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int rows[9] = {};
        int cols[9] = {};
        int boxes[9] = {};

        for (int r=0; r<9; r++) {
            for (int c=0; c<9; c++) {
                int val = board[r][c] - '1';

                if (board[r][c] == '.') continue;

                int box = (r / 3) * 3 + c / 3;

                int bitMask = 1 << val;

                if (rows[r] & bitMask || cols[c] & bitMask || boxes[box] & bitMask) {
                    return false;
                }

                rows[r] |= bitMask;
                cols[c] |= bitMask;
                boxes[box] |= bitMask;
            }
        }

        return true;
    }
};
