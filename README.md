
# SOCMINT (Social Media Intelligence) Django App

SOCMINT (Social Media Intelligence) is a Django web application designed to gather and analyze social media data from platforms like Reddit, Twitter, Instagram, and Telegram. It utilizes machine learning models to classify and analyze social media content for various purposes, such as identifying potential threats, monitoring trends, and extracting insights.

## Features

- **Reddit Search:** Allows users to search for posts on Reddit based on keywords/phrases, subreddit, and other filters. Posts are then classified using a machine learning model to identify relevant information.
- **Twitter Analysis:** In Development.
- **Instagram Monitoring:** In Development.
- **Telegram Chat Analysis:** In Developments.

## Installation

1. Clone the repository:

```
git clone https://github.com/SmartyDroidBot/socmint.git
cd socmint
```

2. Initialize and update submodules:

```
git submodule init
git submodule update
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Set up environment variables:

Create a `.env` file in the root directory and define the following variables:

```
# Django settings
SECRET_KEY=your_secret_key_here
DEBUG=True
...

# Reddit API credentials
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
```

5. Run database migrations:

```
python manage.py migrate
```

6. Start the development server:

```
python manage.py runserver
```

The application should now be accessible at http://localhost:8000/home/.

## Usage

1. Navigate to the desired feature (e.g., Reddit Search, Twitter Analysis) from the navigation menu.
2. Enter the required parameters such as keywords, subreddit, limit, etc.
3. Submit the form to retrieve and analyze relevant social media content.
4. View the results on the web interface, including classified posts, analytics, and visualizations.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/my-feature`).
6. Create a new Pull Request.

## Credits

- Model credits: [HiddenKise/Kaviel-threat-text-classifier](https://huggingface.co/HiddenKise/Kaviel-threat-text-classifier)
- Reddit API: praw

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
```
