import math
from time import time
import numpy as np
import matplotlib.pyplot as plt
import random

def log_brut(a, b, p) :
    a_i = a
    for i in range(1, p) :
        if a_i%p == b :
            return i
        a_i = (a_i*a)%p
    return -1
    
def log_brut_t(a, b, p) :
    t = time()
    a_i = a
    for i in range(1, p) :
        if a_i%p == b :
            return i, time() - t
        a_i = (a_i*a)%p
    return -1   
    
def PGCD_Bezout(a, b) :
    if a%b == 0 :
        return (0, 1), b
    q = a//b
    r = a%b
    (k, l), d = PGCD_Bezout(b, r)
    return (l, k - l*q), d

def inv(a, p) :
    return (PGCD_Bezout(a, p)[0][0])%p
    
def id(n) :
    i = []
    for j in range(n) :
        i.append(j+1)
    return i
    
def prod_sn(s, c, n) :
    d = []
    for i in range(n) :
        d.append(s[c[i] - 1])
    return d
    
def inv_sn(s, n) :
    c = id(n)
    for i in range(n) :
        c[s[i]-1] = i + 1
    return c

def commun(l1, l2) :
    for i in range(len(l1)) :
        for j in range(len(l2)) :
            if l1[i] == l2[j] :
                return (i, j)
    return (-1, -1)

def Baby_Giant_Steps(a, b, p) :
    m = int(math.sqrt(p))
    a_m = pow(a, m, p)
    a_i = inv(a, p)
    baby = []
    giant = []
    for i in range(m) :
        baby.append((b*(pow(a_i, i, p)))%p)
        giant.append(pow(a_m, i, p))
    (q, r) = commun(giant, baby)
    return m*q + r
    
def Baby_Giant_Steps_t(a, b, p) :
    t = time()
    m = int(math.sqrt(p))
    a_m = pow(a, m, p)
    a_i = inv(a, p)
    baby = []
    giant = []
    for i in range(m) :
        baby.append((b*(pow(a_i, i, p)))%p)
        giant.append(pow(a_m, i, p))
    (q, r) = commun(giant, baby)
    return m*q + r, time() - t

def log_premier(a, b, p_i, e, p) :
    p_e = pow(p_i, e)
    a_p0 = pow(a, (p-1)/p_e, p)
    a_i = inv(a_p0, p)
    b_p = pow(b, (p-1)/p_e, p)
    a_p = pow(a_p0, p_i**(e - 1), p)
    x = 0
    
    for i in range(e) :
        l_i =  Baby_Giant_Steps(a_p, pow(b_p*(a_i**x), p_i**(e - i - 1), p), p)
        x = x + l_i*(p_i**i)
        
    return x%p_e
 
    
def decompo(x, p) :
    d = []
    while x != 0 :
        d.append(x%p)
        x = x//p
    return d
    
def premiers(n) :
    facteurs = []
    i = 2
    while i*i <= n :
        k = 0
        while n%i == 0 :
            k += 1
            n = n/i
        if k != 0 :
            facteurs.append((i, k))
        i += 1
    if n != 1 :
        facteurs.append((n, 1))
    return facteurs
    
def restes_chinois(l, n) :
    x = 0
    for i in l :
        x = x + i[0]*(PGCD_Bezout(n/i[1], i[1])[0][0])*(n/i[1])
    return x%n

def Pohlig_Helmann(a, b, p) :
    facteurs = premiers(p-1)
    congruence = []
    for i in facteurs :
        congruence.append((log_premier(a, b, i[0], i[1], p), i[0]**i[1]))
    return restes_chinois(congruence, p - 1)

def Pohlig_Helmann_t(a, b, p) :
    t = time()
    facteurs = recherche(Liste_facteur, p - 1)
    congruence = []
    for i in facteurs :
        congruence.append((log_premier(a, b, i[0], i[1], p), i[0]**i[1]))
    return (restes_chinois(congruence, p - 1), time() - t)
  
Carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911]  
Liste_premiers = [2, 3, 5, 7, 11, 13, 17, 19] 
  
def est_premier(n) :
    if n in Carmichael :
        return False
    for i in Liste_premiers :
        if n == i :
            return True
        if n%i == 0 :
            return False
    for i in range(10) :
        r = random.randint(2, n - 1)
        if pow(r, n - 1, n) != 1 :
            return False
    return True
    
def n_premiers(n) :
    l = []
    while(len(l)) <= 10 :
        if est_premier(n) :
            l.append(n)
        n += 1
    return l   
    
def liste_facteurs(n) :
    l = []
    for i in range(1, n) :
        p = 10**i
        for k in n_premiers(p) :
            l.append((k - 1, premiers(k - 1)))
    for i in range(1, n) :
        p = 5*10**i
        for k in n_premiers(p) :
            l.append((k - 1, premiers(k - 1)))
    for i in range(1, n) :
        p = 8*10**i
        for k in n_premiers(p) :
            l.append((k - 1, premiers(k - 1)))
    return l

Liste_facteur = liste_facteurs(10)

def recherche(l, e) :
    for i in l :
        if i[0] == e :
            return i[1]

