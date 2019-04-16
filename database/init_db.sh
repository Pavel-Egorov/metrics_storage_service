#!/usr/bin/env bash

services=`printenv | sed -n -e 's/^DATABASE_NAME_\([_a-zA-Z1-9]*\)=.*/\1/p'`

for service in ${services}
do
    db_name=DATABASE_NAME_${service}
    db_user=DATABASE_USER_NAME_${service}
    db_password=DATABASE_PASSWORD_${service}
    psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -c "DO \$\$ BEGIN IF NOT EXISTS (SELECT * FROM pg_catalog.pg_user WHERE usename = '${!db_user}') THEN CREATE USER ${!db_user} WITH password '${!db_password}'; END IF; END\$\$;"
    psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -tc "SELECT 1 FROM pg_database WHERE datname = '${!db_name}'" | grep -q 1 || psql -U postgres -c "CREATE DATABASE ${!db_name}"
    psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -c "GRANT ALL privileges ON DATABASE ${!db_name} TO ${!db_user};"
done
