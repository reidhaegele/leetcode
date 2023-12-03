class Solution:
    def hashify(self, s: str) -> {}:
        h = {}
        for l in s:
            h[l] = h.get(l, 0) + 1
        return h

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        hnw = []
        for s in strs:
            hnw.append([self.hashify(s), s])

        output = []
        found = False
        for word in hnw:
            for group in output:
                if group[0][0] == word[0]:
                    group.append(word)
                    found = True
                    break
            if not found:
                output.append([word])
            found = False
        
        o = []
        for g in output:
            ng = []
            for w in g:
                ng.append(w[1])
            o.append(ng)
        return o