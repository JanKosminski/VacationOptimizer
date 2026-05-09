# Vacation Optimizer

A straightforward tool that optimizes scheduling paid leave to maximize consecutive free days.

## Description

Upon launching, the program prompts you to input the number of paid leave days available. The output is generated using a heuristic Branch and Bound algorithm based on the Knapsack Problem.

The algorithm evaluates days between the current date and December 31st of the current year. The calendar is automatically populated with Polish national holidays, including movable holidays such as Easter and Corpus Christi. The output is designed to build optimal vacation blocks around these dates.

## Getting Started

### Dependencies

The program relies on the following Python modules:
* `pandas` (requires installation)
* `tkinter` (standard library, but may require system-level installation on some Linux distributions)
* `itertools` (standard library)
* `datetime` (standard library)
* `calendar` (standard library)

### Installation

Install the required third-party packages using pip:

```bash
pip install pandas
```

### Executing the program

Run the main script from your terminal or preferred IDE:

```bash
python main.py
```

## Authors

Jan Kośminski
