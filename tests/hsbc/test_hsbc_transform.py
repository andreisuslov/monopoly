from datetime import datetime

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from monopoly.banks.hsbc.credit import HsbcRevolution
from monopoly.constants import AMOUNT, DATE, DESCRIPTION


@pytest.mark.parametrize("statement_date", [datetime(2024, 1, 1)])
def test_hsbc_transform_cross_year(date_specific_hsbc: HsbcRevolution):
    raw_df = pd.DataFrame(
        [
            {
                DATE: "09 Jan",
                DESCRIPTION: "Shopee Singapore SINGAPORE SG",
                AMOUNT: "31.45",
            },
            {
                DATE: "12 Dec",
                DESCRIPTION: "UNIQLO SINGAPORE PTE. SINGAPORE SG",
                AMOUNT: "29.80",
            },
        ]
    )

    transformed_df = date_specific_hsbc.transform(raw_df)

    expected_data = pd.DataFrame(
        [
            {
                DATE: "2024-01-09",
                DESCRIPTION: "Shopee Singapore SINGAPORE SG",
                AMOUNT: 31.45,
            },
            {
                DATE: "2023-12-12",
                DESCRIPTION: "UNIQLO SINGAPORE PTE. SINGAPORE SG",
                AMOUNT: 29.80,
            },
        ]
    )

    assert_frame_equal(transformed_df, expected_data)


@pytest.mark.parametrize("statement_date", [datetime(2023, 7, 1)])
def test_ocbc_transform_within_year(date_specific_hsbc: HsbcRevolution):
    raw_df = pd.DataFrame(
        [
            {
                DATE: "09 Jun",
                DESCRIPTION: "Shopee Singapore SINGAPORE SG",
                AMOUNT: "31.45",
            },
            {
                DATE: "12 Jun",
                DESCRIPTION: "UNIQLO SINGAPORE PTE. SINGAPORE SG",
                AMOUNT: "29.80",
            },
        ]
    )

    transformed_df = date_specific_hsbc.transform(raw_df)

    expected_data = pd.DataFrame(
        [
            {
                DATE: "2023-06-09",
                DESCRIPTION: "Shopee Singapore SINGAPORE SG",
                AMOUNT: 31.45,
            },
            {
                DATE: "2023-06-12",
                DESCRIPTION: "UNIQLO SINGAPORE PTE. SINGAPORE SG",
                AMOUNT: 29.80,
            },
        ]
    )

    assert_frame_equal(transformed_df, expected_data)