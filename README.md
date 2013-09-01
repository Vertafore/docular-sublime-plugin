#Sublime Text Plugin for Docular

So putting inline documentation within your script files can get a little unruly. Your script files should be fairly small to begin with, but sometimes the documentation that is displayed to those interested in learning your software can burden those looking at the code on a day to day basis.

### Use these documentation conventions to optimize your efficiency

* Use comment blocks for documentation that should show in the generated docs. These comments are best to describe API usage.

```js
/**
 * @doc module
 * @name docular
 * @description This module contains all the logic for the workflow of generating
 * partials and front end resources for display of docular documentation.
 *
 * This is a comment BLOCK that will be in the documentation
 * This same information should probably be hidden during development
*/
```
* Use single line comments to communicate to other developers the specifics of your code.

```js
// This is a comment for developers
// This gives additional info not already provided by good coding practices ;-)
```

When these conventions are followed, you can then hide all comment blocks a the downloadednd keep all single line comments visible during development!

##Sublime Time

We have written a simple Sublime Text plugin to help with this process. The plugin uses the native "fold" functionality in the Sublime Text API to toggle the visibility of comment blocks.

Once you add the plugin and add the key bindings, you can quickly toggle the visibility of comment blocks so you can focus on improving code or toggle again to focus on improving documentation. Keen!

##Sublime Plugin Installation

* Download the plugin from Github

* Open Sublime Text, and choose:

```bash
    preferences > Browse Packages
```
* Navigate to the "Packages/User/" directory
* Drag the downloaded plugin file "docular.py" into the "Packages/User/" directory

###Done! Keyboard Shortcut Time

Now that you have added the "docular.py" plugin to Sublime, it's time to add keybindings to your user profile so you can quickly access the plugin's functionality.

* With Sublime open, choose <code>Preferences > Key Bindings - User</code>
* Add this line in JSON format to the array in this file

```js
[
    { "keys": ["command+shift+d"], "command": "docular_toggle" }
]
```

* Close Sublime, re-open Sublime.
* Now open a file that has comment blocks within it. Hit "command+shift+d" (on Mac) to toggle the comment blocks.