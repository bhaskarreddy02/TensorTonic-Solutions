import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """Return the Binomial PMF at k and CDF through k."""
    # Write code here
    cdf=0
    comb=math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    for i in range(0,k+1):
        cdf+=(math.factorial(n)/(math.factorial(i)*math.factorial(n-i)))*(p**i)*((1-   p)**(n-i))
    pmf=(comb)*(p**k)*((1-p)**(n-k))
    return {"pmf":pmf,"cdf":cdf}
    pass