# Stakefish: Approach to solving the problem using Probability and Statistics

First, we leverage BigQuery to pull data from 'bigquery-public-data.bitcoin_blockchain.blocks' to give us data on when bitcoin blocks are mined. Then we calculate the average time difference between the blocks, which will be used in future calculations.

Let  π  equal the time in hours to the next block being mined in the Bitcoin network. By the Poisson Process definition,  πβΌπΈπ₯π(π) and  π=60 / avgDiffMin so our lambda value ends up being 6.38.

Let  π  equal the number of times a block is mined until and including one block is mined more than 2 hours after the previous block. This can be modeled via a geometric distribution, with success probability of π(π>2).

Let  π  equal the total duration in hours until a block is mined 2 hours after the previous block was mined. The equation for this random variable is  π=πβπ . Our final solution will be the term  πΈ(π) , which represents the average duration until a block is mined 2 hours after the previous block was mined. We can assume that π is independent of π by our assumption of a Poission Process since a new block is mined independently of previous waiting times between blocks being mined so πΈ(π)=πΈ(πβπ)=πΈ(π)βπΈ(π).

E(Y) will be the inverse of π(π>2), which can be represented as 1βπΉπ(2). πΉπ(2) can be expressed as 1βπβ2π which leads us to believe that π(π>2) = πβ2π, thereby setting E(Y) = 1/πβ2π.

Since E(Z) = E(X) * E(Y), we can express our solution as 1/π * 1/π(π>2) which is equivalent to 1/ππβ2π. Replacing lambda with 6.38 and solving for E(Z), we end up with 6.20655129079743 years as the answer to our first question.

To answer the second question, we sum up all the instances from our 'bigquery-public-data.bitcoin_blockchain.blocks' where the block time differences are greater than 2 hours, which gives us 141.
