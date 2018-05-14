(define (f 1)
  (+ x 10))
  unsaved-editor:1:11: define: expected a variable, but found a number in: 1
(define (f x)
  (+ x 10))
  
(define (g x)
  + x 10)
  unsaved-editor:2:4: define: expected only one expression for the function body, but found 2 extra parts in: x
(define (g x)
  (+ x 10))
  
(define h(x) 
  (+ x 10))
  unsaved-editor:2:2: define: expected only one expression after the variable name h, but found 1 extra part in: (+ x 10)
(define (h x) 
  (+ x 10))
