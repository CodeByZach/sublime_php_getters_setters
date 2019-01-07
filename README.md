PHP Getters and Setters
=======================


With PHP Getters and Setters you can automatically generate _Getters_ and _Setters_ for your PHP classes.

Features:
---------

* Generate Getters, Setters or Both.
* Can be applied to all class properties or just to a single one.
* Description, Type and Type Hinting automatically discovered from the variable docblock.
* Fully customizable templates.

Usage Instruction:
------------------

1. Generate PHP code

    ```php
    class test
    {
        /**
         * foo container
         *
         * @var AbcClass
         */
        private $foo;
    }
    ```

2. Go to Tools -> PHP Getters and Setters
3. Getter and Setter will be generated:

    ```php
    class test
    {
        /**
         * foo container
         *
         * @var AbcClass
         */
        private $foo;

        /**
         * Gets the foo container.
         *
         * @return AbcClass
         */
        public function getFoo()
        {
            return $this->foo;
        }

        /**
         * Sets the foo container.
         *
         * @param AbcClass $foo the foo
         */
        private function _setFoo(AbcClass $foo)
        {
            $this->foo = $foo;

            return $this;
        }
    }
    ```

As you can see, it saves you the trouble of having to comment your variables.

This is an huge time saver!

Usage
-----

Commands available are:

 * Generate Getters and Setters
 * Generate Getter
 * Generate Setter
 * Generate Getter for...
 * Generate Setter for...

These can be accesed via the context menu (right click on the source of any open PHP file) or the command pallette. The currently open file *must* be a PHP file.

Settings Reference
------------------

###ignore_visibility
_type_    : **boolean**

_default_ : **false**

_description_: Ignore visibilty for setters generation.

### setter_before_getter
_type_: **boolean**

_default_: **false**

_description_: Set to true to generate Setters before Getters.

### type_hint_ignore
_type_: **list of strings**

_ignorable types_ : **["unknown", "self", "array", "callable", "bool", "float", "int", "string", "iterable", "object"]**

_default_: **[]**

_description_: Should a variable type match any of the following, it will NOT be used for type hinting. (The **"unknown"** option is a wild-card)

###registerTemplates
_type_   : **array**

_default_: **[]**

_description_: Additional user templates to load.

###template
_type_   : **string**

_built-in options_ : **PSR2, camelCase, camelCaseFluent, snakeCase, snakeCaseFluent**

_default_: **PSR2**

_description_: The selected template.

Creating your own template
--------------------------


[package-dir] is your [package directory](http://docs.sublimetext.info/en/sublime-text-3/basic_concepts.html#the-packages-directory).

* Make a directory called ```[package-dir]/PHP Getters and Setters```.
* Put the following in a file at ```[package-dir]/PHP Getters and Setters/user_templates.py```.
  ```
class myTemplate(object):
    name = "myTemplate"
    style = 'camelCase' # can also be snakeCase
    getter = """
    /**
    * Gets the %(description)s.
    *
    * @return %(type)s
    */
    public function %(getterPrefix)s%(normalizedName)s()
    {
        return $this->%(name)s;
    }
"""

    setter = """
    /**
    * Sets the %(description)s.
    *
    * @param %(type)s $%(param)s
    *
    * @return self
    */
    %(visibility)s function %(visibilityPrefix)s%(setterPrefix)s%(normalizedName)s(%(typeHint)s $%(param)s)
    {
        $this->%(name)s = $%(param)s;
    }
"""
  ```
* Edit the parts between setter and getter how you want.
* Edit your user settings for this package. On OSX that's ```Preferences | Package Settings | PHP Getters and Setters | Settings - User```.
* Add the following settings
  ```
    // user defined templates to load
    "registerTemplates" : [ "myTemplate" ],

    // the template used to generate code
    "template" : "myTemplate"
  ```
 * restart sublime to use the new template
