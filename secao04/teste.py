import psycopg2
from sqlalchemy import create_engine


conexao_pg = create_engine('postgresql+asyncpg://postgres:decastro@localhost:5432/faculdade').connect()
