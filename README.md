# code_featurizer
This is a jupyter notebook file with the code for the source code featurizer, which uses tokens existing in a line as a feature. 

The code is commented directly in the file as a Markdown code.

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

## How to Use

### Using the Jupyter Notebook
Open `source_code_featurizer.ipynb` in Jupyter and run the cells to see the featurizer in action.

### Using the Python Example
Run the standalone Python example:
```bash
python3 example_usage.py
```

This will:
1. Load code from the example CSV file
2. Find an optimal feature set
3. Generate feature vectors for each line
4. Save the results to an output CSV file

## What is Featurization?

The featurizer converts lines of source code into numerical feature vectors based on token frequencies. This is useful for:
- Code similarity analysis
- Machine learning on source code
- Code classification
- Pattern recognition in code

Each feature represents a token (like keywords, operators, identifiers), and the feature vector shows how many times each token appears in a given line.
