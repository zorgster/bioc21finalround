# Bioinformatics Contest 2021 - Final Round 

## Problem 3 - Superspreaders

https://stepik.org/lesson/541852/step/1?unit=535313

I missed the deadline for this by an hour or two.  

The code works fast in all of the tests but only scores incompletely (221 pts out of 650). It'll need a little fixing up to cover all the logic of the problem.

```
    import settings
    import q3
    settings.init()
    
    # assuming 10 tests
    # run_many will run the code 99 times and then take the median answers for each test.
    # 99 times runs in about 5 seconds, 999 times in 20-30 seconds, 9999 times in 1 minute or so
    
    q3.run_many("test3", 99, 10)
    
    # run once using:
    q3.readfile_v1("test3")
    
```
