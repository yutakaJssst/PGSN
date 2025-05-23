from pgsn.stdlib import *
from pgsn import stdlib

ClassTerm = Record
ObjectTerm = Record


# Special constants
# all labels staring the underscore are reserved for OO systems
_obj = stdlib.variable("obj")
_parent = stdlib.variable("parent")
_attrs = stdlib.variable("attrs")
_x = stdlib.variable('x')
_y = stdlib.variable('y')
_self = stdlib.variable('_self')
_methods = stdlib.variable("_methods")
_label = stdlib.variable("_label")
_name = stdlib.variable("_name")

_label_attrs = stdlib.string("attributes")
_label_methods = stdlib.string("methods")
_label_parent = stdlib.string('_parent')
_label_object = stdlib.string('_object')
_label_class = stdlib.string('_class')
_label_anything = stdlib.string('_anything')


_define_obj = lambda_abs(_attrs, stdlib.add_attribute(_attrs)(_label_object)(stdlib.true))

# Attributes
attr = lambda_abs_vars((_obj, _label), _obj(_label))
# Method call
method = lambda_abs_vars((_obj, _label), _obj(_label)(_obj))

# Everything starts here
the_one = _define_obj(stdlib.empty_record)

# Prototyping
inherit = lambda_abs_vars((_parent,_attrs), stdlib.overwrite_record(_parent)(_attrs))

# Class-based OO
# Class
_label_class_name = stdlib.string('_class_name')
_class = stdlib.variable('_class')

define_class = lambda_abs_vars((_name, _parent, _attrs),
                               let_vars(((_class, inherit(_parent, _attrs)),
                                         (_class, stdlib.add_attribute(_class, _label_class_name, _name))),
                                        stdlib.add_attribute(_class, _label_parent, _parent)
                                        )
                               )

is_class = lambda_abs(_class, has_label(_class)(_label_class_name))

base_class = define_class('BaseClass', the_one, stdlib.empty_record)

# Object
_label_instance = stdlib.string('_instance')
instantiate = lambda_abs_vars((_class, _attrs),
                              let(_obj, inherit(_class, _attrs),
                                  add_attribute(_obj)(_label_instance)(_class)))

is_obj = lambda_abs(_obj, has_label(_obj)(_label_instance))

_class1 = stdlib.variable('_class1')
_class2 = stdlib.variable('_class2')
_is_subclass = stdlib.variable('_is_subclass')
is_subclass = stdlib.fix\
    (lambda_abs_vars((_is_subclass, _class1, _class2),
                     if_then_else
                     (has_label(_class1)(_label_class_name))
                     (boolean_or
                      (equal(_class1(_label_class_name))
                       (_class2(_label_class_name)))
                        (_is_subclass(_class1(_label_parent))(_class2)))
                     (false)
                     ))

_is_instance = stdlib.variable('_is_instance')
is_instance = lambda_abs_vars(
                             (_obj, _class),
                             is_subclass(_obj(_label_instance))(_class)
)


def prettify(obs: Term):
    def exclude(s):
        return len(s) == 0 or s[0] == '_'
    printable = obs.__repr__()
    if isinstance(obs, Record):
        printable = {k: prettify(v) for (k, v) in obs.attributes().items() if not exclude(k)}
    if isinstance(obs, List):
        printable = [prettify(v) for v in obs.terms]
    if isinstance(obs, pgsn_term.Data):
        printable = obs.value
    return printable



