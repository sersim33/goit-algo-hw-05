# goit-algo-hw-05

Для пошуку підрядка який існує в статті №1 найбільш ефективними алгоритмами виявилися: КМП (0,001 seconds) і boyer_moore (0,0005 seconds)
Для підрядка якого нема: boyer_moore найбільш ефективний
 
Для статті №2:  boyer_moore найбільш ефективний як для пошуку підрядка який існує, так і для неіснуючого рядка.
В цілому, пошук в статті №2 займає більше часу порівняно зі статтею №1. Так як кількість символів різна:
Length of article 1: 12785
Length of article 2: 18467
 
Тож можна зробити висновок, що для невеликих об’ємів даних найбільш ефективний: boyer_moore
 

#kmp_search (Кнута-Морріса-Пратта)
 
1 article
Average time taken for kmp_search in (substring exists): 0.0011447500437498093 seconds
Average time taken for kmp_search (substring doesn’t exist): 0.1149977499153465 seconds
 
2 article
Average time taken for kmp_search (substring exists): 0.027414500014856458 seconds
Average time taken for kmp_search (substring doesn’t exist): 0.15030829200986773 seconds
 

#boyer_moore
 
1 article
Average time taken for boyer_moore_search: 0.0005421669920906425 seconds
Average time taken for boyer_moore_search: 0.01517579099163413 seconds
 
2 article
Average time taken for boyer_moore_search: 0.005582583020441234 seconds
Average time taken for boyer_moore_search: 0.019204583019018173 seconds
 
 
#rabin_karp_search
 
1 article
Average time taken for rabin_karp_search: 0.002784334006719291 seconds
Average time taken for rabin_karp_search: 0.26462420797906816 seconds
 
2 article
Average time taken for rabin_karp_search: 0.06817300000693649 seconds
Average time taken for rabin_karp_search: 0.3622362499590963 seconds

