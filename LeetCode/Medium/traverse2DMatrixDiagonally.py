#traverse2DMatrixDiagonally

class Solution():

	def findDiagonalOrder(self, matrix):
		"""
        :type matrix: List[List[int]]
        :rtype: List[int]
		"""

		d = {}

		# Loop through the matrix and fill dictionary d
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):

				if i+j not in d:
					# Fill diagonal elements 
					d[i+j] = [matrix[i][j]]
				else:
					# Fill non diagonal elements
					d[i+j].append(matrix[i][j])


		ans = []

		for entry in d.items():

			if entry[0] % 2 == 0:
				[ans.append(x) for x in entry[1][::-1]]
			else:
				[ans.append(x) for x in entry[1]]

		return ans

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(matrix)
output = Solution().findDiagonalOrder(matrix)
print(output)

