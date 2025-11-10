class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0 or not s:
            return False

        st = []
        match = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for pattern in s:
            if pattern in match:
                st.append(match[pattern])
            else:
                if not st or st.pop() != pattern:
                    return False
        
        return False if st else True

