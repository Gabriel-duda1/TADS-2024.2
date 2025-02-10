import pandas as pd

def create_example() -> pd.DataFrame:
    """create a dataframe example,

    Returns:
        pd.DataFrame: _description_
    """

    tabela = pd.DataFrame({
    'Nome': ['Renata' , 'Anderson' , 'Paulo' ],
    'Nota': [10, 5, 5],
    'Nota2': [7, 3, 6],
})

    return tabela 