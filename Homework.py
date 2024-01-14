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
    
    def by_genre(self, genre):
        return self.df[self.df["Genre"] == genre]
    
    def exact_year(self, year):
        return self.df[self.df["Year"] == int(year)]
    
    def over_year(self, year):
        return self.df[self.df["Year"] > int(year)]
    
    def less_year(self,year):
        return self.df[self.df["Year"] < int(year)]
    
    

@click.command(short_help="parser to import dataset")
@click.option("-i","--input",required=True, help="File to import")
@click.option("-o", "--output", default="outputs", help="Path to the output folder")
@click.option("-g", "--genre", help="Filter by a desired genre", required=True)
@click.option("-y", "--year", help="Filter by a desired minimum year", required=True)


def main(input, output, genre, year):
    """
    Main Function
    """     
    df = pd.read_csv(input)

if __name__=="__main__":
    main()