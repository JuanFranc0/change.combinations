# change.combinations

  To complete Ernie's second challenge question, I decided to write some Python code to find the exact number of combinations of change that could make up a dollar. For this, I included all Canadian coins, including the toonie; this allows the code to find the change combinations of larger numbers as well as $1. 

# Using the change.combinations
  To test the code, running it in any Python development environment should be adequate. I used Pycharm to develop and test my script. To use the script, simply call the function <getChangeMethods> with the parameter being the number of cents you would like to find the change combinations for. Obviously, it should be a natural number. 
  
  To my knowledge, there is no real limit on the amount of cents you want to test. Of course, as with all code, it will begin to slow down as the amount of combinations rise exponentially. I tested up to one million dollars, but you are free to try and go as high as you would like. 
 
# List of Findings
| Dollars | Combinations |
|---------|--------------|
| 1       | 243          |
| 5       | 41,634       |
| 10      | 716,061      |
| 50      | 1.2322x10^9  |
| 100     | 3.6294x10^11 |
| 500     | 1.0597x10^14 |
| 1000    | 3.3621x10^15 |
| 5000    | 1.0434x10^20 |
| 10000   | 3.3362x10^20 |
