import numpy as np
import ads5703 as t5703
from ads5703 import BankStatXlsx

logger = t5703.get_logger()


def test_rtgs_inwards_stat_01():
    bank_stat = BankStatXlsx.from_workbook("../data/202507.xlsx")
    res = bank_stat.init_rtgs_stat()
    assert res
    rtgs_df = bank_stat.clone_rtgs_stat()
    mask = (
        rtgs_df[["inw_inter_bank_vol", "inw_customer_vol", "inw_vol_total"]]
        .isna()
        .any(axis=1)
    )
    assert len(rtgs_df[mask]) > 0
    logger.info("test_rtgs_inwards_stat_01")


test_rtgs_inwards_stat_01()


def test_rtgs_reduce_tx_stat_01():
    bank_stat = BankStatXlsx.from_workbook("../data/202507.xlsx")
    res = bank_stat.init_rtgs_stat()
    assert res
    rtgs_df = bank_stat.clone_rtgs_stat()
    _inw_vol_total_ = rtgs_df["inw_inter_bank_vol"] + rtgs_df["inw_customer_vol"]
    assert (_inw_vol_total_ == rtgs_df["inw_vol_total"]).all()
    logger.info("test_rtgs_reduce_tx_stat_01")


test_rtgs_reduce_tx_stat_01()


def test_mobile_banking_df_01():
    bank_stat = BankStatXlsx.from_workbook("../data/202506.xlsx")
    res = bank_stat.init_mobile_banking_stat()
    assert res
    mb_df = bank_stat.clone_mobile_banking_stat()
    mask = mb_df[["vol", "val", "cust_count"]].isna().any(axis=1)
    assert len(mb_df[mask]) == 0
    logger.info("test_mobile_banking_df_01")


test_mobile_banking_df_01()


def test_neft_df_01():
    bank_stat = BankStatXlsx.from_workbook("../data/202505.xlsx")
    res = bank_stat.init_neft_stat()
    assert res
    logger.info("test_neft_df_01 - NEFT stat is available")

    neft_df = bank_stat.clone_neft_stat()
    print(neft_df[neft_df["bank"] == "PAYTM PAYMENTS BANK LIMITED"].values)
    # print(neft_df[neft_df["in_vol"] >= 200000].values)
    _mask_zero_tx_vol_ = neft_df["in_vol"] == 0
    len(neft_df[_mask_zero_tx_vol_]) == 1

    public_sector_stat = neft_df[neft_df["bank"].isin(t5703.PublicSectorBanks)]
    assert len(public_sector_stat) == len(t5703.PublicSectorBanks)
    assert public_sector_stat.shape[0] == len(t5703.PublicSectorBanks)
    assert public_sector_stat["in_vol"].count() == len(t5703.PublicSectorBanks)

    mask = neft_df[["in_vol", "in_val", "out_vol", "out_vol"]].isna().any(axis=1)
    assert len(neft_df[mask]) == 0


test_neft_df_01()
