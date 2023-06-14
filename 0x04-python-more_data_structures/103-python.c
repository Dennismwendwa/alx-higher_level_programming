#include <stdio.h>
#include <python.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t size = PyList_Size(p);

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid Python List\n");
		return;
	}

	

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: ", i);

		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}


void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = PyBytes_Size(p);
	unsigned char *bytes = (unsigned char *)PyBytes_AsString(p);

	if (!PyBytes_Check(p))
	{
		 printf("[ERROR] Invalid Python Bytes Object\n");
		 return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyUnicode_AsUTF8AndSize(p, NULL));
	printf("  first 10 bytes: ");
	
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", bytes[i]);
		 printf("\n");
	}

}
