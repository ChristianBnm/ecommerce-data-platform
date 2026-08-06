ecommerce-data-platform/

├── .github/
│   └── workflows/

├── backend/

├── frontend/

├── etl/

├── database/
│   ├── saas/
│   ├── raw/
│   └── warehouse/

├── docker/

├── docs/
│   ├── architecture.md
│   └── database-design.md

├── .gitignore

├── docker-compose.yml

└── README.md


La conexión a PostgreSQL utiliza el nombre del servicio Docker como hostname, permitiendo que los contenedores se comuniquen mediante la red interna definida en Docker Compose.