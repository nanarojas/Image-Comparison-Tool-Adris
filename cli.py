#!/usr/bin/env python3
import click
import image_diff_score

@click.command()
@click.option('--input_filename', prompt='Input filename',
              help='The name of the file to process')
@click.option('--output_filename', prompt='Output filename',
              help='The name of the file to write results to')
def process(input_filename, output_filename):
    """
    Processes the input file and writes the results to the chosen output
    """
    image_diff_score.process_csv(input_filename, output_filename)

if __name__ == '__main__':
    process()
