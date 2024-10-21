<!-- 

# Finish docker application: 'Details App'

In the link below you'll have access to github repository where the half prepared application is available. Add additional container for saving data from the application on to the database of the other container using Postgres, Mysql or SQLite3 saved on to the host filesystem.

### Pre Requisits:

- Linux based OS (Debian or Rocky)
- Docker
- Docker compose
- Python3
- Poetry
- Git
- Will to finish project
- Popcorn and bamba

### Task

- Setup all the pre-requirements
- verify that you have __forked__ the application (please to not work on this project itself)
- Read the README.md file and understand how is the application runs
- Change application to connect to db container and save data on to the OS filesystem
    - add database container to docker compose file:
        - database container needs setup script that will define tables based on the code of the application, create and run that setup script
        - add testing script that will verify if the application and database are connected correctly and if not, it should try to fix it
        - the database should use volume or mount option on to saves data on the host OS filesystem
    - application should wait until database container is started and initated

### Notes

- Verify that application works
- Save dependencies with `pyproject.toml`
- Update README or INSTALL files as required by your changes
- If several people are working on the project add CONTRIBUTORS.md file and write down full name and nick name in github/gitlab/gitea/bitbucket


[Link to repository](https://github.com/zero-pytagoras/details-app.git) -->