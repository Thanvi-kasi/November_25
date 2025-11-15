class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)

        # Multiply each digit (simulate manual multiplication)
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                d1 = ord(num1[i]) - ord('0')
                d2 = ord(num2[j]) - ord('0')
                
                mul = d1 * d2
                p1 = i + j
                p2 = i + j + 1
                
                # Add to result with carry
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10

        # Convert result array to string, skipping leading zeros
        result = []
        for digit in res:
            if not (digit == 0 and len(result) == 0):
                result.append(str(digit))

        return "".join(result)
