# Airflow Pipeline

## Project Overview

This repository showcases Apache Airflow projects developed during an in-depth learning course. It includes diverse DAGs, tasks, and workflow integrations, demonstrating practical applications and advanced features of Airflow.

## Setup and Configuration

To run the Airflow environment using Docker Compose and integrate with services like APIs and PostgreSQL, follow these steps:

### Starting the Environment

1. Ensure Docker is installed and running on your machine.
2. Clone this repository to your local system.
3. Navigate to the directory containing the `docker-compose.yml` file.
4. Start the services using:

    ```bash
    docker-compose up -d
    ```

    The `-d` flag indicates that the containers should be started in the background.

### Configuring Airflow

1. Once the services are up, access the Airflow web interface by navigating to `http://localhost:8080`.
2. Log in with the default credentials provided in the Docker setup.
3. To configure connections to your API and PostgreSQL:

- Go to **Admin** > **Connections** in the Airflow UI.
- Click on **+** to add a new connection.
- For PostgreSQL:
  - **Conn Id**: `postgres`
  - **Conn Type**: `Postgres`
  - **Host**: usually `postgres` if using Docker's networking
  - **Login**: `<your-username>`
  - **Password**: `<your-password>`
  - **Port**: `5432`
- For API:
  - **Conn Id**: `user_api`
  - **Conn Type**: `HTTP`
  - **Host**: `https://randomuser.me/`

## Contributions

Contributions to this project are welcome. Please fork the repository and submit pull requests with your enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
