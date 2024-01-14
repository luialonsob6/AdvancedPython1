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
    try:
        df = pd.read_csv(input)
        print(f"The file imported is:'{input}'")
    except FileNotFoundError:
        print(f"The file:'{input}' was not found")
    
    
    Filter_genre = FilteringClass(df).by_genre(genre)
    Filter_exact_year = FilteringClass(df).exact_year(year)

    filtered_df = pd.concat([Filter_genre, Filter_exact_year], axis =0).drop_duplicates()

    print(df.shape())
    return filtered_df.shape()

if __name__=="__main__":
    main()