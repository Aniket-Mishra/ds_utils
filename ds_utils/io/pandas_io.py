from pathlib import Path
import pandas as pd
import numpy as np


def safe_write(df, filepath, index=False, **kwargs):
    """
    Write a DataFrame to disk.
    Creates parent directories if they do not exist.

    Parameters
    ----------
    df : pandas.DataFrame
    filepath : str or Path
    writer : str  ('csv', 'parquet', 'xlsx', etc.)
    kwargs : passed to pandas writer
    """

    path = Path(filepath).expanduser()

    # If relative → resolve from CWD
    if not path.is_absolute():
        path = Path.cwd() / path

    # Create directory tree if missing
    path.parent.mkdir(parents=True, exist_ok=True)
    suffix = path.suffix.lower()
    if suffix == "":
        path = path.with_suffix(".csv")
        df.to_csv(path, index=index, **kwargs)
    elif suffix == ".csv":
        df.to_csv(path, index=index, **kwargs)
    elif suffix == ".parquet":
        df.to_parquet(path, index=index, **kwargs)
    elif suffix == ".json":
        df.to_json(path, index=index, **kwargs)
    else:
        raise ValueError(f"Unsupported writer: {suffix}")
    return path
