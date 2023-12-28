For part 2, it could be used a polyfit

[reddit](https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/keaiiq7/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

[polyfit](https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/kebm6ak/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
[wolframalpha](https://www.wolframalpha.com/input?i=quadratic+fit+calculator&assumption=%7B%22F%22%2C+%22QuadraticFitCalculator%22%2C+%22data3x%22%7D+-%3E%22%7B0%2C+1%2C+2%7D%22&assumption=%7B%22F%22%2C+%22QuadraticFitCalculator%22%2C+%22data3y%22%7D+-%3E%22%7B3762%2C+33547%2C+93052%7D%22)

[Visual explanation](https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21)
26501365 isn't a random number. 
Our input is 131x131 tiles in size, and 26501365 = 65 + (202300 * 131). 
65 is the number of steps it takes to get from the centre of the square to the edge, and 131 is the number of steps it takes to traverse the whole square. 
So if you traveled 26501365 steps in a straight line from the start, you will traverse 202300 squares (each square is 131x131)


You need to find the best y values for x = 0, x = 1, and x = 2 (which are equal to f(65), f(65 + 131), f(65 + 131 * 2)).

f(65) = a0

f(65 + 131) = a1

f(65 + 2 * 131) = a2

...

then you'll get something 

a0 + a1 x + a2 x^2

Substituting x = 202300 you'll get the answer


In short, instead of calculating all the f(65), f(65 + 131), f(65 + 131 * 2), f(65 + 131 * 3)... and so on, we stopped at the first
3 coefficient, extract the quadratic function that would best fit the those coefficients and delegate math to find the value of the n repetition f(65 + 131 * n) (find the value by using a function)


[Btw, people complains by the fact that this pattern is only present in the large input data, not in the simple one!!](https://www.reddit.com/r/adventofcode/comments/18nol3m/comment/kecf2yx/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)