def mesure(n) :
    T_b = []
    T_S = []
    T_P = []
    T = []
    for i in range(1, n) :
        p = 10**i
        T.append(p)
        l = n_premiers(p)
        for k in l :
            T_b_i = []
            T_S_i = []
            T_P_i = []
            T_b_i.append(log_brut_t(3, pow(3, k//2, k), k)[1])
            T_S_i.append(Baby_Giant_Steps_t(3, pow(3, k//2, k), k)[1])
            T_P_i.append(Pohlig_Helmann_t(3, pow(3, k//2, k), k)[1])
        T_b.append(np.mean(T_b_i))
        T_S.append(np.mean(T_S_i))
        T_P.append(np.mean(T_P_i))
        p = 5*10**i
        T.append(p)
        l = n_premiers(p)
        for k in l :
            T_b_i = []
            T_S_i = []
            T_P_i = []
            T_b_i.append(log_brut_t(3, pow(3, k//2, k), k)[1])
            T_S_i.append(Baby_Giant_Steps_t(3, pow(3, k//2, k), k)[1])
            T_P_i.append(Pohlig_Helmann_t(3, pow(3, k//2, k), k)[1])
        T_b.append(np.mean(T_b_i))
        T_S.append(np.mean(T_S_i))
        T_P.append(np.mean(T_P_i))
        p = 8*10**i
        T.append(p)
        l = n_premiers(p)
        for k in l :
            T_b_i = []
            T_S_i = []
            T_P_i = []
            T_b_i.append(log_brut_t(3, pow(3, k//2, k), k)[1])
            T_S_i.append(Baby_Giant_Steps_t(3, pow(3, k//2, k), k)[1])
            T_P_i.append(Pohlig_Helmann_t(3, pow(3, k//2, k), k)[1])
        T_b.append(np.mean(T_b_i))
        T_S.append(np.mean(T_S_i))
        T_P.append(np.mean(T_P_i))
    plt.plot(T, T_b, label = "log_brut")
    plt.plot(T, T_S, label = "Shanks")
    plt.plot(T, T_P, label = "Pohlig-Helmann")
    plt.xlabel("Taille du groupe")
    plt.ylabel("Temps (s)")
    plt.legend()
    plt.show()


def mesure_p(n) :
    T_S = []
    T_P = []
    T = []
    for i in range(1, n) :
        p = 10**i
        T.append(p)
        l = n_premiers(p)
        for k in l :
            T_S_i = []
            T_P_i = []
            T_S_i.append(Baby_Giant_Steps_t(3, pow(3, k//2, k), k)[1])
            T_P_i.append(Pohlig_Helmann_t(3, pow(3, k//2, k), k)[1])
        T_S.append(np.mean(T_S_i))
        T_P.append(np.mean(T_P_i))
        
        p = 5*10**i
        T.append(p)
        l = n_premiers(p)
        for k in l :
            T_S_i = []
            T_P_i = []
            T_S_i.append(Baby_Giant_Steps_t(3, pow(3, k//2, k), k)[1])
            T_P_i.append(Pohlig_Helmann_t(3, pow(3, k//2, k), k)[1])
        T_S.append(np.mean(T_S_i))
        T_P.append(np.mean(T_P_i))
        
        p = 8*10**i
        T.append(p)
        l = n_premiers(p)
        for k in l :
            T_S_i = []
            T_P_i = []
            T_S_i.append(Baby_Giant_Steps_t(3, pow(3, k//2, k), k)[1])
            T_P_i.append(Pohlig_Helmann_t(3, pow(3, k//2, k), k)[1])
        T_S.append(np.mean(T_S_i))
        T_P.append(np.mean(T_P_i))
    plt.plot(T, T_S, label = "Shanks")
    plt.plot(T, T_P, label = "Pohlig-Helmann")
    plt.legend()
    plt.show()  
    
def est_generateur(n, p) :
    if log_brut(n, 1, p) == p - 1 :
        return True
    else :
        return False
        
def relations(n, p, r) :
    rel = []
    for i in range(1, p) :
        d = premiers(pow(n, i, p))
        b = True
        for e in d :
            if e[0] > r :
                b = False
        if b == True :
            rel.append((i, d))
    return rel

def somme_facteurs(n) :
    m = 0
    facteurs = premiers(n)
    for i in facteurs :
        m += i[1]*math.sqrt(i[0])
    return m
    
def somme_facteurs_m(n) :
    m = 0
    for i in range(10) :
        m += plus_grand(n + i)
    return float(m)/10
        

def L(n) :
    return np.exp(math.sqrt(1.5*np.log(n)*np.log(np.log(n))))

def m(n) :
    T_S = []
    T_P = []
    T_c = []
    T = []
    for i in range(1, n) :
        p = 10**i
        T.append(p)
        T_S.append(math.sqrt(p))
        T_P.append(i**2 + somme_facteurs_m(p))
        T_c.append(L(p))
        p = 5*10**i
        T.append(p)
        T_S.append(math.sqrt(p))
        T_P.append(i**2 + somme_facteurs_m(p))
        T_c.append(L(p))
        p = 8*10**i
        T.append(p)
        T_S.append(math.sqrt(p))
        T_P.append(i**2 + somme_facteurs_m(p))
        T_c.append(L(p))
    plt.plot(T, T_S, label = "Shanks")
    plt.plot(T, T_P, label = "Pohlig-Helmann")
    plt.plot(T, T_c, label = "Calcul d'indice")
    plt.xlabel("Taille du groupe")
    plt.ylabel("Nombre d'operations elementaires")
    plt.legend()
    plt.show()         