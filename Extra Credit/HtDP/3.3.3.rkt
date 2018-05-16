;; area-cylinder: number number -> number
;; Calculates surface area of a cylinder given base radius and height
(define (area-cylinder r h)
  (+ (* 2 (area-circle r)) (* h (circumference r))))
  
;; area-circle: number -> number
;; calculates area of a circle given its radius
(define (area-circle r)
  (* r r pi))
  
;; circumference: number -> number
;; calculates circumference of a circle given its radius
(define (circumference r)
  (* 2 pi r))
