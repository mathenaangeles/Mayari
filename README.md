# Mayari

## Docker
Prerequisites: Have docker installed in system
Recommended: Have Docker VSCode extension

1. To run the docker container, open to the terminal and type `docker-compose up` in the the root of the folder. You can stop the container from the terminal or by using the VSCode extension.
2. To build or rebuild images, run `docker-compose build`. Rebuild in the following scenarios:
  - adding of new libraries
  - changing any of the Docker files
  - changing the `docker-compose.yml` file
3. To verify if the tables were created, run `docker-compose exec db psql --username=admin --dbname=mayaridb` then `\dt` in the terminal.

## Get Started  

### Backend
Prerequisites: Get `.env` file from other developers.
1. Navigate to the backend directory.
2. Run `source venv/bin/activate` to activate the virtual environment.
3. Run `pip3 install -r requirements.txt`.
4. Run `python3 server.py`.

#### Database Migrations
1. Every time the database models change, run `python3 -m flask db migrate`.
2. Run `python3 -m flask db upgrade`. 

### Frontend
1. Navigate to the client folder inside the frontend directory.
2. Run `npm install`.
3. Run `npm run serve` to compile and enable hot-reloads for development.
4. To compile and minify to production, run `npm run build`.
5. To lint and fix files, run `npm run lint`.


#### Customize Configuration
Please read the [Configuration Reference](https://cli.vuejs.org/config/).
