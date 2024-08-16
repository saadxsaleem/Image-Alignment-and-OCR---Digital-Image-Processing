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
    git clone https://github.com/yourusername/document-alignment-ocr.git
    ```
2. Navigate to the project directory:
    ```bash
    cd document-alignment-ocr
    ```
3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```
5. Apply migrations to set up the database:
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

### Configuration

- **Filters**: Adjust filter parameters in the Django admin interface or update settings in `settings.py`.
- **OCR Settings**: Configure OCR settings in `ocr_config.py` or through the admin interface.

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/YourFeature
    ```
3. Commit your changes:
    ```bash
    git commit -am 'Add new feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/YourFeature
    ```
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Special thanks to the open-source libraries and tools used in this project.
- Credits to the contributors who provided feedback and suggestions.

---

Feel free to connect if you have any questions or need further assistance!

