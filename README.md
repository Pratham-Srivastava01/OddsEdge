# OddsEdge

OddsEdge is a backend-focused sports betting analytics project that ingests external odds data, tracks historical market movement, evaluates picks, and serves structured insights through a REST API.

The goal of this project is to move beyond a static data pipeline and build a more production-style backend system with real API integration, persistent storage, internal service layers, and documented endpoints.

## Why I Built This

I wanted to build a project that was more advanced than a local analytics pipeline and centered around another hobby of mine: Sports. Instead of only analyzing stored data, OddsEdge is designed to pull live odds data from external providers, normalize and store it, and expose useful betting analytics through its own backend API.

This project is meant to demonstrate:
- External API integration
- Backend service design
- Data modeling and persistence
- REST API development with FastAPI
- Odds tracking and historical line movement analysis
- A cleaner, more realistic software engineering project structure

## Features

Current and planned features include:
- Ingest sports odds from an external API
- Store game, odds, and pick data in a relational database
- Track historical line movement over time
- Score picks against closing lines or game outcomes
- Expose REST endpoints for games, odds, picks, and refresh operations
- Return structured JSON responses for downstream clients
- Auto-generate interactive API docs with FastAPI

## Tech Stack

- **Backend:** FastAPI
- **Language:** Python
- **Database:** SQLite for local development
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Testing:** Pytest
- **API Docs:** Swagger UI / OpenAPI via FastAPI

## Setup

### 1. Clone the repository

```bash
git clone git@github.com:Pratham-Srivastava01/OddsEdge.git
cd OddsEdge
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create environment file

Create a `.env` file in the project root and add your configuration values.

Example:

```env
ODDS_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///./data/oddsedge.db
```

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

Once the server is running, open:
- `http://127.0.0.1:8000/docs` for Swagger UI
- `http://127.0.0.1:8000/redoc` for ReDoc

FastAPI automatically generates interactive API documentation for your endpoints [web:384].

## API Design

Initial API surface will likely include endpoints such as:

### Health
- `GET /health`
- `GET /`

### Games
- `GET /games`
- `GET /games/{game_id}`
- `GET /games/upcoming`

### Odds
- `GET /odds/{sport}`
- `GET /games/{game_id}/odds-history`

### Picks
- `POST /picks`
- `GET /picks`
- `GET /picks/{pick_id}`

### Refresh / Ingestion
- `POST /refresh/odds`
- `POST /refresh/games`

These may change as the project evolves, but the main idea is to separate ingestion endpoints from read/query endpoints.

## Data Model

The first version of the system will likely revolve around three main entities:

- **Game**: teams, sport, league, start time, status
- **OddsSnapshot**: sportsbook, market, line, price, timestamp
- **Pick**: user-selected side, line taken, stake, confidence, result

This makes it possible to compare opening vs. closing lines, monitor line movement, and evaluate whether picks beat the market.

## Development Roadmap

### Phase 1
- Set up FastAPI app
- Add config and database session management
- Add health route
- Define initial SQLAlchemy models
- Create first routers and schemas

### Phase 2
- Integrate a live sports odds API
- Ingest and normalize game + odds data
- Store snapshots in SQLite
- Add refresh endpoints

### Phase 3
- Add pick creation and scoring logic
- Track line movement and closing line value
- Improve validation and error handling
- Add tests for core endpoints

### Phase 4
- Add better analytics endpoints
- Add caching and background refresh jobs
- Consider PostgreSQL + Docker for a more production-style setup

## Notes

- Local development uses SQLite for simplicity.
- API providers may enforce rate limits, so refresh logic should eventually include retry/backoff behavior and request pacing [web:390][web:393].
- The project is currently focused on backend architecture and API design rather than frontend UI.

## Status

This project is currently in early development. The initial repository structure is complete, and core API routes, models, and services are being built next.

## License

This project is for educational and portfolio purposes right now.
