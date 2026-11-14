#!/usr/bin/env python3
"""Theta cumulants and the Cayley/Li bridge. No zero list is used.
Finite computations are not a proof of RH or interval-certified bounds.
Requires mpmath. Run: python prime_meridian.py --output results.json
"""
from __future__ import annotations
import argparse
from functools import lru_cache
import json
from pathlib import Path
import platform
import time
import mpmath as mp


def xi(s):
    if s == 0 or s == 1:
        return mp.mpf('0.5')
    return s*(s-1)/2 * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)


def phi(v, terms=8):
    """Even theta kernel; evaluate stable positive-v series."""
    v = abs(mp.mpf(v))
    e2 = mp.exp(2*v)
    return mp.exp(v/2)*mp.fsum(
        (4*mp.pi**2*k**4*e2**2-6*mp.pi*k*k*e2)*mp.exp(-mp.pi*k*k*e2)
        for k in range(1, terms+1))


def cumulants(moments):
    """Raw moments E[V^j], j=0..N, to cumulants (index zero is zero)."""
    if not moments or abs(moments[0]-1) > mp.mpf('1e-20'):
        raise ValueError('moments[0] must be 1')
    k = [mp.mpf(0)]
    for n in range(1, len(moments)):
        k.append(moments[n]-mp.fsum(mp.binomial(n-1,j-1)*k[j]*moments[n-j]
                                   for j in range(1,n)))
    return k


def li_from_cumulants(k):
    return [mp.mpf(0)]+[mp.fsum(mp.binomial(n,j)*k[j]/mp.factorial(j-1)
                               for j in range(1,n+1))
                        for n in range(1,len(k))]


def kernel_data(order=12, digits=50, terms=8, cutoff='2.5'):
    """Moments of exp(v/2)*Phi(v)/xi(1) on R; no xi/zeta calls.

    Evenness folds to v>=0, using cosh for even moments, sinh for odd.
    Integral and theta series are truncated, not interval-certified.
    """
    with mp.workdps(digits):
        end=mp.mpf(cutoff)
        if order<1 or end<2 or terms<1:
            raise ValueError('order>=1, cutoff>=2, terms>=1 required')
        @lru_cache(maxsize=None)
        def cached_phi(v): return phi(v,terms)
        breaks=[mp.mpf(x) for x in ('0','.25','.5','1','1.5')]+[end]
        raw=[]
        for j in range(order+1):
            fn=mp.cosh if j%2==0 else mp.sinh
            raw.append(mp.quad(lambda v:2*cached_phi(v)*v**j*fn(v/2),breaks))
        moments=[x/raw[0] for x in raw]
        k=cumulants(moments)
        return {'normalizer':raw[0],'moments':moments,'cumulants':k,
                'li':li_from_cumulants(k)}


def reference_li(order=12, digits=60):
    """Independent logarithmic-derivative formula at s=1, not a zero sum."""
    with mp.workdps(digits):
        c=mp.taylor(lambda s:mp.log(xi(s)),mp.mpf(1),order)
        k=[mp.mpf(0)]+[c[j]*mp.factorial(j) for j in range(1,order+1)]
        return li_from_cumulants(k)


def control_cumulants(order=12,a='6',c='4'):
    """Added tilt cumulants for Phi(v-a)+Phi(v+a)+c*Phi(v).

    Fourier multiplier: c+2*cos(a*z). Independent tilt shift takes values
    -a,0,+a with weights exp(-a/2),c,exp(a/2).
    """
    a,c=mp.mpf(a),mp.mpf(c)
    if a<=0 or c<=2: raise ValueError('a>0 and c>2 required')
    norm=mp.exp(-a/2)+c+mp.exp(a/2)
    ms=[mp.mpf(1)]+[((-a)**j*mp.exp(-a/2)+a**j*mp.exp(a/2))/norm
                      for j in range(1,order+1)]
    return cumulants(ms)


def run(order=12,digits=50):
    start=time.perf_counter()
    low=kernel_data(order,digits,8,'2.5')
    high=kernel_data(order,digits+15,10,'3')
    with mp.workdps(digits+15):
        reference=reference_li(order,digits+15)
        shift=control_cumulants(order)
        control=li_from_cumulants([a+b for a,b in zip(high['cumulants'],shift)])
        z0=mp.pi/6+1j*mp.acosh(2)/6
        s0=mp.mpf('.5')+1j*z0
        rows=[{'n':j,'theta_li':mp.nstr(high['li'][j],32),
               'reference_li':mp.nstr(reference[j],32),
               'cumulant':mp.nstr(high['cumulants'][j],32),
               'positive_kernel_control_li':mp.nstr(control[j],32)}
              for j in range(1,order+1)]
        return {
            'name':'Prime Meridian / Cayley-Li theta-cumulant investigation',
            'base_repository_commit':'9163b62a67a62b20af7a9e147a732364dbf1b244',
            'scope':'Mathematical coordinates only; no RH proof or novelty claim.',
            'order':order,
            'runs':[{'digits':digits,'terms':8,'cutoff':'2.5'},
                    {'digits':digits+15,'terms':10,'cutoff':'3'}],
            'tilted_integral_normalizer':mp.nstr(high['normalizer'],40),
            'normalizer_error_vs_half':mp.nstr(abs(high['normalizer']-mp.mpf('.5')),8),
            'max_li_run_difference':mp.nstr(max(abs(a-b) for a,b in
                                              zip(low['li'][1:],high['li'][1:])),8),
            'max_li_reference_error':mp.nstr(max(abs(a-b) for a,b in
                                               zip(high['li'][1:],reference[1:])),8),
            'rows':rows,
            'control':{'a':'6','c':'4',
                'positive_first_orders':[j for j in range(1,order+1) if control[j]>0],
                'negative_orders':[j for j in range(1,order+1) if control[j]<0],
                'added_Xi_zero_real':mp.nstr(z0.real,25),
                'added_Xi_zero_imag':mp.nstr(z0.imag,25),
                'added_xi_zero_real':mp.nstr(s0.real,25),
                'added_xi_zero_imag':mp.nstr(s0.imag,25),
                'factor_zero_residual':mp.nstr(abs(4+2*mp.cos(6*z0)),8),
                'Li_map_radius':mp.nstr(abs((s0-1)/s0),25),
                'quaternion_meridian_radius':mp.nstr(abs(s0/(1-s0)),25)},
            'numerical_caution':'Finite truncations and precision comparisons; not interval certification or an all-orders theorem.',
            'runtime_seconds':round(time.perf_counter()-start,3),
            'environment':{'python':platform.python_version(),'mpmath':mp.__version__}}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--order',type=int,default=12)
    p.add_argument('--digits',type=int,default=50)
    p.add_argument('--output',type=Path,default=Path('prime_meridian_results.json'))
    args=p.parse_args()
    if not 1<=args.order<=20 or args.digits<35: p.error('order 1..20; digits>=35')
    result=run(args.order,args.digits)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
