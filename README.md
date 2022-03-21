# Mayari

## Get Started

### Running on Docker
Prerequisites: Have docker installed in system
Recommended: Have Docker VSCode extension

1. In the root of the folder, ```docker-compose up``` on terminal
- Stop the containers from either the terminal or extension.
2. Build/Rebuild images 
- ```docker-compose build```

3. If you'd like to verify the tables were created:
- ```docker-compose exec db psql --username=admin --dbname=mayaridb```
- Then run ```\dt``` in the terminal

4. Rebuild in the following scenarios:
- adding of new libraries
- changes to any of the Dockerfiles
- changes to docker-compose.yml

### Backend
Prerequisites: Get .env file from other devs
1. Navigate to the backend directory.
2. Run `source venv/bin/activate` to activate the virtual environment.
3. Run `pip3 install -r requirements.txt`.
4. Run `python3 server.py`.

### Frontend
1. Navigate to the client folder inside the frontend directory.
2. Run `npm install`.
3. Run `npm run serve` to compile and enable hot-reloads for development.
4. To compile and minify to production, run `npm run build`.
5. To lint and fix files, run `npm run lint`.


#### Customize Configuration
Please read the [Configuration Reference](https://cli.vuejs.org/config/).
