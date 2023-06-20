def chakravyuha(p,a,b,powers):
    
    # a = no. of enemies abhimanyu can skip
    # b = no. of abhimanyu can recharge his power
    # p = power of abhimanyu
    # here 'powers' are the enemy powers (i.e. k1,k2,...,k11)
    # since k3 and k7 will attack back after regenerating half of their powers in the next circle(i.e. k4 and k8)
    # the enemy powers will be k1,k2,k3,(k4+k3/2),k5,k6,k7,(k8+k7/2),k9,k10,k11.
    # if abimanyus max power < any of remaining enemies power then he can't cross the circle(He fails)
    # abhimanyu will skip 'a' enemies with highest power
    # battling in each circle will result in loss of the same power from abhimanyu as the enemy
    # abhimanyu can recharge his power 'b' times

    i = 0
    max_power = p   # maximum power of abhimanyu
    
    # changing k4,k8 powers as k3,k7 will regenerate with half of their powers and attack abhimanyu along with k4 and k8 respectively
    powers[3] = powers[3] + (powers[2]/2)   
    powers[7] = powers[7] + (powers[6]/2)

    sortedPowers = sorted(powers, reverse=True) # sorting and the enemy powers
    biggestPowers = sortedPowers[:a]    # abhimanyu will skip the enemies with these powers
    remainingPowers = sortedPowers[a:]

    # i assumed that abhimanyu can't recharge his powers in the middle of a battle
    if max_power < remainingPowers[0]:  # so, if abhimanyu maximum power < power of next highest enemy then he will lose the battle
        return False
    
    for j in range(11):     # replacing the powers of biggest/highest 'a' enemies with 0, as abhimanyu will skip these circles.
        if powers[j] in biggestPowers:
            powers[j] = 0

    while i < 11:   
        if p < powers[i]:
            if b > 0:       # before the battle if abhimanyu's power < enemy power then he will recharge his power to maximum
                b -= 1
                p = max_power - powers[i]
            else:           # if there are no recharges left, he will lose the battle
                return False
        else:
            p -= powers[i]

        i += 1
    return True

powers1 = [5, 10, 20, 30, 15, 25, 35, 40, 45, 50, 55]
powers2 = [10, 20, 30, 15, 25, 35, 20, 25, 30, 45, 40]

print(chakravyuha(100, 2, 2, powers1))
print(chakravyuha(100, 2, 1, powers2))