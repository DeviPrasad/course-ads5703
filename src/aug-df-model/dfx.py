import os
import random
import numpy as np
import pandas as pd


def random_int():
    return int.from_bytes(os.urandom(4)) // 253


"""
list comprehensions.
(1) How would you generate an array of strings such as A34751, B103, etc?
(2) How would you generate an array of strings such as ZVO11666, LMH4659817, etc?
"""


def test_random_string():
    print([random_int() for _ in range(7)])
    print(
        [
            "".join(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3)) + str(random_int())
            for _ in list("ABCDEFG")
        ]
    )


# test_random_string()


"""
(1) run with 'vol' as a simple list of random_int()s.
    What is the type of 'vol' returned by pd.concat?
(2) run with 'rdf.vol' as pd.series with dtype=np.uint64

"""


def _create_banks_stat_random_():
    ndf = pd.DataFrame(
        {
            "vol": pd.Series([random_int() for _ in range(9)], dtype=np.uint64),
            "name": list("ABCDEFGKL"),
        }
    )
    rdf = pd.DataFrame(
        {
            "name": [c for c in "ABCDETUWXYZ"],
            "vol": pd.Series([random_int() for _ in "ABCDETUWXYZ"], dtype=np.uint64),
        }
    )
    ndf["type"], rdf["type"] = "NEFT", "RTGS"
    assert isinstance(ndf, pd.DataFrame)
    assert isinstance(rdf, pd.DataFrame)
    return (ndf, rdf)


def test_df_concat():
    (ndf, rdf) = _create_banks_stat_random_()
    print(pd.concat([ndf, rdf], ignore_index=True))


# test_df_concat()


def test_df_group_by_type_then_sum_vol():
    (ndf, rdf) = _create_banks_stat_random_()
    # consolidated dataframe
    cdf = pd.concat([ndf, rdf], ignore_index=True)
    assert isinstance(cdf, pd.DataFrame)

    # DataFrameGroupBy object of the consolidated dataframe
    assert type(cdf.groupby("type")) == pd.api.typing.DataFrameGroupBy
    print("-" * 40)
    for t, group in cdf.groupby("type"):
        print(f"    Type: {t}")
        print(f"        {group}\n")
    print("-" * 40)

    # project the 'vol' columns and sum up the values
    type_vol_sum = cdf.groupby("type")["vol"].sum()
    assert isinstance(type_vol_sum, pd.Series)
    print("-" * 40)
    print("Dataframe containing NEFT and RTGS sum")
    print(type_vol_sum)
    print("-" * 40)

    assert cdf[cdf["type"] == "NEFT"]["vol"].sum() == type_vol_sum["NEFT"]
    assert cdf[cdf["type"] == "RTGS"]["vol"].sum() == type_vol_sum["RTGS"]


test_df_group_by_type_then_sum_vol()


def test_df_group_by_name_then_sum_vol():
    (ndf, rdf) = _create_banks_stat_random_()
    # consolidated dataframe
    cdf = pd.concat([ndf, rdf], ignore_index=True)
    assert isinstance(cdf, pd.DataFrame)

    name_vol_sum = cdf.groupby("name")["vol"].sum()
    assert isinstance(name_vol_sum, pd.Series)
    # sum contributions from NEFT and RTGS and verify it against the groupby sum
    assert cdf[cdf["name"] == "A"]["vol"].sum() == name_vol_sum["A"]
    assert cdf[cdf["name"] == "B"]["vol"].sum() == name_vol_sum["B"]
    assert cdf[cdf["name"] == "Z"]["vol"].sum() == name_vol_sum["Z"]
    assert cdf[cdf["name"] == "G"]["vol"].sum() == name_vol_sum["G"]


test_df_group_by_name_then_sum_vol()


"""
Introduce public sector banks to the mix!
"""

PublicSectorBankNames = [
    "F",
    "G",
    "T",
    "U",
    "V",
    "I",
    "P",
    "Q",
    "Z",
]


def test_neft_rtgs_pub_prv_banks():
    (ndf, rdf) = _create_banks_stat_random_()
    cdf = pd.concat([ndf, rdf])
    cdf["sector"] = "PRIVATE"
    # what is the output of the following statement?
    print(cdf["name"].isin(PublicSectorBankNames))
    # how does the following statement work?
    cdf.loc[cdf["name"].isin(PublicSectorBankNames), "sector"] = "PUBLIC"


test_neft_rtgs_pub_prv_banks()


def test_df_sum():
    (ndf, rdf) = _create_banks_stat_random_()

    name_sum_df = ndf[["name"]] + rdf[["name"]]
    assert isinstance(name_sum_df, pd.DataFrame)
    print(name_sum_df)

    name_sum_df["vol"] = ndf[["vol"]].add(rdf[["vol"]], fill_value=0)
    name_sum_df["vol"] = name_sum_df["vol"].astype(np.uint64)
    print(name_sum_df)


# test_df_sum()
