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
    
    def filter_price(self,price):
        """
        filter by price
        """
        return self.df[self.df["Price Starting With ($)"] < price]

@click.command(short_help="parser to import dataset")
@click.option("-i","--input",required=True, help="File to import")

def main():
    """
    Main Function
    """
    df = pd.read_csv(input)
    result = FilteringClass(df).filter_price(12)
    print(result.shape)

if __name__=="__main__":
    main()