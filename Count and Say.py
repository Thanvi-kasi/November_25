class Solution:
    def countAndSay(self, n: int) -> str:
        # Start with the base case
        result = "1"
        
        # Generate the sequence from 2 to n
        for _ in range(1, n):
            next_result = ""
            count = 1
            # Traverse the previous result string
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    next_result += str(count) + result[i - 1]
                    count = 1
            # Don't forget to add the last sequence
            next_result += str(count) + result[-1]
            result = next_result
        
        return result
