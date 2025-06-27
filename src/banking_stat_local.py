import sys
import logging
import numpy as np
import pandas as pd
from decimal import Decimal

logger = logging.getLogger(__name__)


def rtgs_data(xlsx, sheet_name):
    pass


def internet_banking_data(xls, sheet_names):
    def conv(x):
        if type(x) == str:
            return x
        return str(np.around(x, 2))

    for sheet_name in sheet_names:
        try:
            ib_df = pd.read_excel(
                xls,
                sheet_name,
                usecols=[1, 2, 3, 4, 5],
                skiprows=3,
                skipfooter=2,
                names=["Sln", "Bank", "Volume", "Value", "Active Customers"],
                converters={"Value": conv},
            )
            logger.info(
                f"internet_banking_data: found sheet '{sheet_name}' in '{xls.name}'"
            )
            return ib_df
        except Exception as ex:
            logger.error(f"internet_banking_data: {str(ex)} in '{xls.name}'")


def mobile_banking_data(xls, sheet_names):
    for sheet_name in sheet_names:
        try:
            ib_df = pd.read_excel(
                xls,
                sheet_name,
                usecols=[1, 2, 3, 4],
                skiprows=2,
                skipfooter=3,
                names=["Sln", "Bank", "Volume", "Value"],
            )
            logger.info(
                f"mobile_banking_data: found sheet '{sheet_name}' in '{xls.name}'"
            )
            return ib_df
        except Exception as ex:
            logger.error(f"mobile_banking_data: {str(ex)} in '{xls.name}'")
    return None


def xlsx(path):
    try:
        xls_doc = open(path, "rb")
        # print(xls_doc)
        return xls_doc
    except Exception as ex:
        logger.error(str(ex))
    return None


def test_banking_stat():
    rbi_docs = [
        (
            "/Users/dprasad/Downloads/RTGSNEFTAPRIL2025C5C14916CD804966A715D63CC56A1D24.XLSX",
            True,
            True,
        ),
        (
            "/Users/dprasad/Downloads/RTGSNEFTJAN25CD5E02D1321249779606FFE4BADF8439.XLSX",
            True,
            True,
        ),
        (
            "/Users/dprasad/Downloads/RTGSNEFTMISMARCH20251A8E4422C463474EBC88BF6BFC026A0B.XLSX",
            True,
            True,
        ),
        (
            "/Users/dprasad/Downloads/NEFT122020A5CD3A009E1B45ADAFAA5EF5038476F9.XLSX",
            False,
            True,
        ),
    ]
    for doc, has_ib, has_mb in rbi_docs:
        logger.info(f"reading {doc}")
        xls_doc = xlsx(doc)
        assert xls_doc is not None
        ibd = internet_banking_data(xls_doc, ["Internet Banking", "Internet Banking "])
        assert not has_ib or ibd is not None
        mbd = mobile_banking_data(
            xls_doc,
            [
                "Mobile ",
                "Mobile banking ",
                "Mobile",
                "Mobile banking",
                "Mobile Banking",
            ],
        )
        assert not has_mb or mbd is not None


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.DEBUG)
    handler.set_name("root")
    log_format = "%(asctime)s %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info("started..")
    test_banking_stat()
