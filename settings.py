TORTOISE_ORM = {
    "connections": {"default": "mysql://aerich:aerich@127.0.0.1:3306/aerichTest"},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}