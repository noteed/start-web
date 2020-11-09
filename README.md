# Start a web application

This repository contains a minimal web application written in two different languages:

- C#, using ASP.NET Core and Razor pages
- Python, using Flask and Jinja2


For each application, a development environment is given by a `shell.nix` file,
automatically activated through a `.envrc` file (and thus `direnv`). In the
case of the C# application, dependencies are automatically downloaded by
`dotnet`, not Nix.


# C#

```
$ nix-shell
direnv: ...
$ dotnet run
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: http://localhost:5000
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
      Content root path: /home/thu/projects/start-web/csharp
```

Then navigate to [`127.0.0.1:5000`](http://127.0.0.1:5000).


# Python

```
$ cd python/
direnv: ...
$ python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://0.0.0.0:9002/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 111-111-111
```

Then navigate to [`127.0.0.1:9002`](http://127.0.0.1:9002).

The `.envrc` file also specifies the `FLASK_ENV` environment variable to enable
auto-reloading upon changes to the source code.
