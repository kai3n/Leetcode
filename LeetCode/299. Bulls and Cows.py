class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_dic = collections.Counter(secret)
        guess_dic = collections.Counter(guess)
        bulls = 0
        cows = 0
        for k, v in secret_dic.items():
            if guess_dic.get(k) is not None:
                if guess_dic[k] > v:
                    bulls += v
                else:
                    bulls += guess_dic[k]
        for s, g in zip(secret, guess):
            if s == g:
                bulls -= 1
                cows += 1
        return str(cows) + "A" + str(bulls) + "B"
