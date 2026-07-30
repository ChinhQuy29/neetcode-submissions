class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        while i < len(asteroids) - 1:
            if asteroids[i] * asteroids[i + 1] > 0 or asteroids[i] - asteroids[i + 1] < 0:
                i += 1
                continue
            
            if asteroids[i] + asteroids[i + 1] > 0:
                asteroids.pop(i + 1)
            elif asteroids[i] + asteroids[i + 1] < 0:
                asteroids.pop(i)
            else:
                asteroids.pop(i + 1)
                asteroids.pop(i)
            
            i -= 1
        
        return asteroids
