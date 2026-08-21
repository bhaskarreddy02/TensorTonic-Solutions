def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Return the micro-averaged F1 score rounded to four decimals.
    """
    # Write code here
    sum=0
    for i in range(len(y_pred)):
        if y_pred[i]==y_true[i]:
            sum=sum+1
            
    return sum/len(y_pred)  
    pass