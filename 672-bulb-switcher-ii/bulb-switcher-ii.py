class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n=min(n, 6)
        states=set()
        for mask in range(16):
            used=bin(mask).count("1")
            if used>presses or (presses-used)%2!=0:
                continue
            bulbs=[1]*n
            for button in range(4):
                if mask & (1<<button):
                    for i in range(n):
                        pos=i+1
                        if button==0:
                            bulbs[i]^=1
                        elif button==1 and pos%2==0:
                            bulbs[i]^=1
                        elif button==2 and pos%2==1:
                            bulbs[i]^=1
                        elif button==3 and pos%3==1:
                            bulbs[i]^=1
            states.add(tuple(bulbs))
        return len(states)