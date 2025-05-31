import pytest
import pandas as pd
import numpy as np
from io import StringIO
import sys
from simple_python.utils.data_frames import create_fancy_dataframe, print_dataframe_info

def test_create_fancy_dataframe():
    df = create_fancy_dataframe()
    
    # Test return type
    assert isinstance(df, pd.DataFrame)
    
    # Test columns
    expected_columns = ['A', 'B', 'C', 'D']
    assert all(col in df.columns for col in expected_columns)
    
    # Test number of rows
    assert len(df) == 5
    
    # Test data types
    assert df['A'].dtype == np.int64
    assert df['B'].dtype == object
    assert df['C'].dtype == np.float64
    assert pd.api.types.is_datetime64_any_dtype(df['D'])

def test_print_dataframe_info(capsys):
    # Create sample DataFrame
    df = pd.DataFrame({
        'A': [1, 2],
        'B': ['X', 'Y'],
        'C': [0.1, 0.2],
        'D': pd.date_range('2024-01-01', periods=2)
    })
    
    # Call function
    print_dataframe_info(df)
    
    # Capture output
    captured = capsys.readouterr()
    
    # Verify expected sections in output
    assert "DataFrame Head" in captured.out
    assert "DataFrame Info" in captured.out
    assert "DataFrame Description" in captured.out