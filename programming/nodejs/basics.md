# Basics

### Work environment
Make sure that both npm and node is installed:
```
nodejs -v && npm -v
```

There is also a REPL: `node`

Create new NPM project
```
npm init
```

Use existing package.json
```
npm install
```


### Env
create a `.env` file. Load its content by `require('dotenv').config();`


### Nodemon
Works like Debug mode for Flask apps und auto reloads, etc.
```sh
npm install nodemon --save-dev
```
I may be smart to add a simple start command to `package.json`:
```json
...
  "scripts": {
    "start": "node index.js",
    "devstart": "nodemon index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  }
  ...
```
Can then be used like this:
```sh
npm start
npm run-script devstart
```

### Express + Expres Generator
Express is basically a (customizable) webframework - like Flask.
```
npm install express --save
```

The express generator is a nice commandline interface, that handles lots of boilerplate code and sets up a basic application layout.
```sh
npm install express-generator -g
```

##### Generator
Create a new application that uses handlebars as its templateing engine:
```sh
express --view=hbs NAME_APP && cd NAME_APP && npm install
```
After that it may be a good idea to enable .env support:
```sh
npm install dotenv --save
```
and then load the config right at the beginning of the entry point for the application:
```js
...
/**
 * Firstly load .env file.
 */
if (process.env.NODE_ENV !== 'production') {
  require('dotenv').config();
}
...
```



### Handlebars
Use exress-handlebars instead of normal handlebars:
```sh
npm install express-handlebars --save
```
Then setup handlebars to use the correct layouts and partials:
--> https://stackoverflow.com/questions/16385173/node-js-express-handlebars-js-partial-views

--> https://github.com/ericf/express-handlebars/issues/134


### Form Validation
https://stackoverflow.com/questions/55772477/how-to-implement-validation-in-a-separate-file-using-express-validator

### Session + Locals
Middleware: express-session
Response.locals -> is available in **every** template.
```js
app.use((req, res, next) => {
  res.locals.authenticated = req.session && req.session.authenticated;
  next();
})
```