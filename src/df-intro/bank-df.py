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


def create_neft_df():
    neft_apr_2025 = {
        "BANK_NAME": [
            "AXIS BANK",
            "BANK OF BARODA",
            "CANARA BANK",
            "HDFC BANK",
            "ICICI BANK LTD",
            "IDBI BANK",
            "STATE BANK OF INDIA",
        ],
        "COUNT_INWARD_TXS": [
            23568611,
            64204188,
            38418448,
            61299190,
            32313166,
            12238743,
            187499773,
        ],
        "AMOUNT": [
            "373781.27",
            "130123.47",
            "98136 .52",
            "597782.83",
            "360140.49",
            "55831.06,,",
            "656919.35abc",
        ],
    }

    df = pd.DataFrame(neft_apr_2025)
    assert df.index.size == 7
    assert df.shape == (7, 3)
    assert df.head(2)["BANK_NAME"].array == [
        "AXIS BANK",
        "BANK OF BARODA",
    ]
    assert df.tail(2).BANK_NAME.array == [
        "IDBI BANK",
        "STATE BANK OF INDIA",
    ]

    df["AMOUNT"] = df["AMOUNT"].map(to_decimal)
    try:
        neft_sum = pd.to_numeric(df["AMOUNT"], errors="coerce").sum()
        print(f"Sum = {neft_sum}")
    except:
        print("Sum raised an exception!")

    assert isinstance(df["AMOUNT"], pd.Series)

    assert df["AMOUNT"][0] == Decimal("373781.27")
    neft_total = df["AMOUNT"].sum()
    assert neft_total == Decimal("2272714.99")

    return df


def test_sorting(df):
    assert df["AMOUNT"][0] == Decimal("373781.27")
    # If ignore_index is True, the resulting axis will be labeled 0, 1, …, n - 1.
    df = df.sort_values("COUNT_INWARD_TXS", ignore_index=True)
    print(df)
    assert df["AMOUNT"][0] == Decimal("373781.27")


if __name__ == "__main__":
    df = create_neft_df()
    test_sorting(df)
