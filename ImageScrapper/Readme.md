# Google Image Scraper

## Introduction

The **Google Image Scraper**  provides an efficient solution for collecting and organizing images at scale. It is made using Tkinter, Requests, and os libraries. With its intuitive graphical interface, users can specify search queries, select the number of images required, and manage their downloads seamlessly. It can be used to to streamline the process of gathering large datasets of images for training machine learning models.

## Features

- **Graphical Interface** for entering search queries and specifying the number of images to download.
- **Directory Selection** option to choose where the images will be saved.
- **Progress Indicator** to show the download status.
- **Automatic Folder Creation** for storing the images.
- **Efficient Data Collection** for machine learning model training.

## Dependencies

Ensure you have the following Python libraries installed:

- `tkinter` (built-in for Python)
- `requests`
- `BeautifulSoup` (part of `bs4` package)

You can install missing dependencies with:

```bash
pip install requests beautifulsoup4
```
## Usage
- Run the script using:

```bash
python script.py
```
- Enter the search query for images.

- Specify the number of images to download.

- Select a folder where the images will be stored.

- Wait for the progress indicator to complete.

- The images will be saved in the selected directory.

## Author
Developed by Santhosh.A

## Notes
- This scraper fetches images from Google Image search results.

- Due to changes in Google's structure, functionality may require updates.

- Use this tool responsibly, respecting web scraping policies and image copyrights.
