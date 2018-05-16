;; area-pipe: number number number -> number
;; to find the surface area of an open cylinder given an inner radius, length, and wall thickness
(define (area-pipe radius length thickness)
  (+ (* (circumference radius) length)
     (* (circumference (+ radius thickness)) length)
     (* 2 (- (area-circle (+ radius thickness)) (area-circle radius)))))

;; circumference: number -> number
;; to find the circumference of a circle given a radius
(define (circumference radius)
  (* 2 pi radius))

;; area-circle: number -> number
;; to find the area of a circle given a radius
(define (area-circle radius)
  (* pi radius radius))
