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

**ignore_visibility**
<br/>type: `boolean`
<br/>default: `false`
<br/>description: Ignore visibilty for setters generation.

**setter_before_getter**
<br/>type: `boolean`
<br/>default: `false`
<br/>description: Set to true to generate Setters before Getters.

**type_hint_ignore** (requires restart)
<br/>type: list of strings
<br/>ignorable types: `["unknown", "self", "array", "callable", "bool", "float", "int", "string", "iterable", "object"]`
<br/>default: `[]`
<br/>description: Should a variable type match any of the following, it will NOT be used for type hinting. (The **"unknown"** option is a wild-card)

**register_templates** (requires restart)
<br/>type: `array`
<br/>default: `[]`
<br/>description: Additional user-defined templates to load.

**template** (requires restart)
<br/>type: `string`
<br/>built-in options: `"PSR2"`, `"camelCase"`, `"camelCaseFluent"`, `"snakeCase"`, `"snakeCaseFluent"`
<br/>default: `"PSR2"`
<br/>description: The selected template.

Creating your own template
--------------------------


[package-dir] is your [package directory](http://docs.sublimetext.info/en/sublime-text-3/basic_concepts.html#the-packages-directory).

1. Make a directory called `[package-dir]/PHP Getters and Setters`.
2. Put the following in a file at `[package-dir]/PHP Getters and Setters/user_templates.py`.
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
3. Edit the parts between getter and setter how you want.
4. Edit your user settings for this package. On macOS that's _Preferences > Package Settings > PHP Getters and Setters > Settings - User_.
5. Add the following settings:
```
    // Additional user-defined templates to load.
    "register_templates" : [ "myTemplate" ],

    // The selected template.
    "template" : "myTemplate"
```
