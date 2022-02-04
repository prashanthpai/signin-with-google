## signin-with-google

Sample code to demonstrate signin with Google

### Usage

#### Prerequisites

1. [Create OAuth consent screen](https://console.developers.google.com/apis/credentials/consent)
   - Setup test users by adding their Google email addresses.
2. [Create OAuth 2.0 Client IDs](https://console.developers.google.com/apis/credentials)
   - Ensure to whitelist javascript origins `http://localhost` and `http://localhost:8001`.
   - Note down the `Client ID` and set it in `GOOGLE_CLIENT_ID` variable of `index.html` and `server.py` files.

#### Run

```sh
$ pipenv install
$ pipenv shell
$ python server.py
```

Open `http://localhost:8001` in your browser.

On sign-in, encoded JWT credentials are logged in web console and sent to the python backend where it is verified, decoded and logged.

```
127.0.0.1 - - [07/Feb/2022 11:17:26] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [07/Feb/2022 11:17:28] code 404, message File not found
127.0.0.1 - - [07/Feb/2022 11:17:28] "GET /favicon.ico HTTP/1.1" 404 -
{
    "iss": "https://accounts.google.com",
    "nbf": 9999999999,
    "aud": "999999999999-xxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com",
    "sub": "xxxxxxxxxxxxxxxxxxxxxx",
    "hd": "unacademy.com",
    "email": "xxxxxxxxx@unacademy.com",
    "email_verified": true,
    "azp": "999999999999-xxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com",
    "name": "Prashanth Pai",
    "picture": "https://lh3.googleusercontent.com/a/AATXAJYFjhvBVFMGMNVnbvNVGCGCG=s96-c",
    "given_name": "Prashanth",
    "family_name": "Pai",
    "iat": 1644212851,
    "exp": 1644216451,
    "jti": "6876ibhghjgbur76xe654xchfjgcf5ru76jygtg7tki"
}
127.0.0.1 - - [07/Feb/2022 11:17:34] "POST /signin-with-google HTTP/1.1" 200 -
```

### References

* [Display the Sign In With Google button](https://developers.google.com/identity/gsi/web/guides/display-button)
* [Verify the Google ID token on your server side](https://developers.google.com/identity/gsi/web/guides/verify-google-id-token)
