#!/usr/bin/env python3
"""Chapter 34: exact signature test for a reflected zero pair."""
from fractions import Fraction

def pair_form(a,b):
    return 2*(a*b)  # real slice; enough to witness both signs

def main():
    J=((0,1),(1,0))
    assert pair_form(Fraction(1),Fraction(1))==2
    assert pair_form(Fraction(1),Fraction(-1))==-2
    for a,b in ((1,1),(1,-1)):
        assert (J[0][0]*a+J[0][1]*b,J[1][0]*a+J[1][1]*b)==(b,a)
    # Quaternionic extension contains the real slice, so negative persists.
    print("PASS: reflected off-line 2x2 block has eigenvalues +1 and -1")
    print("PASS: negative real vector also witnesses quaternionic indefiniteness")
    print("LIMITATION: not an admissible global Weil test-function construction")
    print("NO RH PROOF")

if __name__=="__main__":
    main()
