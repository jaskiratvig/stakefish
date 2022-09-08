import numpy as np
import pandas as pd
from google.cloud import bigquery


def main():
    bigqueryClient = bigquery.Client('clear-arbor-279319')

    sqlQuery = """
    #standardSQL
    SELECT timestamp
    FROM `bigquery-public-data.bitcoin_blockchain.blocks`
    ORDER BY timestamp
    """

    job = bigqueryClient.query(sqlQuery)
    vals = list(job.result())
    times = pd.DataFrame(data=[list(y.values()) for y in vals], columns=list(vals[0].keys()))

    timeDiff = times['timestamp'].diff()
    avgDiffMin = np.mean(timeDiff) / 1000 / 60

    lambdaVal = 60 / avgDiffMin
    occ = 1 / (lambdaVal * np.e ** (-2 * lambdaVal)) / 24 / 365
    print("Bitcoin network sees two consecutive blocks mined more than 2 hours apart from each other once every ", occ, "years")

    count = sum(timeDiff > 2 * 1000 * 60 * 60)
    print("The above has happened ", count, " times so far in the history of Bitcoin.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
