import sklearn_decision
import sklearn_decision11
import tertiary

inp = input("Enter the symptoms:")

p1 = inp.split(',') 

sklearn_decision.primary(p1)
sklearn_decision11.secondary(p1)
tertiary.tertiary(p1)

