from flask import Flask
from flask_graphql import GraphQLView
from schema import schema  # <-- change from .schema to schema

app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enable GraphiQL UI
    )
)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()