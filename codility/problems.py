def solution(S, k):
    for i in range(1, len(S)):
        for j in range(i):
            if ord(S[i]) < ord(S[j]):
                print(S[i], S[j])
    pass

S = "decade"
K = 4
solution(S, K)