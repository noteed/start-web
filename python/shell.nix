{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    buildInputs = [
      pkgs.python38
      pkgs.python38Packages.flask
      pkgs.python38Packages.pycountry # Only used to generate countries.sql.
      pkgs.sqlite
    ];
}

