# StepScraper
StepScraper is a python script that hits a provided URL in increments of 50 (configurable) up to a maximum count. The script sends a GET request to each URL constructed and prints out the response text to the console. It's particularly useful when you want to scrape data from a web service that delivers information in paginated format.

## Getting Started
To get a local copy up and running, follow these simple steps.

### Prerequisites
The script uses `requests` library to send GET requests to the specified URL and `time` library to introduce a delay between successive requests. 

### Installation
1. Clone the repo
   ```
   git clone https://github.com/your_username_/StepScraper.git
   ```
2. Install required python packages
   ```
   pip install requests
   ```

## Usage
You should replace `[url]` in the script with the base URL that you want to send requests to. The script sends requests to URLs of the form `[url]0`, `[url]50`, `[url]100`, and so on, up until `[url]20000` by default. You can adjust these numbers according to your needs.

To run the script, simply navigate to the directory where the script is located and run the command:
```
python Steptember.py
```
You should start seeing the response text of the requests being printed out to the console.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## Azure DevOps Pipeline

This project includes a basic Azure DevOps pipeline configuration file for running tests using `pytest`. 

The pipeline is triggered manually (`trigger: none`), uses the Ubuntu-latest VM image, and tests the package on Python 3.7.

The pipeline follows these main steps:
1. Specify the Python version to use.
2. Install the dependencies listed in `requirements.txt`.
3. Run the `pytest` command to execute all the test cases.
4. Run the `StepScraper.py` script.

To use this pipeline, ensure that you've set up an Azure DevOps environment and have configured a pipeline using the included configuration file.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Created by [Zane Pearton](https://www.linkedin.com/in/zane-pearton/)
