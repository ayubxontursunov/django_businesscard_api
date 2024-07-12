# Business Card Generator API


![Django REST framework Logo](https://www.django-rest-framework.org/img/logo.png)


Welcome to the Business Card Generator project! This project allows users to create elegant and personalized business cards using a Django REST framework. The project provides an API for users to input their details and generate a business card image.

## Features

- **Generate Business Cards**: Create a personalized business card with user-provided information.
- **Elegant Designs**: Choose from multiple elegant card designs.
- **REST API**: Use a simple REST API to submit user details and download the generated card.
- **Temporary Data Storage**: Personal data is not stored in the database, ensuring privacy.

## Project Structure

- **app**: Contains the Django application.
- **media**: Directory where generated business card images are saved.
- **fonts**: Custom fonts used for generating business cards.
- **static**: Static files for the application.

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/ayubxontursunov/django_businesscard_api.git
    cd django_businesscard_api
    ```

2. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Run migrations**:

    ```sh
    python manage.py migrate
    ```

4. **Start the development server**:

    ```sh
    python manage.py runserver
    ```

## Usage

1. **Register User Details**:

    Send a POST request to `/register` with user details in the following format:

    ```json
    {
        "job_title": "Manager",
        "email": "hello@reallygreatsite.com",
        "fname": "Kyrie",
        "sname": "Petrakis",
        "phone": "123-456-789",
        "github": "https://github.com/kyrie"
    }
    ```

2. **Download Business Card**:

    After registration, download the generated business card by sending a GET request to `/card/{firstname}`.

    Example:
    
    ```sh
    GET /card/Kyrie
    ```

## Example Business Cards
### Business Card 1

<img src="media/KYRIE.png" alt="Business Card 1" width="300">

### Business Card 2

<img src="media/KYRIE(2).png" alt="Business Card 2" width="300">


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [tursunovayubxon07@gmail.com](mailto:tursunovayubxon07@gmail.com).
