## Algs for finding frequent itemsets

# Apriori
  * Any nonempty subset of a frequent itemset must be frequent
  * If `c` is not frequent, all the sets containing `c` are pruned
  * ![graph](./images/apriori.png)
  * ![visual execution](./images/apriori2.png)
    * Candidate generation to find valuable itemset
    * ![visual execution 2](./images/apriori3.png)
    * ![visual execution 3](./images/apriori4.png) 
FP-Growth
