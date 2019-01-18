class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for i in range(len(emails)):
            before_at = True
            met_plus = False
            candidate = []
            j = 0
            while j < len(emails[i]):
                if emails[i][j] == "+":
                    while emails[i][j] != "@":
                        j += 1

                if emails[i][j] == "@":
                    candidate += emails[i][j]
                    before_at = False
                    j += 1
                    continue
                if before_at and emails[i][j] == ".":
                    j += 1
                    continue
                candidate += emails[i][j]
                j += 1
            res.add(''.join(candidate))
        print(res)
        return len(res)


class Solution:
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)