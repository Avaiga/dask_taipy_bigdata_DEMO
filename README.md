# Intelligent Big Data Pipelines with Dask & Taipy

## Table of Contents
- [Usage](#usage)
- [About Taipy Core](#about-taipy-core)
- [Demo Type](#demo-type)
- [Directory Structure](#directory-structure)
- [License](#license)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)

## Usage

This README outlines the details and usage of the Dask & Taipy DEMO for building Big Data pipelines.

## About Taipy Core and this Project

Taipy is a Python library aimed at creating Business Applications. More information can be found on our [website](https://www.taipy.io).

This project, Intelligent Big Data Pipelines with Dask & Taipy, serves as a comprehensive demonstration of advanced data manipulation techniques for larger-than-memory datasets. It showcases how to construct robust data pipelines and highlights innovative features of Taipy Core, such as the ability to skip tasks within pipelines for optimized performance.

### Demo Type

- **Level**: Beginner/Intermediate
- **Topic**: Dask, Taipy-Core, Data Pipeline
- **Components/Controls**:
  - Taipy Core: DataNode, Pipeline, Scenario

## How to Run

The demo works with Python versions greater than 3.8. Install the dependencies from the `Pipfile` and run `app.ipynb` in the `src/` folder. A `requirements.txt` file is also available in the `src/` folder.

## Introduction

### Data Preprocessing and Customer Scoring

Reads customer data and calculates a customer score. The goal is to categorize customers based on different metrics.

### Feature Engineering and Segmentation

Additional features are added and customers are segmented into 'High Value' and 'Low Value' based on their scores.

### Segment Analysis

Performs detailed analysis on each customer segment.

### Additional Analysis

Conducts further statistical analyses based on segment analysis.

## Directory Structure

- `src/`: Contains the source code of the demo.
  - `src/algos`: Contains the functions executed as tasks by Taipy.
  - `src/config`: Contains the configuration files.
  - `src/data`: Contains the data files used in the application.
- `CODE_OF_CONDUCT.md`: Code of conduct for members and contributors.m
- `CONTRIBUTING.md`: Instructions for contributing to the project.
- `INSTALLATION.md`: Installation instructions.
- `LICENSE`: The Apache 2.0 License.
- `Pipfile`: Used by Pipenv to manage project dependencies.
- `README.md`: Current file.

## License

Copyright 2023 Avaiga Private Limited

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at [http://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)

## Contributing

To contribute to this project, please refer to the [`CONTRIBUTING.md`](CONTRIBUTING.md) file.

## Code of Conduct

For details on how to engage with the community, please refer to [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
