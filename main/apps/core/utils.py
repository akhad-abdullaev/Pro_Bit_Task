# utils/tenants.py

import psycopg2
from django.conf import settings
from django.core.management import call_command

def create_tenant_database(db_name):
    conn = psycopg2.connect(
        dbname="postgres",
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default'].get('PORT', '5432'),
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f'CREATE DATABASE "{db_name}"')
    cur.close()
    conn.close()

    settings.DATABASES[db_name] = {
        **settings.DATABASES['default'],
        'NAME': db_name,
    }

    call_command('migrate', database=db_name)
