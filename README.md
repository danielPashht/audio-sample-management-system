# Audio Sample Library

This project is an audio sample library management system. It allows you to manage audio samples and their categories using a PostgreSQL database.

## Features

- Add, delete, and retrieve audio samples
- Add, delete, and retrieve categories
- Raw SQL execution using psycopg2

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/audio_sample_library.git
    cd audio_sample_library
    ```

2. Create a virtual environment and install dependencies:
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set up your PostgreSQL database and update the `DB_URL` in `constants.py`.

## Usage

Run the application:
```sh
python main.py