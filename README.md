

# Social Media Intelligence (Socmint) App

## Introduction
The Social Media Intelligence (Socmint) App is a Django web application designed to search and analyze social media posts from platforms like Reddit. It provides insights into potentially threatening or harmful content by leveraging machine learning models.

## Features
- **Reddit Search**: Search and analyze posts from Reddit.
- **Threat Detection**: Identify potential threats such as banking fraud, terrorist attacks, life threats, online scams, and information leakage.
- **Comment Analysis**: Analyze post comments for additional insights and threats.
- **Visual Insights**: Visualize search results with interactive pie charts.

## Model Credits
The threat detection model used in this application is provided by [HiddenKise](https://huggingface.co/HiddenKise/Kaviel-threat-text-classifier) and is available on the Hugging Face Model Hub as the "Kaviel-threat-text-classifier" model.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your_username/socmint.git
   ```
2. Navigate to the project directory:
   ```
   cd socmint
   ```
3. **Use a Virtual Environment (Optional)**: We recommend using a virtual environment to manage project dependencies. If you're not familiar with virtual environments, you can learn how to set one up by following this [guide](https://docs.python.org/3/tutorial/venv.html). 
4. Initialize and update Git submodules:
   ```
   git submodule init
   git submodule update
   ```
5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Set up environment variables:
   - Create a `.env` file in the project root directory.
   - Add the following environment variables:
     ```
     REDDIT_CLIENT_ID=your_reddit_client_id
     REDDIT_CLIENT_SECRET=your_reddit_client_secret
     REDDIT_USER_AGENT=your_reddit_user_agent
     # Add other necessary environment variables
     ```
7. Run migrations:
   ```
   python manage.py migrate
   ```
8. Start the development server:
   ```
   python manage.py runserver
   ```
9. Access the application at `http://127.0.0.1:8000/` in your web browser.

## Usage
1. Navigate to the Reddit platform using the navigation bar.
2. Enter keywords and optional filters (subreddit, limit, comment limit) in the search form.
3. Click "Submit" to view the search results.
4. Explore the search results and visual insights provided by the application.

## Future Plans
Here are some features planned for future development:
- **Google Account Integration**: Allow users to log in or sign up using their Google accounts.
- **Instagram Integration**: Add support for searching and analyzing posts from Instagram.
- **Twitter Integration**: Add support for searching and analyzing tweets from Twitter.
- **Telegram Integration**: Add support for searching and analyzing messages from Telegram.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/new-feature`)
6. Create a new Pull Request

## License
This project is licensed under the [MIT License](LICENSE).
