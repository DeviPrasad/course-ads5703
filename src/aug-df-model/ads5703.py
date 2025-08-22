import sys
import logging
import re
import string
import numpy as np
import pandas as pd
from decimal import Decimal, InvalidOperation as DecimalInvalidOp

_logger_ = None

PublicSectorBanks = [
    "BANK OF BARODA",
    "BANK OF INDIA",
    "BANK OF MAHARASHTRA",
    "CANARA BANK",
    "CENTRAL BANK OF INDIA",
    "INDIAN BANK",
    "INDIAN OVERSEAS BANK",
    "PUNJAB AND SIND BANK",
    "PUNJAB NATIONAL BANK",
    "STATE BANK OF INDIA",
    "UCO BANK",
    "UNION BANK OF INDIA",
]


def get_logger():
    global _logger_
    if _logger_ is None:
        log_format = "%(asctime)s %(levelname)s - %(message)s"
        formatter = logging.Formatter(log_format)
        handler = logging.StreamHandler(sys.stderr)
        # handler.setLevel(logging.DEBUG)
        handler.set_name("root")
        handler.setFormatter(formatter)
        _logger_ = logging.getLogger()
        _logger_.setLevel(logging.DEBUG)
        _logger_.handlers = [handler]

    return logging.getLogger()


class BankStatXlsx:
    def __init__(self):
        self.workbook = None
        self.neft_df = None
        self.mobile_df = None

    def clone_neft_stat(self):
        return self.neft_df.copy(deep=True)

    def clone_rtgs_stat(self):
        return self.rtgs_df.copy(deep=True)

    def clone_mobile_banking_stat(self):
        return self.mobile_df.copy(deep=True)

    def from_workbook(docpath):
        logger = get_logger()
        try:
            workbook = open(docpath, "rb")
            bx = BankStatXlsx()
            bx.workbook = workbook
            return bx
        except Exception as ex:
            logger.error(str(ex))

        return None

    def init_neft_stat(self):
        self.neft_df = BankStatXlsx._neft_df_(self.workbook)
        # print(self.neft_df)
        return self.neft_df is not None

    def init_rtgs_stat(self):
        self.rtgs_df = BankStatXlsx._rtgs_df_(
            self.workbook,
        )
        # print(self.rtgs_df)
        return self.rtgs_df is not None

    def _neft_df_(workbook):
        try:
            df = pd.read_excel(
                workbook,
                "NEFT",
                # engine="openpyxl",
                usecols=[1, 2, 3, 4, 5, 6],
                skiprows=3,
                skipfooter=1,
                dtype={
                    "in_vol": "Int64",
                    "in_val": "Float64",
                    "out_vol": "Int64",
                    "out_val": "Float64",
                },
                names=["sln", "bank", "in_vol", "in_val", "out_vol", "out_val"],
            )
            return df
        except Exception as ex:
            pass

        return None

    def _rtgs_df_(workbook):
        try:
            df = pd.read_excel(
                workbook,
                "RTGS",
                # engine="openpyxl",
                usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                skiprows=4,
                skipfooter=1,
                dtype={
                    "inw_inter_bank_vol": "Int64",
                    "inw_customer_vol": "Int64",
                    "inw_vol_total": "Int64",
                    "inw_percent_val": "Float64",
                    "inw_inter_bank_val": "Float64",
                    "inw_customer_val": "Float64",
                    "inw_val_total": "Float64",
                    "inw_percent_val": "Float64",
                },
                names=[
                    "sln",
                    "bank",
                    "inw_inter_bank_vol",
                    "inw_customer_vol",
                    "inw_vol_total",
                    "inw_percent_vol",
                    "inw_inter_bank_val",
                    "inw_customer_val",
                    "inw_val_total",
                    "inw_percent_val",
                ],
            )
            return df
        except Exception as ex:
            print(ex)

        return None

    def init_mobile_banking_stat(self):
        self.mobile_df = BankStatXlsx._mobile_internet_df(
            self.workbook, "Mobile banking ", 4
        )
        if self.mobile_df is None:
            self.mobile_df = BankStatXlsx._mobile_internet_df(
                self.workbook, "Mobile banking", 4
            )
        if self.mobile_df is None:
            self.mobile_df = BankStatXlsx._mobile_internet_df(
                self.workbook, "Mobile Banking", 4
            )
        # print(self.mobile_df)
        return self.mobile_df is not None

    def _mobile_internet_df(workbook, sheet_name, skip_footer):
        try:
            df = pd.read_excel(
                workbook,
                sheet_name,
                # engine="openpyxl",
                usecols=[1, 2, 3, 4, 5],
                skiprows=2,
                skipfooter=skip_footer,
                names=["sln", "bank", "vol", "val", "cust_count"],
            )
            return df
        except Exception as ex:
            # print(ex)
            pass

        return None
