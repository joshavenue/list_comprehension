x = [i**3 for i in range(10) if i**3 % 2 == 0]

print(x)

## Creates a list whereby starting from 0, i = 0,1,2,3,4,5,6,7,8,9 will be substituded into i as i**3
## Intially creating [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
## The IF condition whereby if any product of i**3 that is not even ( i**3 % 2 == 0 )
## Will not be included in the final outcome, hence : [0, 8, 64, 216, 512] instead.

x = [i**3 for i in range(10) if not i**3 % 2 == 0]

print(x)

## Adding 'not' in front of the 'if' will display odd number instead.
