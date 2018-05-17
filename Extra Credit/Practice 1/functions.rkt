(define (points-per-game fg 3pt ft gp)
  (/ (+ (* 2 fg) (* 3 3pt) ft) gp))
  
(define (force m1 m2 r)
  (* G (/ (* m1 m2) (* r r))))
  
(define G 0.00000000006674)
