# User templates

class myCamelCase(object):
	name = "myCamelCase"
	style = 'camelCase'
	getter = """
	// $%(name)s
	public function %(getterPrefix)s%(normalizedName)s() {
		return $this->%(name)s;
	}
"""

	setter = """
	%(visibility)s function %(visibilityPrefix)s%(setterPrefix)s%(normalizedName)s(%(typeHint)s $%(param)s) {
		$this->%(name)s = $%(param)s;
	}
"""
