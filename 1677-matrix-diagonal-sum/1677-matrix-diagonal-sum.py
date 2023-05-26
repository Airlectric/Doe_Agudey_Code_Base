class Solution(object):
    def diagonalSum(self, mat):
        sum = 0
        len_arr = len(mat)
        neg_len = -(len_arr+1)

        for i in range(len_arr):
                sum += mat[i][i]
                

        for a in range(len_arr):
                sum += mat[a][len_arr -1 -a]

        if len_arr % 2 == 1:
            sum -= mat[len_arr//2][len_arr//2]

        return sum

                

        