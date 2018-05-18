;; points-per-game: number number number number number -> number
;; to determing a player's average points per basketball game
(define (points-per-game fg 3pt ft gp)
  (/ (+ (* 2 fg) (* 3 3pt) ft) gp))

;; force: number number number -> number
;; to determine gravitational force
(define (force m1 m2 r)
  (* G (/ (* m1 m2) (* r r))))
  
;; Gravitational constant
(define G 0.00000000006674)

;; password-entropy: number number -> number
;; to determine strength of a password
;; s is number of possible symbols, pl is number of symbols used
(define (password-entropy s pl)
  (* s (/ (log s) (log 2))))

;; partition-size-approximation: number -> number
;; to approximated the number of partitions for n
(define (partition-size-approximation n)
  (* (/ 1 (* 4 n (sqrt 3))) (exp (* pi (sqrt (/ (* 2 n) 3))))))
