# Example Flask App, using TailwindCSS and Blueprints

## Setup

1. First, install the node modules in the `jstoolchain` folder:

    ```bash
    cd jstoolchain
    (npm|pnpm|yarn) install
    ```

2. Run the Tailwind toolchain:

    ```bash
    cd jstoolchain
    (npm run|yarn|pnpm) tailwind-(watch|build)
    ```

3. Check out the `Makefile` to either run the flask app via `make` or manually:

    ```bash
    make

    # or

    export FLASK_DEBUG=1 && flask run
    ```

This should output a file called `output.css` in your static folder. This is the file referenced in your `index.html` file.
