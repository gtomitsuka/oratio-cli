# `oratio` API Specification

Built for compatibility with [Oratio Dev](https://dev.oratio.io) at `0.1.0` and with `oratio-core` at `0.1.0`.

## `oratio login`

### Expected output

```
$ oratio login
Username for 'https://accounts.oratio.io': username
Password for 'https://username@accounts.oratio.io':
```

### How to process

After securely getting username and password, do:

    POST https://accounts.oratio.io/api/login
    
With username and password sent as URL-encoded body.

Expected response is `{"error":null,"username":"example","email":"example@example.com","session":"7887024b17d1c6919f496e7028d657de"}`.

Parse JSON and save session on a file called `~/.oratio-session`.

## `oratio add <module name>`

This will add a `module.json` to the current directory.
`<module name>` is the module name, that the user must have created on [Oratio Dev](https://dev.oratio.io) first.

## Expected output

```
$ oratio add feedback
{
  "name": "feedback",
  "metadata": {
    "description": "get feedback for anything"
  },
  "version": "0.0.1",
  "id": "b44a9d53-7159-40a3-aa3b-094cfd3c6217",
  "screenshots": []
}
Is this correct? [y/n] y
```

## How to process

First, get the name and do

    GET https://dev.oratio.io/module/(module name)/info

Expected response is:

```
{
  "error": null,
  "name": "module name",
  "metadata": {
    "description": "module description"
  },
  "latest: "0.0.1",
  "id: "b44a9d53-7159-40a3-aa3b-094cfd3c6217",
  "screenshots": []
}
```

Then, get `~/.oratio-session` and do

    GET https://dev.oratio.io/module/(module name)/verify-owner?session=(~/.oratio-session)

If the user is indeed the owner, the response is:

```
{
  "is-owner": true,
  "error": null
}
```

If the user isn't the owner, expected response is:

```
{
  "is-owner": false,
  "error": null
}
```

If the user isn't the owner, display an error message. If he is it indeed, then save `./module.json`.

## `oratio upload`

Read `./module.json` and get `version`. Compress current directory into a .tar.gz and upload it
with `POST https://dev.oratio.io/api/module/add-release?version=(version)` - tar.gz shall be sent as multipart/form-data
