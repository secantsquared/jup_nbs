def merge_the_tools(string, k):
    outputs = []
    n = len(string)
    substring_ratio = n / k
    for i in range(0, n):
        j = 0
        while j < n:
            outputs.append(string[i:substring_ratio])
            j += substring_ratio
