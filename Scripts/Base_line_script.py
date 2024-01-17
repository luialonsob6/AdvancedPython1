"""
Script to make updates in github
"""
import pandas as pd
import click


class FilteringClass:
    """
    Class for filtering
    """

    def __init__(self, df):
        self.df = df

    def filter_price(self, price):
        """
        filter by price
        """
        return self.df[self.df["Price Starting With ($)"] < price]


def load_dataset(filename):
    """
    Function to load dataset
    """
    extension = filename.rsplit(".", 1)[-1]
    if extension == "csv":
        return pd.read_csv(filename)
    else:
        raise TypeError(
            f"The extension is {extension} and not csv, try again"
        )  # Hacemos un raise del error(lo mismo que en el try and except)


@click.command(short_help="parser to import dataset")
@click.option("-i", "--input", required=True, help="File to import")
def main(input):
    """
    Main Function
    """
    df = load_dataset(input)
    result = FilteringClass(df).filter_price(12)
    print(result.shape)


if __name__ == "__main__":
    main()
