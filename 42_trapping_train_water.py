class Solution:
    def trap(self, height) -> int:
        total = 0
        barStack = []
        heightIndex = 0
        
        while heightIndex < len(height):
            while len(barStack) is not 0 and height[heightIndex] > height[barStack[-1]] :
                topIndex = barStack.pop()
                if len(barStack) == 0:
                    break
                distance = heightIndex - barStack[-1] - 1
                bounded_height = min(height[heightIndex], height[barStack[-1]]) - height[topIndex]
                total += distance * bounded_height
            barStack.append(heightIndex)
            heightIndex += 1
            
        
        return total