class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines=input.split("\n")
        print(lines)
        maxlen=0
        pathlen={0:0}
        for line in lines:
            path=line.split("\t")[-1]
            print(path)
            depth=len(line)-len(path)
            if '.' in path:
                maxlen=max(maxlen, pathlen[depth]+len(path))
            else:
                pathlen[depth+1]=pathlen[depth]+1+len(path)
        return maxlen
