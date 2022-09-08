# Stakefish: Approach to solving the problem using Probability and Statistics

First, we leverage BigQuery to pull data from 'bigquery-public-data.bitcoin_blockchain.blocks' to give us data on when bitcoin blocks are mined. Then we calculate the average time difference between the blocks, which will be used in future calculations.

Let  𝑋  equal the time in hours to the next block being mined in the Bitcoin network. By the Poisson Process definition,  𝑋∼𝐸𝑥𝑝(𝜆) and  𝜆=60 / avgDiffMin so our lambda value ends up being 6.38.

Let  𝑌  equal the number of times a block is mined until and including one block is mined more than 2 hours after the previous block. This can be modeled via a geometric distribution, with success probability of 𝑃(𝑋>2).

Let  𝑍  equal the total duration in hours until a block is mined 2 hours after the previous block was mined. The equation for this random variable is  𝑍=𝑋∗𝑌 . Our final solution will be the term  𝐸(𝑍) , which represents the average duration until a block is mined 2 hours after the previous block was mined. We can assume that 𝑌 is independent of 𝑋 by our assumption of a Poission Process since a new block is mined independently of previous waiting times between blocks being mined so 𝐸(𝑍)=𝐸(𝑋∗𝑌)=𝐸(𝑋)∗𝐸(𝑌).

E(Y) will be the inverse of 𝑃(𝑋>2), which can be represented as 1−𝐹𝑋(2). 𝐹𝑋(2) can be expressed as 1−𝑒−2𝜆 which leads us to believe that 𝑃(𝑋>2) = 𝑒−2𝜆, thereby setting E(Y) = 1/𝑒−2𝜆.

Since E(Z) = E(X) * E(Y), we can express our solution as 1/𝜆 * 1/𝑃(𝑋>2) which is equivalent to 1/𝜆𝑒−2𝜆. Replacing lambda with 6.38 and solving for E(Z), we end up with 6.20655129079743 years as the answer to our first question.

To answer the second question, we sum up all the instances from our 'bigquery-public-data.bitcoin_blockchain.blocks' where the block time differences are greater than 2 hours, which gives us 141.
