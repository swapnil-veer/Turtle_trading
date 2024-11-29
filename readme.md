# **Turtle Trading Strategy**

## **Overview**
Turtle Trading is a famous trend-following strategy developed by Richard Dennis and William Eckhardt. This project automates the Turtle Trading strategy using Python and Django, offering the ability to process stock data, identify trading signals, and manage portfolio positions efficiently.

### **Key Features**
- Automated data processing for stocks using the Turtle Trading strategy.
- Integration with MySQL for efficient data storage and retrieval.
- Dockerized setup for easy deployment and portability.
- Support for Nifty 50 and custom stock lists.
- Extendable architecture for real-time trading and API integrations.

**To know more about Turtle Trading, please refer *project.md* file**

---

## **Setup Instructions**

### **Prerequisites**
Ensure the following software is installed:
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

### **Installation**

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd Turtle_trading
   ```

2. **Setup .env File**
   
Create a .env file in the root directory with the following contents:
   ```env
   MYSQL_ROOT_PASSWORD=your_root_password
   MYSQL_DATABASE=turtle_trading
   MYSQL_USER=your_db_user
   MYSQL_PASSWORD=your_db_password
```
* Replace your_root_password with your MySQL root password.
* Replace your_db_user and your_db_password with your desired database username and password.


3. **Build and Start Docker Containers**
   
Build and run the backend and MySQL services:

   ```bash
      docker-compose up --build
   ```

4. **Run Database Migrations**
   
Apply migrations to set up the database:

   ```bash
   docker-compose exec django_backend python manage.py migrate
   ```

5. **Load Initial Data (Optional)**
   
If you want to add the Nifty 50 tickers to the database:

```bash
docker-compose exec django_backend python manage.py stock_lists
```
6. **Create a Superuser**
   
To create a Django superuser:

```bash
docker-compose exec django_backend python createsuperuser 
```
7. **Access the Application**

Django Admin: Visit http://localhost:8000/admin to manage data.
MySQL: Connect via any MySQL client using the credentials in your .env.

## Contributing

We welcome contributions to enhance the project. Follow these steps to get started:

1. **Development Environment Setup**
Clone the Repository
```bash
git clone <repository_url>
cd Turtle_trading
```

2. **Create a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Application Locally**
Run the Django development server:

```bash
python manage.py runserver
```
Ensure Docker is running for MySQL or set up a local MySQL instance.

5. **Run Tests**
```bash
python manage.py test
```

### Contribution Workflow
1. Fork the Repository: Click on the "Fork" button on the GitHub repository page.
2. Create a Feature Branch:
```bash
git checkout -b feature/your-feature-name
```
3. Make Changes: Implement your feature or fix.
4. Run Tests: Ensure all tests pass before committing.
5. Commit and Push:
```bash
git add .
git commit -m "Description of your changes"
git push origin feature/your-feature-name
```
6. Submit a Pull Request: Open a pull request on the original repository.

### Code of Conduct
By contributing, you agree to follow our Code of Conduct.
This project is licensed under the MIT License. See the LICENSE file for details.

## Project Structure
```bash
Turtle_trading/
├── data_processing/
│   ├── models.py         # Models for data processing
│   ├── stock_lists.py    # Utility for managing stock lists
│   ├── management/
│       └── commands/     # Custom Django management commands
├── trading/
│   ├── models.py         # Models for trading logic
│   ├── utils.py          # Utility functions for trading
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Dockerfile for backend
├── requirements.txt      # Python dependencies
└── manage.py             # Django management script
```

## Future Enhancements
   * Real-Time Trading: Integrate with Zerodha APIs for live trading.
   * Email Notifications: Notify users about trading signals via email.
   * Advanced Analytics: Add visualization and performance reports.
   * Real-Time Data: Support for live market data via APIs.

## License
This project is licensed under the MIT License. See the LICENSE file for details.