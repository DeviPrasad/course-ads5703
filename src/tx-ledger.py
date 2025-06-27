"""
We will develop a simple method for maintaining loan account transactions.

A transaction is represented by the following data:
    tx_id: unique uuid per transaction.
    acc_num: ten digit loan account number.
    tx_date: date of transaction (YYYY-MM-DD).
    gl_acc_code: code representing the general ledger account type.
    amount: amount in INR - a decimal number with two decimal places.
    tx_code: debit/credit - D/C.
    value_date: value realization date (YYYY-MM-DD).
    tx_time: unix timestamp.
    entry_type: loan operation - OPEN, CLOSE, RECEIPT, AUCTION, WRITE_OFF.
    tx_desc: unstructured text.

Notice that
    - There are many different elementary data types
        - string, number, uuid, date, and timestamp

We need a composite data type to represent a transaction per se.
Python defines tuple data type for grouping data.
A tuple can be viewed and used as a single, logical unit of data.
"""

"""
Exchange rate details:
    tx_id: unique uuid per transaction.
    currency: INR, USD, GBP, EUR, CAD, AUD, JPY, RUR.
    amount_from: decimal number.
    amount_to: decimal number.
    rate: exchange rate for the transaction - a decimal number.
"""
