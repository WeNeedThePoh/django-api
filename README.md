# Django Small API

- [Available endpoints](#available-endpoints)
- [Setup](#setup)
- [Usage](#usage)
- [Other commands](#other-commands)

Small API that lets you perform CRUD operations. Its main focus is the management of occurrences.

### Available endpoints

| Endpoint         | Method | Description         |
| ---------        | ------ | -----------         |
| /occurences      | POST   | Create a occurrence |
| /occurences      | GET    | Get all occurrences |
| /occurences/{id} | GET    | Get a occurrence    |
| /occurences/{id} | PUT    | Update occurrence   |
| /occurences/{id} | DELETE | Delete occurrence   |

For more **detailed documentation** you can run the following command to generation the documentation.

```bash
make api_docs
```
After it's done, you can access the documention at `./docs/web/index.html`

### Setup
Before starting, you will need to have [docker](https://store.docker.com/search?type=edition&offering=community) installed in your computer. If you have [postman](https://www.getpostman.com/apps) installed it will help you to test and make request to the API.

You can start the API by simply run the following command.

```bash
make setup_api
```

Because it's the first time, this command will build all the necessary images and then will spin up the containers. After that it will run migrations and make your database up to date.

If it's not the first time you can simply run:

```bash
make start_api
```

This command will only spin up the containers, so if you want to run migrations you will need to run:

```bash
make migrate_db
```

### Usage

When the setup is done you can now safely browse [localhost:8000](127.0.0.1:8000) and explore the API.

There is one other option ***(better one)*** to explore the API. You can test it using this [Postman collection](https://www.getpostman.com/collections/4009e8b293720945c663), you just need to **import** it **to** your **Postman** and it's ready to use.



The endpoints are in order, so you can make the first request to create one *Occurrence*, then you can make request to get all *Occurrences* and so on.

### Tests

To run tests you just need to do:

```bash
make tests
```

### Other commands

You can see the list of commands by running:

```bash
make help
```

If there is some cache problem you can clean it by running:

```bash
make clean_cache
```

If you want to get inside the container you can run:

```bash
make hijack
```
