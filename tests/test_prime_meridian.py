"""Focused new tests; does not assert earlier repository suites were rerun."""
import importlib.util
from pathlib import Path
import unittest
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
HERE=Path(__file__).resolve().parent
PATH=ROOT/'experiments'/'prime_meridian.py'
if not PATH.exists(): PATH=HERE/'prime_meridian.py'
SPEC=importlib.util.spec_from_file_location('prime_meridian',PATH)
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)

class PrimeMeridianTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps=45
        cls.d=M.kernel_data(12,45,8,'2.5')
        cls.ref=M.reference_li(12,50)
        cls.ctl=M.li_from_cumulants([a+b for a,b in
            zip(cls.d['cumulants'],M.control_cumulants(12))])

    def test_positive_kernel(self):
        for v in ('0','.3','1','2'):
            self.assertGreater(M.phi(mp.mpf(v)),0)

    def test_tilt_normalizer(self):
        self.assertLess(abs(self.d['normalizer']-mp.mpf('.5')),mp.mpf('1e-38'))

    def test_independent_reference(self):
        self.assertLess(max(abs(a-b) for a,b in
            zip(self.d['li'][1:],self.ref[1:])),mp.mpf('1e-38'))

    def test_first_two_theory_and_twelve_numeric(self):
        k=self.d['cumulants']
        self.assertGreater(k[1],0)
        self.assertGreater(k[2],0)
        self.assertEqual(self.d['li'][2],2*k[1]+k[2])
        self.assertTrue(all(v>0 for v in self.d['li'][1:]))

    def test_not_all_cumulants_positive(self):
        self.assertLess(self.d['cumulants'][3],0)
        self.assertLess(self.d['cumulants'][4],0)

    def test_control_eight_pass_then_nine_fail(self):
        self.assertTrue(all(v>0 for v in self.ctl[1:9]))
        self.assertLess(self.ctl[9],-17)

    def test_off_axis_control_zero_and_radii(self):
        z=mp.pi/6+1j*mp.acosh(2)/6
        s=mp.mpf('.5')+1j*z
        self.assertLess(abs(4+2*mp.cos(6*z)),mp.mpf('1e-40'))
        self.assertTrue(0<s.real<mp.mpf('.5'))
        self.assertGreater(abs((s-1)/s),1)
        self.assertLess(abs(s/(1-s)),1)

    def test_single_global_cayley_chart(self):
        for t in (mp.mpf('1'),mp.mpf('10'),mp.mpf('100')):
            s=mp.mpf('.5')+1j*t
            theta=2*mp.atan(2*t)
            q=s/(1-s)
            self.assertLess(abs(q-mp.exp(1j*theta)),mp.mpf('1e-40'))
            self.assertLess(abs((s-1)/s+1/q),mp.mpf('1e-40'))

    def test_generating_coefficient_recurrence(self):
        moments=self.d['moments']
        g=[mp.mpf(1)]+[mp.fsum(mp.binomial(n-1,j-1)*moments[j]/mp.factorial(j)
                              for j in range(1,n+1)) for n in range(1,13)]
        out=[mp.mpf(0)]
        for n in range(1,13):
            out.append(n*g[n]-mp.fsum(out[j]*g[n-j] for j in range(1,n)))
        self.assertTrue(all(v>0 for v in g))
        self.assertLess(max(abs(a-b) for a,b in zip(out,self.d['li'])),mp.mpf('1e-38'))

if __name__=='__main__': unittest.main()
