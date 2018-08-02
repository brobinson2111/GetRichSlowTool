import click

@click.command()
@click.option(
    '--total_capitol',
    required=True,
    type=int,
    prompt='Total Capitol',
    help='This is the total capitol to distribute across Stocks. Please provide an integer value.')
@click.option(
    '--number_of_days_to_spend',
    required=True,
    type=int,
    prompt='Number of Days To Spend',
    help='This is the number of days for which the capitol is to be distributed. Please provide an integer value.')
@click.option(
    '--output_location',
    required=True,
    prompt='Output Location',
    help='This is the location on the disc where a file with the output will be produced.')
def get_rich_slowly(total_capitol, number_of_days_to_spend, output_location):
    print("This is the total capitol: " + str(total_capitol))
    print("This is the number of days to spend: " + str(number_of_days_to_spend))
    print("This is the output location: " + output_location)


if __name__ == '__main__':
    get_rich_slowly()