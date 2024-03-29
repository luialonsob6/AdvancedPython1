"""
Script to make updates in github
"""
import os
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
        return self.df[self.df["Year"] == (year)]


@click.command(short_help="parser to import dataset")
@click.option("-i", "--input", required=True, help="File to import")
@click.option("-o", "--output", default="outputs", help="Path to output")
@click.option("-f", "--filtering", is_flag=True, help="Set a filtering or not")
@click.option("-g", "--genre", help="Filter by a desired genre", required=True)
@click.option("-y", "--year", help="Filter minimum year", required=True)
def main(input, output, filtering, genre, year):
    """
    Main Function
    """
    try:
        df = pd.read_csv(input)
        print(f"The file imported is:'{input}'")
    except FileNotFoundError as e:
        print(f"The file:'{e}' was not found")

    print(df.shape)
    print(df.info())

    import pdb

    pdb.set_trace()

    if filtering:
        print(
            "Print shape from Dataset that correspond to the genre:",
            genre,
            "and the year:",
            year,
        )
        df = FilteringClass(df).by_genre(genre)
        df = FilteringClass(df).exact_year(float(year))
        print(df.shape)

    if not os.path.exists(output):
        os.makedirs(output)

    df.to_csv(f"{output}/final_df.csv", index=None)


if __name__ == "__main__":
    main()
