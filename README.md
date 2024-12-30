# Todoist-sh
this is an attempt to make a cli that will ultimately be used to wrap a neovim plugin or any other editor plugin that can use a cli command as the base of the plugin logic

python was decided as the language so that we can leverage the official python sdk and minimize our effort in making this wrapper

while the `uv` ecosystem is helping to increase the ability to make python executibles easy to distribute and use with a wide variety of system especially in non-performance intensive scenarios such as this one

this is definately still under development but pull requests are welcome for those that want to work with me on this.

im mostly trying to leverage my existing work on [my treesitter project](https://github.com/ca-mantis-shrimp/tree-sitter-projects) as well as the neovim plugin im creating to make a nice interface:
[plugin link](https://github.com/ca-mantis-shrimp/todoist-nvim)

if you have no interest in the neovim plugin, thats fine! this was built so that if someone is wanting to build out vscode plugin or whatever other kind of plugin, that is fine

you will however want to read the spec for the treesitter plugin so that you are aware of how i plan to capture this data as a file rather than work on an individual list or a database schema since i feel like todoist already did that part and i have not intention of reinventing the wheel

## Configuration
right now configuration just consitutes getting the api key into the program in the least invasive way possible while still respecting UNIX standards

environment variables are the primary way to set it, but i have also created the `set-key` subcommand which can be used to set the API key directly where it will be stored in local storage for later user

configuration is handled with the standard `platformdirs` package and can be used place the default configuration within the standard place, no matter what program you are using

### A quick note on security
in order to ensure best-practices, I actually store your api key into an encrypted file locally to ensure the api key is safe even in the case of a compromise.

this has a few design considerations however. 

the primary one being that the encrypted file itself also needs a password. when you first run either the normal command or the set key, you will first need to create a password for the key vault.
This password should be put in a secure place, and later put into the "KEYRING_CRYPTFILE_PASSWORD" environment variable to ensure this does not ask you for the password every time you run the CLI.

If this becomes too much of a burden, you can turn encryption off to eliminate this whole process, and just use the standard "TODOIST_API_KEY" environment variable
