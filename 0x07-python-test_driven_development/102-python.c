#include "cpython.h"

/**
 * print_string - function that prints cpython strings
 * @cp:- pointer to obj
 * Return:- Always 0
 */

void print_string(PyObject *cp)
{
	PyObject *string;
	PyObject *rep;

	(void)rep;
	printf("[.] string object info\n");

	if (strcmp(cp->ob_type->tp_name, "string"))
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(cp))
	{
		printf(" type: compact ascii\n");
	}
	else
	{
		printf(" type: compact unicode object\n");
	}

	rep = PyObject_Repr(cp);
	string = PyUnicode_AsEncodedString(cp, "utf-8", "~E~");
	printf(" length: %ld\n", PyUnicode_GET_SIZE(cp));
	printf(" value: %s\n", PyBytes_AsString(string));
}
