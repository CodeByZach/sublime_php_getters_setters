print('==== USER TEMPLATES ===')

class myCamelCase(object):
	name = "myCamelCase"
	style = 'camelCase'
	getter = """
	/**
	 * Gets the %(humanName)s.
	 * @return %(type)s $%(name)s
	 */
	public function %(getterPrefix)s%(normalizedName)s() {
		return $this->%(name)s;
	}
"""

	setter = """
	/**
	 * Sets $%(name)s.
	 * @param %(type)s $%(param)s
	 */
	%(visibility)s function %(visibilityPrefix)s%(setterPrefix)s%(normalizedName)s(%(typeHint)s $%(param)s) {
		$this->%(name)s = $%(param)s;
	}
"""
