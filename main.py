from random import randint as ri

def goldc(waterline):
    if waterline >= 73:
        r = ri(1, 1000)
        if r <= 6 + 60 * (waterline - 72):
            return 1
        else:
            return 0
    else:
        r = ri(1, 1000)
        if r <= 6:
            return 1
        else:
            return 0

def goldw(waterline):
    if waterline >= 63:
        r = ri(1, 1000)
        if r <= 7 + 60 * (waterline - 62):
            return 1
        else:
            return 0
    else:
        r = ri(1, 1000)
        if r <= 7:
            return 1
        else:
            return 0
        
# 保存卡池状态：
#     是否大保底、水位、明光
lc = [        0,    0,   1]
lw = [        0,    0]
#保存高级参数：
#      对两把武器的接受度
lst = [               0]

lc[0] = int(input("角色池是否大保底（1/0）："))
lc[1] = int(input("角色池水位："))
lc[2] = int(input("角色池明光："))

lw[0] = int(input("武器池是否大保底（1/0）："))
lw[1] = int(input("武器池水位："))

balls = int(input("粉球数："))
target = input("抽取序列：")
lst[0] = int(input("对两把武器的接受度：")) 

def acceptweapon(x):
    if x == 1:
        return 750
    else:
        return 375

def chouka(lc, lw, balls, target, lst):
    tarpointer = 0  # 指示当前所处的抽卡目标
    anotherweapon = 0
    while balls > 0 and tarpointer < len(target):
        balls -= 1
        if target[tarpointer] == "c":           
            if goldc(lc[1]):
                lc[1] = 0
                if lc[0] == 1:# 大保底
                    tarpointer += 1
                    lc[0] = 0
                elif lc[2] == 3:# 小保底·捕获明光必不歪
                    tarpointer += 1
                    if lc[2] > 0:
                        lc[2] -= 1
                else:# 小保底·明光未满3
                    r = ri(0,1)
                    if r:#没歪
                        lc[0] = 0
                        if lc[2] > 0:
                            lc[2] -= 1
                        tarpointer += 1 
                    else:
                        lc[0] = 1
                        lc[2] += 1    
            else:
                lc[1] += 1
        else:           
            if goldw(lw[1]):
                lw[1] = 0
                if lw[0] == 1:#大保底
                    tarpointer += 1
                    lw[0] = 0   
                else:#小保底
                    r = ri(1,1000)
                    if r <= acceptweapon(lst[0]):#没歪
                        lw[0] = 0
                        tarpointer += 1
                    else:
                        lw[0] = 1
                        if lst[0] == 3 and r <= 750:
                            anotherweapon += 1
            else:
                lw[1] += 1
    return tarpointer,anotherweapon
m = 0
out = {}
for i in range(100000):
    c = list(chouka(lc[:],lw[:],balls,target,lst[:]))
    if c[0] == len(target):
        m += 1
    if tuple(c) in out.keys():
        out[tuple(c)] += 0.00001
    else:
        out[tuple(c)] = 0.00001
    if i % 10000 == 0:
        print("-",end="",flush=True)
print("",end="\n")
print(f"总体成功率：{m/100000}")
print("详细情况：")
rounded_out = {k: round(v, 2) for k, v in out.items()}
print(rounded_out)
t = input("Press any key to exit...")