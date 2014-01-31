from django import template


def slicemark(value, arg):

	# Corta del documento hasta la marca indicada "arg"
	value = value.split(arg)[0]
	return value


register = template.Library()
register.filter('slicemark', slicemark)