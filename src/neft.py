"""
NATIONAL ELECTRONIC FUNDS TRANSFER (NEFT) - APRIL 2025
    (RTGSNEFTAPRIL2025C5C14916CD804966A715D63CC56A1D24.XLSX)

+--------------------------------------------------------------------------------------------------+
Sln.       Bank Name                       Received Inward Credits          Total Outward Debits
                                           Inward Txs      Amount        Outward Txs      Amount
                                            (Count)     (Rs. Crore)       (Count)	  (Rs. Crore)
+--------------------------------------------------------------------------------------------------+
1     ABHYUDAYA CO-OP BANK LTD              409607          913.70           105882         422.50
2     AHMEDABAD MERCANTILE COOP BANK.        69167          385.19            42184         491.42
3     AHMEDNAGAR MERCHANTS CO-OP BANK LTD    27226          220.27            22818         164.56
4     AIRTEL PAYMENTS BANK LIMITED.        6500482         3023.64          1619880       33862.34
5     AKOLA DISTRICT CENTRAL CO-OP BANK      78364          358.09            20340         123.84
...
233   WOORI BANK                              1777         1588.91             7356         364.40
234   YES BANK.                            4843708        99283.56        156820269      267225.22
235   ZILA SAHKARI BANK LTD GHAZIABAD.       17055           50.61             2630          35.70
+--------------------------------------------------------------------------------------------------+
Total (No. of transactions in actuals
       and Amount in Rs. crore)          768751744      3897347.90        768751744     3897347.90
+--------------------------------------------------------------------------------------------------+

"""

"""
Notice each row in the table represents one logical unit of data containing
    - text representing bank names
    - non-negative numbers representing count of transactions
    - decimal numbers (two decimal places) representing amount in INR crores

"""

"""

We should be able to represent such simple data in our programs
even before we start thinking about processing such data.

"""
