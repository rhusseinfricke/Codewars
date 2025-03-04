
#In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater than or equal to p = 1200 inhabitants?

def nb_year(p0, percent, aug, p):
    count = 1
    for i in range(1000):
        pop = (p0 + (percent/100)*p0) + aug
        if pop < p:
            p0 = pop
            count += 1
    else:
        return count