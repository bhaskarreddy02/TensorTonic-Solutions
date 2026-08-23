import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """Return the Poisson PMF at k and CDF through k."""
    # Write code 
    cdf=0
    for i in range(0,k+1):
        cdf=cdf+((math.e)**(-lam))*((lam)**i)/(math.factorial(i))
    
    return {"pmf": ((math.e)**(-lam))*((lam)**k)/(math.factorial(k)), "cdf": cdf}
    pass