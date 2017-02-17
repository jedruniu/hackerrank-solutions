def common_prefix_len(first,second):
    pref_len = 0
    while(first[0] == second[0]):
        pref_len += 1
        first, second = first[1:], second[1:]
        if first == "" or second == "":
            break
    return pref_len

def is_convertable_in_k_steps(s,t,k):
    pref_len = common_prefix_len(s,t)
    diff_without_pref = len(s) + len(t) - 2 * pref_len

    if k % 2 == diff_without_pref % 2:
        if k >= diff_without_pref:
            return True
        else:
            return False
    else:
        if k >= len(s) + len(t):
            return True
        else:
            return False