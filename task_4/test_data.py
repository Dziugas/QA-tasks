import os

import pytest
from click.testing import CliRunner

from task_4.upper_case_file import upper_case_file


directory_name = "data"
data_files = os.listdir(directory_name)

input_files = [file for file in data_files if "input" in file]
output_files = [file for file in data_files if "output" in file]
test_files = zip(input_files, output_files)


def test_upper_case_file(tmp_path):
    for files in test_files:
        input_file = files[0]
        input_file = f'{directory_name}/{input_file}'

        output_file = files[1]
        output_file = f'{directory_name}/{output_file}'

        with open (output_file, "r") as output_file:
            output_data = output_file.read()

        test_output = tmp_path/"test_output.txt"

        runner = CliRunner()
        runner.invoke(upper_case_file, ["--input-file", input_file, "--output-file", test_output])

        with open(test_output, "r") as test_output:
            test_text = test_output.read()

        assert output_data == test_text