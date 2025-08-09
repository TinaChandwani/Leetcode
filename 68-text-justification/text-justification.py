class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        result = []
        length = 0
        
        i = 0
        n = len(words)

        while i < n:
            w = len(words[i])
            if line and len(line) + w + length > maxWidth:
                # Justify the words in the line
                if len(line) == 1:
                    # left justify
                    result.append(line[0] + " " * (maxWidth - length))
                else:
                    total_space = maxWidth - length
                    slots = len(line) - 1
                    base = total_space // slots
                    extra = total_space % slots
                    parts = []
                    for idx in range(slots):
                        spaces = base
                        if extra > 0:
                            spaces += 1
                            extra -= 1
                        parts.append(line[idx] + (" " * spaces))
                    parts.append(line[-1])
                    result.append(''.join(parts))

                # Reset
                line = []
                length = 0
            else:
                line.append(words[i])
                length += w
                i += 1
        
        # last Line
        last = ' '.join(line)
        last += " " * (maxWidth - len(last))
        result.append(last)  

        return result