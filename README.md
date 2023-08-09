# graphene vs strawberry

## commands

### Run dev server

```
python manage.py runserver
```

- Graphene GraphiQL: http://127.0.0.1:8000/ingredients/graphene
- Strawberry GraphiQL: http://127.0.0.1:8000/ingredients/strawberry

### Export schema

#### Graphene

```
python manage.py graphql_schema --out schema.graphql
```

#### Strawberry

```
python manage.py export_strawberry_schema > schema.graphql
```
