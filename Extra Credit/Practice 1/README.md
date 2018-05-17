# Practice 1

## functions.rkt

Translating the following functions into Racket:

1. A basketball player's points per game is based on the number of field goals fg, 3-point baskets 3pt, free throws ft, and a positive   number of games played gp:

~~~
points-per-game(fg, 3pt, ft, gp) = (2 * fg + 3 * 3pt + ft) / gp
~~~

2. Newton's law of universal gravitation describes the attraction between two masses, where G is the gravitational constant and r is the distance between the two masses:

~~~
force(m1, m2, r) = G * (m1m2) / (r ** 2)
~~~

3. A basic formula for calculating password entropy is, where s is the number of possible symbols and pl is the number of symbols in the password:

~~~
password-entropy(s, pl) = pl * logs / log2
~~~

4. An approximation of the number of partitions for the positive integer n:

~~~
partition-size-approximation(n) = (1 / 4nsqrt(3)) * e ^ (pi * sqrt(2n / 3))
~~~

## conversion.rkt

## jeopardy.rkt

## grade.rkt

## bonus.rkt
