divisors n = 1 : filter ((==0) . rem n) [2 .. n `div` 2]

main = do
    print(divisors 4324320)