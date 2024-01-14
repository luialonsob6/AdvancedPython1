"""
Script to make updates in github
"""
import pandas as pd
import click

@click.command(short_help="parser to import dataset")
@click.option("-i","--input",required=True, help="File to import")

def main():
    """
    Main Function
    """
    df = pd.read_csv(input)
    print(df.shape)

if __name__=="__main__":
    main()