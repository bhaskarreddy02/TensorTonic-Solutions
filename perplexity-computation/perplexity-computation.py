def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    lenght=len(actual_tokens)
    sum=0
    for i in range(lenght):
        p=prob_distributions[i][actual_tokens[i]]
        sum+=math.log(p)
    H=-sum/lenght
    return math.exp(H)