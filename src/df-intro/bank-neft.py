from decimal import Decimal, InvalidOperation as DecimalInvalidOp
import pandas as pd
import re
import string
from string import ascii_letters


def to_decimal(v):
    try:
        v2 = str(v).strip(string.ascii_letters)
        v2 = re.sub(r"[, \s\t\n]+", "", v2)
        decimal = Decimal(v2)
    except DecimalInvalidOp:
        decimal = Decimal(0)

    return decimal


class NEFTStat:
    @staticmethod
    def from_raw_data(bank_names, inward_tx_counts, amounts):
        assert len(bank_names) == len(inward_tx_counts)
        assert len(bank_names) == len(amounts)

        inward_tx_counts = [max(c, 0) for c in inward_tx_counts]
        amounts = map(to_decimal, amounts)

        return NEFTStat(
            {
                "BANK_NAME": bank_names,
                "INWARD_TX_COUNT": inward_tx_counts,
                "AMOUNT": amounts,
            }
        )

    def __init__(self, neft_dict):
        self.df = pd.DataFrame(neft_dict)

    def amounts(self):
        return self.df["AMOUNT"]

    def validate(self):
        neft_total = self.amounts().sum()
        assert neft_total == Decimal("2272714.99")


def test_neft_abstraction():
    neft_stat = NEFTStat.from_raw_data(
        [
            "AXIS BANK",
            "BANK OF BARODA",
            "CANARA BANK",
            "HDFC BANK",
            "ICICI BANK LTD",
            "IDBI BANK",
            "STATE BANK OF INDIA",
        ],
        [
            23568611,
            64204188,
            38418448,
            61299190,
            32313166,
            12238743,
            187499773,
        ],
        [
            "373781.27",
            "130123.47",
            " 98136 .52",
            "  597782.83",
            "360140.49",
            "55831.06,,",
            "656919.35abc",
        ],
    )
    neft_stat.validate()


if __name__ == "__main__":
    test_neft_abstraction()
