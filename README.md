# Todoist-sh
this is an attempt to make a cli that will ultimately be used to wrap a neovim plugin or any other editor plugin that can use a cli command as the base of the plugin logic

python was decided as the language so that we can leverage the official python sdk and minimize our effort in making this wrapper

while the `uv` ecosystem is helping to increase the ability to make python executibles easy to distribute and use with a wide variety of system especially in non-performance intensive scenarios such as this one

this is definately still under development but pull requests are welcome for those that want to work with me on this.

im mostly trying to leverage my existing work on [my treesitter project](https://github.com/ca-mantis-shrimp/tree-sitter-projects) as well as the neovim plugin im creating to make a nice interface:
[plugin link](https://github.com/ca-mantis-shrimp/todoist-nvim)

if you have no interest in the neovim plugin, thats fine! this was built so that if someone is wanting to build out vscode plugin or whatever other kind of plugin, that is fine

you will however want to read the spec for the treesitter plugin so that you are aware of how i plan to capture this data as a file rather than work on an individual list or a database schema since i feel like todoist already did that part and i have not intention of reinventing the wheel
