# code_featurizer

This repository contains a token-based source code featurizer that converts lines of source code into numerical feature vectors. The featurizer uses tokens existing in a line as features, enabling machine learning and analysis on source code.

## Overview

The featurizer implements a method that:
1. Tokenizes source code lines by splitting on common delimiters
2. Identifies a minimal set of features (tokens) that can distinguish between different lines
3. Generates feature vectors where each element represents the frequency of a token in a line

This approach is particularly useful for code quality analysis, code review datasets, and machine learning applications on source code.

## Installation

### Prerequisites
- Python 3.x
- Jupyter Notebook (for the interactive notebook)
- pandas library

### Setup
```bash
# Clone the repository
git clone https://github.com/miroslawstaron/code_featurizer.git
cd code_featurizer

# Install required dependencies
pip install pandas jupyter
```

## How to Use

### Method 1: Using the Jupyter Notebook
Open `source_code_featurizer.ipynb` in Jupyter and run the cells to see the featurizer in action:
```bash
jupyter notebook source_code_featurizer.ipynb
```

The notebook contains detailed explanations and examples of the featurization process.

### Method 2: Using the Python Example
Run the standalone Python example:
```bash
python3 example_usage.py
```

This script demonstrates the complete workflow:
1. Load code from the example CSV file
2. Find an optimal feature set that distinguishes all unique lines
3. Generate feature vectors for each line
4. Save the results to an output CSV file

### Method 3: Integrating into Your Project
You can import the featurizer classes directly into your Python project. See `example_usage.py` for the complete implementation of:
- `FeatureMaker` - Creates feature vectors based on a defined set of features
- `DataSet` - Manages the connection between code lines and their feature vectors
- `findFeatureListIterative()` - Finds a minimal set of distinguishing features
- `featurizeListPredefined()` - Generates feature vectors using a predefined feature set

## Examples

The repository includes several examples to help you understand how to use the featurizer:

### 1. C Code Example (main.c)
A simple "Hello, World!" C program demonstrating the featurizer on C code.
- Input: `main.csv` - CSV file with the C code lines
- Output: `output_main.csv` - Featurized output
- Code: `main.c` - The original C source file

### 2. Python Calculator Example (example_calculator.py)
A complete Python calculator program showing how to use the featurizer with Python code.
- Input: `example_calculator.csv` - CSV file with the Python code lines
- Output: `output_example_calculator.csv` - Featurized output
- Code: `example_calculator.py` - The original Python source file
- Demo: `example_usage.py` - Standalone script demonstrating the featurizer

## What is Featurization?

The featurizer converts lines of source code into numerical feature vectors based on token frequencies. This is useful for:
- Code similarity analysis
- Machine learning on source code
- Code classification and clustering
- Pattern recognition in code
- Quality assessment of code review datasets
- Training models for automated code review

Each feature represents a token (like keywords, operators, identifiers), and the feature vector shows how many times each token appears in a given line. The algorithm iteratively finds the minimal set of features needed to uniquely distinguish all different lines of code.

## Citation

If you use this code featurizer in your research, please cite the following paper:

```bibtex
@inproceedings{staron2021improving,
  title={Improving quality of code review datasets--Token-based feature extraction method},
  author={Staron, Miroslaw and Meding, Wilhelm and S{\"o}der, Ola and Ochodek, Miroslaw},
  booktitle={International Conference on Software Quality},
  pages={81--93},
  year={2021},
  organization={Springer}
}
```

**Note**: The BibTeX entry uses ASCII transliteration for author names as per standard practice.

## License

See the LICENSE file for details.

## Author

Mirosław Staron
