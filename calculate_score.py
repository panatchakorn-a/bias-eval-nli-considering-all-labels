def calculate_score(results):
    """
    results: [[ep, cp, np], 
            [ea, ca, na], 
            [en, cn, nn]]
    the values should be proportion, i.e. ep+cp+np=1 and so on.
    """
    # calculate the bias score
    ep, cp, np = results[0][0], results[0][1], results[0][2] # PS
    ea, ca, na = results[1][0], results[1][1], results[1][2] # AS
    en, cn, nn = results[2][0], results[2][1], results[2][2] # NS
    bias_score = (ep + ca + 1-nn)/3

    return bias_score