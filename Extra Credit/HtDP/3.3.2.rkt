;; volume-cylinder: number number -> number
;; calculates the volume of a cylinder given the radius of its base and its height
(define (volume-cylinder r h)
  (* (area-of-disk r) h))
  
;; area-of-disk: number -> number
;; finds area of a disk given its radius
(define (area-of-disk r)
  (* r r PI))
  
(define PI 3.14159)
