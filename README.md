# Document Alignment and OCR Application

## Overview

This Django application enhances document processing and analysis. It aligns document images based on their contours, applies image filters, performs Optical Character Recognition (OCR), and extracts text into a notepad file.

## Features

- **Document Alignment**:

  - Detects document edges and contours.
  - Applies a perspective transformation to correct orientation and achieve a top-down view.
  - Ensures accuracy for subsequent processing.

- **Image Filters**:

  - Adjusts brightness, saturation, and rotation to enhance image quality.

- **Optical Character Recognition (OCR)**:

  - Extracts and recognizes text from aligned images.

- **Text Extraction**:
  - Downloads extracted text as a notepad file for easy access and further processing.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Django 3.2 or higher
- Required libraries (see `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/saadxsaleem/Image-Alignment-and-OCR---Digital-Image-Processing.git
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

### Usage

1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
2. Access the application in your web browser at `http://127.0.0.1:8000/`.
3. Upload your document images via the web interface.
4. The aligned images, filtered results, and extracted text files will be available for download.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to connect if you have any questions or need further assistance!
