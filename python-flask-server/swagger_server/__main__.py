#!/usr/bin/env python3

import connexion

from swagger_server import encoder

from swagger_server.managers import firehose_manager

# TODO: This can be set as a system FLAG in the future to disable debug messages in production.
DEBUG = True


def main():

    firehose_manager.init()

    if DEBUG:
        print("\n[DEBUG - Starting Flask Server]\n")
        print(
            "\n[DEBUG - Production WSGI Server vs Development Server]\n\
            This is a demo, don't worry about the big red message below (for now...)\n\
            TODO: https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/\n"
        )

    # TODO: https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/

    app = connexion.App(__name__, specification_dir="./swagger/")
    app.app.json_provider_class = encoder.JSONEncoder
    app.add_api(
        "swagger.yaml", arguments={"title": "Tracking API"}, pythonic_params=True
    )
    app.run(port=8080)


if __name__ == "__main__":
    main()
