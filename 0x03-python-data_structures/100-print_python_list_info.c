#include <Python.h>

/**
 * print_python_list_info - prints information about a Python list
 * @p: PyObject
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
	{
		PyObject *type = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(type)->tp_name);
	}
}
