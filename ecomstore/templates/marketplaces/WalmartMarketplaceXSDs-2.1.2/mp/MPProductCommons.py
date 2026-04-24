# ./MPProductCommons.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ec44654e5389a7d5fe08059f8b0fd3f74283f889
# Generated 2016-07-17 09:43:09.571139 by PyXB version 1.2.5-DEV using Python 2.7.10.final.0
# Namespace http://walmart.com/

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:65be77c0-4c24-11e6-bd45-a820661af0fa')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5-DEV'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://walmart.com/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 22, 20)
    _Documentation = None
STD_ANON._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2000))
STD_ANON._InitializeFacetMap(STD_ANON._CF_maxLength)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 35, 20)
    _Documentation = None
STD_ANON_._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(150))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_maxLength)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 63, 20)
    _Documentation = None
STD_ANON_2._InitializeFacetMap()
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 75, 20)
    _Documentation = None
STD_ANON_3._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_maxLength)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 95, 20)
    _Documentation = None
STD_ANON_4._InitializeFacetMap()
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 105, 20)
    _Documentation = None
STD_ANON_5._InitializeFacetMap()
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 114, 20)
    _Documentation = None
STD_ANON_6._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_maxLength)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 125, 20)
    _Documentation = None
STD_ANON_7._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_maxLength)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 136, 20)
    _Documentation = None
STD_ANON_8._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_maxLength)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 156, 20)
    _Documentation = None
STD_ANON_9._InitializeFacetMap()
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 166, 20)
    _Documentation = None
STD_ANON_10._InitializeFacetMap()
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 187, 20)
    _Documentation = None
STD_ANON_11._InitializeFacetMap()
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 217, 20)
    _Documentation = None
STD_ANON_12._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_maxLength)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 232, 20)
    _Documentation = None
STD_ANON_13._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_maxLength)
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 246, 20)
    _Documentation = None
STD_ANON_14._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_maxLength)
_module_typeBindings.STD_ANON_14 = STD_ANON_14

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 260, 20)
    _Documentation = None
STD_ANON_15._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_maxLength)
_module_typeBindings.STD_ANON_15 = STD_ANON_15

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 274, 20)
    _Documentation = None
STD_ANON_16._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_maxLength)
_module_typeBindings.STD_ANON_16 = STD_ANON_16

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 288, 20)
    _Documentation = None
STD_ANON_17._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_maxLength)
_module_typeBindings.STD_ANON_17 = STD_ANON_17

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 300, 20)
    _Documentation = None
STD_ANON_18._InitializeFacetMap()
_module_typeBindings.STD_ANON_18 = STD_ANON_18

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 310, 20)
    _Documentation = None
STD_ANON_19._InitializeFacetMap()
_module_typeBindings.STD_ANON_19 = STD_ANON_19

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 320, 20)
    _Documentation = None
STD_ANON_20._InitializeFacetMap()
_module_typeBindings.STD_ANON_20 = STD_ANON_20

# Atomic simple type: [anonymous]
class STD_ANON_21 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 330, 20)
    _Documentation = None
STD_ANON_21._InitializeFacetMap()
_module_typeBindings.STD_ANON_21 = STD_ANON_21

# Atomic simple type: [anonymous]
class STD_ANON_22 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 342, 20)
    _Documentation = None
STD_ANON_22._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_22._InitializeFacetMap(STD_ANON_22._CF_maxLength)
_module_typeBindings.STD_ANON_22 = STD_ANON_22

# Atomic simple type: [anonymous]
class STD_ANON_23 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 353, 20)
    _Documentation = None
STD_ANON_23._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_23._InitializeFacetMap(STD_ANON_23._CF_maxLength)
_module_typeBindings.STD_ANON_23 = STD_ANON_23

# Atomic simple type: [anonymous]
class STD_ANON_24 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 365, 20)
    _Documentation = None
STD_ANON_24._InitializeFacetMap()
_module_typeBindings.STD_ANON_24 = STD_ANON_24

# Atomic simple type: [anonymous]
class STD_ANON_25 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 382, 20)
    _Documentation = None
STD_ANON_25._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_25._InitializeFacetMap(STD_ANON_25._CF_maxLength)
_module_typeBindings.STD_ANON_25 = STD_ANON_25

# Atomic simple type: [anonymous]
class STD_ANON_26 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 394, 20)
    _Documentation = None
STD_ANON_26._InitializeFacetMap()
_module_typeBindings.STD_ANON_26 = STD_ANON_26

# Atomic simple type: [anonymous]
class STD_ANON_27 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 404, 20)
    _Documentation = None
STD_ANON_27._InitializeFacetMap()
_module_typeBindings.STD_ANON_27 = STD_ANON_27

# Atomic simple type: [anonymous]
class STD_ANON_28 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 424, 20)
    _Documentation = None
STD_ANON_28._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_28._InitializeFacetMap(STD_ANON_28._CF_maxLength)
_module_typeBindings.STD_ANON_28 = STD_ANON_28

# Atomic simple type: [anonymous]
class STD_ANON_29 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 436, 20)
    _Documentation = None
STD_ANON_29._InitializeFacetMap()
_module_typeBindings.STD_ANON_29 = STD_ANON_29

# Atomic simple type: [anonymous]
class STD_ANON_30 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 448, 20)
    _Documentation = None
STD_ANON_30._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_30._InitializeFacetMap(STD_ANON_30._CF_maxLength)
_module_typeBindings.STD_ANON_30 = STD_ANON_30

# Atomic simple type: [anonymous]
class STD_ANON_31 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 460, 20)
    _Documentation = None
STD_ANON_31._InitializeFacetMap()
_module_typeBindings.STD_ANON_31 = STD_ANON_31

# Atomic simple type: [anonymous]
class STD_ANON_32 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 470, 20)
    _Documentation = None
STD_ANON_32._InitializeFacetMap()
_module_typeBindings.STD_ANON_32 = STD_ANON_32

# Atomic simple type: [anonymous]
class STD_ANON_33 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 490, 20)
    _Documentation = None
STD_ANON_33._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_33._InitializeFacetMap(STD_ANON_33._CF_maxLength)
_module_typeBindings.STD_ANON_33 = STD_ANON_33

# Atomic simple type: [anonymous]
class STD_ANON_34 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 504, 20)
    _Documentation = None
STD_ANON_34._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_34._InitializeFacetMap(STD_ANON_34._CF_maxLength)
_module_typeBindings.STD_ANON_34 = STD_ANON_34

# Atomic simple type: [anonymous]
class STD_ANON_35 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 518, 20)
    _Documentation = None
STD_ANON_35._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_35._InitializeFacetMap(STD_ANON_35._CF_maxLength)
_module_typeBindings.STD_ANON_35 = STD_ANON_35

# Atomic simple type: [anonymous]
class STD_ANON_36 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 532, 20)
    _Documentation = None
STD_ANON_36._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_36._InitializeFacetMap(STD_ANON_36._CF_maxLength)
_module_typeBindings.STD_ANON_36 = STD_ANON_36

# Atomic simple type: [anonymous]
class STD_ANON_37 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 546, 20)
    _Documentation = None
STD_ANON_37._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_37._InitializeFacetMap(STD_ANON_37._CF_maxLength)
_module_typeBindings.STD_ANON_37 = STD_ANON_37

# Atomic simple type: [anonymous]
class STD_ANON_38 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 560, 20)
    _Documentation = None
STD_ANON_38._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_38._InitializeFacetMap(STD_ANON_38._CF_maxLength)
_module_typeBindings.STD_ANON_38 = STD_ANON_38

# Atomic simple type: [anonymous]
class STD_ANON_39 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 574, 20)
    _Documentation = None
STD_ANON_39._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_39._InitializeFacetMap(STD_ANON_39._CF_maxLength)
_module_typeBindings.STD_ANON_39 = STD_ANON_39

# Atomic simple type: [anonymous]
class STD_ANON_40 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 588, 20)
    _Documentation = None
STD_ANON_40._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_40._InitializeFacetMap(STD_ANON_40._CF_maxLength)
_module_typeBindings.STD_ANON_40 = STD_ANON_40

# Atomic simple type: [anonymous]
class STD_ANON_41 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 602, 20)
    _Documentation = None
STD_ANON_41._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_41._InitializeFacetMap(STD_ANON_41._CF_maxLength)
_module_typeBindings.STD_ANON_41 = STD_ANON_41

# Atomic simple type: [anonymous]
class STD_ANON_42 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 616, 20)
    _Documentation = None
STD_ANON_42._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_42._InitializeFacetMap(STD_ANON_42._CF_maxLength)
_module_typeBindings.STD_ANON_42 = STD_ANON_42

# Atomic simple type: [anonymous]
class STD_ANON_43 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 630, 20)
    _Documentation = None
STD_ANON_43._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_43._InitializeFacetMap(STD_ANON_43._CF_maxLength)
_module_typeBindings.STD_ANON_43 = STD_ANON_43

# Atomic simple type: [anonymous]
class STD_ANON_44 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 644, 20)
    _Documentation = None
STD_ANON_44._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_44._InitializeFacetMap(STD_ANON_44._CF_maxLength)
_module_typeBindings.STD_ANON_44 = STD_ANON_44

# Atomic simple type: [anonymous]
class STD_ANON_45 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 658, 20)
    _Documentation = None
STD_ANON_45._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_45._InitializeFacetMap(STD_ANON_45._CF_maxLength)
_module_typeBindings.STD_ANON_45 = STD_ANON_45

# Atomic simple type: [anonymous]
class STD_ANON_46 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 672, 20)
    _Documentation = None
STD_ANON_46._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_46._InitializeFacetMap(STD_ANON_46._CF_maxLength)
_module_typeBindings.STD_ANON_46 = STD_ANON_46

# Atomic simple type: [anonymous]
class STD_ANON_47 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 686, 20)
    _Documentation = None
STD_ANON_47._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_47._InitializeFacetMap(STD_ANON_47._CF_maxLength)
_module_typeBindings.STD_ANON_47 = STD_ANON_47

# Atomic simple type: [anonymous]
class STD_ANON_48 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 700, 20)
    _Documentation = None
STD_ANON_48._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_48._InitializeFacetMap(STD_ANON_48._CF_maxLength)
_module_typeBindings.STD_ANON_48 = STD_ANON_48

# Atomic simple type: [anonymous]
class STD_ANON_49 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 714, 20)
    _Documentation = None
STD_ANON_49._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_49._InitializeFacetMap(STD_ANON_49._CF_maxLength)
_module_typeBindings.STD_ANON_49 = STD_ANON_49

# Atomic simple type: [anonymous]
class STD_ANON_50 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 736, 20)
    _Documentation = None
STD_ANON_50._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_50._InitializeFacetMap(STD_ANON_50._CF_maxLength)
_module_typeBindings.STD_ANON_50 = STD_ANON_50

# Atomic simple type: [anonymous]
class STD_ANON_51 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 750, 20)
    _Documentation = None
STD_ANON_51._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_51._InitializeFacetMap(STD_ANON_51._CF_maxLength)
_module_typeBindings.STD_ANON_51 = STD_ANON_51

# Atomic simple type: [anonymous]
class STD_ANON_52 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 764, 20)
    _Documentation = None
STD_ANON_52._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_52._InitializeFacetMap(STD_ANON_52._CF_maxLength)
_module_typeBindings.STD_ANON_52 = STD_ANON_52

# Atomic simple type: [anonymous]
class STD_ANON_53 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 778, 20)
    _Documentation = None
STD_ANON_53._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_53._InitializeFacetMap(STD_ANON_53._CF_maxLength)
_module_typeBindings.STD_ANON_53 = STD_ANON_53

# Atomic simple type: [anonymous]
class STD_ANON_54 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 792, 20)
    _Documentation = None
STD_ANON_54._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_54._InitializeFacetMap(STD_ANON_54._CF_maxLength)
_module_typeBindings.STD_ANON_54 = STD_ANON_54

# Atomic simple type: [anonymous]
class STD_ANON_55 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 804, 20)
    _Documentation = None
STD_ANON_55._InitializeFacetMap()
_module_typeBindings.STD_ANON_55 = STD_ANON_55

# Atomic simple type: [anonymous]
class STD_ANON_56 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 814, 20)
    _Documentation = None
STD_ANON_56._InitializeFacetMap()
_module_typeBindings.STD_ANON_56 = STD_ANON_56

# Atomic simple type: [anonymous]
class STD_ANON_57 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 824, 20)
    _Documentation = None
STD_ANON_57._InitializeFacetMap()
_module_typeBindings.STD_ANON_57 = STD_ANON_57

# Atomic simple type: [anonymous]
class STD_ANON_58 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 836, 20)
    _Documentation = None
STD_ANON_58._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_58._InitializeFacetMap(STD_ANON_58._CF_maxLength)
_module_typeBindings.STD_ANON_58 = STD_ANON_58

# Atomic simple type: [anonymous]
class STD_ANON_59 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 850, 20)
    _Documentation = None
STD_ANON_59._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_59._InitializeFacetMap(STD_ANON_59._CF_maxLength)
_module_typeBindings.STD_ANON_59 = STD_ANON_59

# Atomic simple type: [anonymous]
class STD_ANON_60 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 864, 20)
    _Documentation = None
STD_ANON_60._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_60._InitializeFacetMap(STD_ANON_60._CF_maxLength)
_module_typeBindings.STD_ANON_60 = STD_ANON_60

# Atomic simple type: [anonymous]
class STD_ANON_61 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 886, 20)
    _Documentation = None
STD_ANON_61._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_61._InitializeFacetMap(STD_ANON_61._CF_maxLength)
_module_typeBindings.STD_ANON_61 = STD_ANON_61

# Atomic simple type: [anonymous]
class STD_ANON_62 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 900, 20)
    _Documentation = None
STD_ANON_62._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_62._InitializeFacetMap(STD_ANON_62._CF_maxLength)
_module_typeBindings.STD_ANON_62 = STD_ANON_62

# Atomic simple type: [anonymous]
class STD_ANON_63 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 914, 20)
    _Documentation = None
STD_ANON_63._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_63._InitializeFacetMap(STD_ANON_63._CF_maxLength)
_module_typeBindings.STD_ANON_63 = STD_ANON_63

# Atomic simple type: [anonymous]
class STD_ANON_64 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 928, 20)
    _Documentation = None
STD_ANON_64._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_64._InitializeFacetMap(STD_ANON_64._CF_maxLength)
_module_typeBindings.STD_ANON_64 = STD_ANON_64

# Atomic simple type: [anonymous]
class STD_ANON_65 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 942, 20)
    _Documentation = None
STD_ANON_65._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_65._InitializeFacetMap(STD_ANON_65._CF_maxLength)
_module_typeBindings.STD_ANON_65 = STD_ANON_65

# Atomic simple type: [anonymous]
class STD_ANON_66 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 956, 20)
    _Documentation = None
STD_ANON_66._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_66._InitializeFacetMap(STD_ANON_66._CF_maxLength)
_module_typeBindings.STD_ANON_66 = STD_ANON_66

# Atomic simple type: [anonymous]
class STD_ANON_67 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 970, 20)
    _Documentation = None
STD_ANON_67._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_67._InitializeFacetMap(STD_ANON_67._CF_maxLength)
_module_typeBindings.STD_ANON_67 = STD_ANON_67

# Atomic simple type: [anonymous]
class STD_ANON_68 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 984, 20)
    _Documentation = None
STD_ANON_68._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_68._InitializeFacetMap(STD_ANON_68._CF_maxLength)
_module_typeBindings.STD_ANON_68 = STD_ANON_68

# Atomic simple type: [anonymous]
class STD_ANON_69 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 998, 20)
    _Documentation = None
STD_ANON_69._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_69._InitializeFacetMap(STD_ANON_69._CF_maxLength)
_module_typeBindings.STD_ANON_69 = STD_ANON_69

# Atomic simple type: [anonymous]
class STD_ANON_70 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1010, 20)
    _Documentation = None
STD_ANON_70._InitializeFacetMap()
_module_typeBindings.STD_ANON_70 = STD_ANON_70

# Atomic simple type: [anonymous]
class STD_ANON_71 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1022, 20)
    _Documentation = None
STD_ANON_71._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_71._InitializeFacetMap(STD_ANON_71._CF_maxLength)
_module_typeBindings.STD_ANON_71 = STD_ANON_71

# Atomic simple type: [anonymous]
class STD_ANON_72 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1036, 20)
    _Documentation = None
STD_ANON_72._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_72._InitializeFacetMap(STD_ANON_72._CF_maxLength)
_module_typeBindings.STD_ANON_72 = STD_ANON_72

# Atomic simple type: [anonymous]
class STD_ANON_73 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1050, 20)
    _Documentation = None
STD_ANON_73._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_73._InitializeFacetMap(STD_ANON_73._CF_maxLength)
_module_typeBindings.STD_ANON_73 = STD_ANON_73

# Atomic simple type: [anonymous]
class STD_ANON_74 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1064, 20)
    _Documentation = None
STD_ANON_74._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_74._InitializeFacetMap(STD_ANON_74._CF_maxLength)
_module_typeBindings.STD_ANON_74 = STD_ANON_74

# Atomic simple type: [anonymous]
class STD_ANON_75 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1078, 20)
    _Documentation = None
STD_ANON_75._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_75._InitializeFacetMap(STD_ANON_75._CF_maxLength)
_module_typeBindings.STD_ANON_75 = STD_ANON_75

# Atomic simple type: [anonymous]
class STD_ANON_76 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1100, 20)
    _Documentation = None
STD_ANON_76._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_76._InitializeFacetMap(STD_ANON_76._CF_maxLength)
_module_typeBindings.STD_ANON_76 = STD_ANON_76

# Atomic simple type: [anonymous]
class STD_ANON_77 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1114, 20)
    _Documentation = None
STD_ANON_77._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_77._InitializeFacetMap(STD_ANON_77._CF_maxLength)
_module_typeBindings.STD_ANON_77 = STD_ANON_77

# Atomic simple type: [anonymous]
class STD_ANON_78 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1128, 20)
    _Documentation = None
STD_ANON_78._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_78._InitializeFacetMap(STD_ANON_78._CF_maxLength)
_module_typeBindings.STD_ANON_78 = STD_ANON_78

# Atomic simple type: [anonymous]
class STD_ANON_79 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1142, 20)
    _Documentation = None
STD_ANON_79._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_79._InitializeFacetMap(STD_ANON_79._CF_maxLength)
_module_typeBindings.STD_ANON_79 = STD_ANON_79

# Atomic simple type: [anonymous]
class STD_ANON_80 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1159, 20)
    _Documentation = None
STD_ANON_80._InitializeFacetMap()
_module_typeBindings.STD_ANON_80 = STD_ANON_80

# Atomic simple type: [anonymous]
class STD_ANON_81 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1170, 20)
    _Documentation = None
STD_ANON_81._InitializeFacetMap()
_module_typeBindings.STD_ANON_81 = STD_ANON_81

# Atomic simple type: [anonymous]
class STD_ANON_82 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1182, 20)
    _Documentation = None
STD_ANON_82._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_82._InitializeFacetMap(STD_ANON_82._CF_maxLength)
_module_typeBindings.STD_ANON_82 = STD_ANON_82

# Atomic simple type: [anonymous]
class STD_ANON_83 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1193, 20)
    _Documentation = None
STD_ANON_83._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_83._InitializeFacetMap(STD_ANON_83._CF_maxLength)
_module_typeBindings.STD_ANON_83 = STD_ANON_83

# Atomic simple type: [anonymous]
class STD_ANON_84 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1207, 20)
    _Documentation = None
STD_ANON_84._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_84._InitializeFacetMap(STD_ANON_84._CF_maxLength)
_module_typeBindings.STD_ANON_84 = STD_ANON_84

# Atomic simple type: [anonymous]
class STD_ANON_85 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1218, 20)
    _Documentation = None
STD_ANON_85._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_85._InitializeFacetMap(STD_ANON_85._CF_maxLength)
_module_typeBindings.STD_ANON_85 = STD_ANON_85

# Atomic simple type: [anonymous]
class STD_ANON_86 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1232, 20)
    _Documentation = None
STD_ANON_86._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_86._InitializeFacetMap(STD_ANON_86._CF_maxLength)
_module_typeBindings.STD_ANON_86 = STD_ANON_86

# Atomic simple type: [anonymous]
class STD_ANON_87 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1246, 20)
    _Documentation = None
STD_ANON_87._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_87._InitializeFacetMap(STD_ANON_87._CF_maxLength)
_module_typeBindings.STD_ANON_87 = STD_ANON_87

# Atomic simple type: [anonymous]
class STD_ANON_88 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1260, 20)
    _Documentation = None
STD_ANON_88._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_88._InitializeFacetMap(STD_ANON_88._CF_maxLength)
_module_typeBindings.STD_ANON_88 = STD_ANON_88

# Atomic simple type: [anonymous]
class STD_ANON_89 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1274, 20)
    _Documentation = None
STD_ANON_89._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_89._InitializeFacetMap(STD_ANON_89._CF_maxLength)
_module_typeBindings.STD_ANON_89 = STD_ANON_89

# Atomic simple type: [anonymous]
class STD_ANON_90 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1288, 20)
    _Documentation = None
STD_ANON_90._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_90._InitializeFacetMap(STD_ANON_90._CF_maxLength)
_module_typeBindings.STD_ANON_90 = STD_ANON_90

# Atomic simple type: [anonymous]
class STD_ANON_91 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1299, 20)
    _Documentation = None
STD_ANON_91._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_91._InitializeFacetMap(STD_ANON_91._CF_maxLength)
_module_typeBindings.STD_ANON_91 = STD_ANON_91

# Atomic simple type: [anonymous]
class STD_ANON_92 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1313, 20)
    _Documentation = None
STD_ANON_92._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_92._InitializeFacetMap(STD_ANON_92._CF_maxLength)
_module_typeBindings.STD_ANON_92 = STD_ANON_92

# Atomic simple type: [anonymous]
class STD_ANON_93 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1325, 20)
    _Documentation = None
STD_ANON_93._InitializeFacetMap()
_module_typeBindings.STD_ANON_93 = STD_ANON_93

# Atomic simple type: [anonymous]
class STD_ANON_94 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1334, 20)
    _Documentation = None
STD_ANON_94._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_94._InitializeFacetMap(STD_ANON_94._CF_maxLength)
_module_typeBindings.STD_ANON_94 = STD_ANON_94

# Atomic simple type: [anonymous]
class STD_ANON_95 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1351, 20)
    _Documentation = None
STD_ANON_95._InitializeFacetMap()
_module_typeBindings.STD_ANON_95 = STD_ANON_95

# Atomic simple type: [anonymous]
class STD_ANON_96 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1362, 20)
    _Documentation = None
STD_ANON_96._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_96._InitializeFacetMap(STD_ANON_96._CF_maxLength)
_module_typeBindings.STD_ANON_96 = STD_ANON_96

# Atomic simple type: [anonymous]
class STD_ANON_97 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1379, 20)
    _Documentation = None
STD_ANON_97._InitializeFacetMap()
_module_typeBindings.STD_ANON_97 = STD_ANON_97

# Atomic simple type: [anonymous]
class STD_ANON_98 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1404, 20)
    _Documentation = None
STD_ANON_98._InitializeFacetMap()
_module_typeBindings.STD_ANON_98 = STD_ANON_98

# Atomic simple type: [anonymous]
class STD_ANON_99 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1415, 20)
    _Documentation = None
STD_ANON_99._InitializeFacetMap()
_module_typeBindings.STD_ANON_99 = STD_ANON_99

# Atomic simple type: [anonymous]
class STD_ANON_100 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1424, 20)
    _Documentation = None
STD_ANON_100._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_100._InitializeFacetMap(STD_ANON_100._CF_maxLength)
_module_typeBindings.STD_ANON_100 = STD_ANON_100

# Atomic simple type: [anonymous]
class STD_ANON_101 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1438, 20)
    _Documentation = None
STD_ANON_101._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_101._InitializeFacetMap(STD_ANON_101._CF_maxLength)
_module_typeBindings.STD_ANON_101 = STD_ANON_101

# Atomic simple type: [anonymous]
class STD_ANON_102 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1452, 20)
    _Documentation = None
STD_ANON_102._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_102._InitializeFacetMap(STD_ANON_102._CF_maxLength)
_module_typeBindings.STD_ANON_102 = STD_ANON_102

# Atomic simple type: [anonymous]
class STD_ANON_103 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1469, 20)
    _Documentation = None
STD_ANON_103._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(150))
STD_ANON_103._InitializeFacetMap(STD_ANON_103._CF_maxLength)
_module_typeBindings.STD_ANON_103 = STD_ANON_103

# Atomic simple type: [anonymous]
class STD_ANON_104 (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1482, 20)
    _Documentation = None
STD_ANON_104._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2000))
STD_ANON_104._InitializeFacetMap(STD_ANON_104._CF_maxLength)
_module_typeBindings.STD_ANON_104 = STD_ANON_104

# Atomic simple type: [anonymous]
class STD_ANON_105 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1495, 20)
    _Documentation = None
STD_ANON_105._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_105._InitializeFacetMap(STD_ANON_105._CF_maxLength)
_module_typeBindings.STD_ANON_105 = STD_ANON_105

# Atomic simple type: [anonymous]
class STD_ANON_106 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1519, 20)
    _Documentation = None
STD_ANON_106._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_106, enum_prefix=None)
STD_ANON_106.UPC = STD_ANON_106._CF_enumeration.addEnumeration(unicode_value='UPC', tag='UPC')
STD_ANON_106.GTIN = STD_ANON_106._CF_enumeration.addEnumeration(unicode_value='GTIN', tag='GTIN')
STD_ANON_106.EAN = STD_ANON_106._CF_enumeration.addEnumeration(unicode_value='EAN', tag='EAN')
STD_ANON_106.ISSN = STD_ANON_106._CF_enumeration.addEnumeration(unicode_value='ISSN', tag='ISSN')
STD_ANON_106.ISBN = STD_ANON_106._CF_enumeration.addEnumeration(unicode_value='ISBN', tag='ISBN')
STD_ANON_106._InitializeFacetMap(STD_ANON_106._CF_enumeration)
_module_typeBindings.STD_ANON_106 = STD_ANON_106

# Atomic simple type: [anonymous]
class STD_ANON_107 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1536, 20)
    _Documentation = None
STD_ANON_107._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(14))
STD_ANON_107._InitializeFacetMap(STD_ANON_107._CF_maxLength)
_module_typeBindings.STD_ANON_107 = STD_ANON_107

# Atomic simple type: [anonymous]
class STD_ANON_108 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1553, 20)
    _Documentation = None
STD_ANON_108._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_108._InitializeFacetMap(STD_ANON_108._CF_maxLength)
_module_typeBindings.STD_ANON_108 = STD_ANON_108

# Atomic simple type: [anonymous]
class STD_ANON_109 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1566, 20)
    _Documentation = None
STD_ANON_109._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_109._InitializeFacetMap(STD_ANON_109._CF_maxLength)
_module_typeBindings.STD_ANON_109 = STD_ANON_109

# Atomic simple type: [anonymous]
class STD_ANON_110 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1583, 20)
    _Documentation = None
STD_ANON_110._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_110, enum_prefix=None)
STD_ANON_110.Lithium_Ion = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Lithium Ion', tag='Lithium_Ion')
STD_ANON_110.Nickel_Metal_Hydride = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Nickel Metal Hydride', tag='Nickel_Metal_Hydride')
STD_ANON_110.Does_Not_Contain_a_Battery = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Does Not Contain a Battery', tag='Does_Not_Contain_a_Battery')
STD_ANON_110.Lead_Acid_Non_Spillable = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Lead Acid (Non-Spillable)', tag='Lead_Acid_Non_Spillable')
STD_ANON_110.Lithium_Primary = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Lithium Primary', tag='Lithium_Primary')
STD_ANON_110.Multiple_Types = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Multiple Types', tag='Multiple_Types')
STD_ANON_110.Carbon_Zinc = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Carbon Zinc', tag='Carbon_Zinc')
STD_ANON_110.Magnesium = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Magnesium', tag='Magnesium')
STD_ANON_110.Mercury = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Mercury', tag='Mercury')
STD_ANON_110.Thermal = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Thermal', tag='Thermal')
STD_ANON_110.Other = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
STD_ANON_110.Nickel_Cadmium = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Nickel Cadmium', tag='Nickel_Cadmium')
STD_ANON_110.Lead_Acid = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Lead Acid', tag='Lead_Acid')
STD_ANON_110.Silver = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Silver', tag='Silver')
STD_ANON_110.Alkaline = STD_ANON_110._CF_enumeration.addEnumeration(unicode_value='Alkaline', tag='Alkaline')
STD_ANON_110._InitializeFacetMap(STD_ANON_110._CF_enumeration)
_module_typeBindings.STD_ANON_110 = STD_ANON_110

# Atomic simple type: [anonymous]
class STD_ANON_111 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1610, 20)
    _Documentation = None
STD_ANON_111._InitializeFacetMap()
_module_typeBindings.STD_ANON_111 = STD_ANON_111

# Atomic simple type: [anonymous]
class STD_ANON_112 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1628, 20)
    _Documentation = None
STD_ANON_112._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_112._InitializeFacetMap(STD_ANON_112._CF_maxLength)
_module_typeBindings.STD_ANON_112 = STD_ANON_112

# Atomic simple type: [anonymous]
class STD_ANON_113 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1641, 20)
    _Documentation = None
STD_ANON_113._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_113._InitializeFacetMap(STD_ANON_113._CF_maxLength)
_module_typeBindings.STD_ANON_113 = STD_ANON_113

# Atomic simple type: [anonymous]
class STD_ANON_114 (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1658, 20)
    _Documentation = None
STD_ANON_114._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2000))
STD_ANON_114._InitializeFacetMap(STD_ANON_114._CF_maxLength)
_module_typeBindings.STD_ANON_114 = STD_ANON_114

# Atomic simple type: [anonymous]
class STD_ANON_115 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1671, 20)
    _Documentation = None
STD_ANON_115._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_115._InitializeFacetMap(STD_ANON_115._CF_maxLength)
_module_typeBindings.STD_ANON_115 = STD_ANON_115

# Atomic simple type: [anonymous]
class STD_ANON_116 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1688, 20)
    _Documentation = None
STD_ANON_116._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_116._InitializeFacetMap(STD_ANON_116._CF_maxLength)
_module_typeBindings.STD_ANON_116 = STD_ANON_116

# Atomic simple type: [anonymous]
class STD_ANON_117 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1701, 20)
    _Documentation = None
STD_ANON_117._InitializeFacetMap()
_module_typeBindings.STD_ANON_117 = STD_ANON_117

# Atomic simple type: [anonymous]
class STD_ANON_118 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1716, 20)
    _Documentation = None
STD_ANON_118._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_118._InitializeFacetMap(STD_ANON_118._CF_maxLength)
_module_typeBindings.STD_ANON_118 = STD_ANON_118

# Atomic simple type: [anonymous]
class STD_ANON_119 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1729, 20)
    _Documentation = None
STD_ANON_119._InitializeFacetMap()
_module_typeBindings.STD_ANON_119 = STD_ANON_119

# Atomic simple type: [anonymous]
class STD_ANON_120 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1744, 20)
    _Documentation = None
STD_ANON_120._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_120._InitializeFacetMap(STD_ANON_120._CF_maxLength)
_module_typeBindings.STD_ANON_120 = STD_ANON_120

# Atomic simple type: [anonymous]
class STD_ANON_121 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1757, 20)
    _Documentation = None
STD_ANON_121._InitializeFacetMap()
_module_typeBindings.STD_ANON_121 = STD_ANON_121

# Atomic simple type: [anonymous]
class STD_ANON_122 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1772, 20)
    _Documentation = None
STD_ANON_122._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_122._InitializeFacetMap(STD_ANON_122._CF_maxLength)
_module_typeBindings.STD_ANON_122 = STD_ANON_122

# Atomic simple type: [anonymous]
class STD_ANON_123 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1785, 20)
    _Documentation = None
STD_ANON_123._InitializeFacetMap()
_module_typeBindings.STD_ANON_123 = STD_ANON_123

# Atomic simple type: [anonymous]
class STD_ANON_124 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1796, 20)
    _Documentation = None
STD_ANON_124._InitializeFacetMap()
_module_typeBindings.STD_ANON_124 = STD_ANON_124

# Atomic simple type: [anonymous]
class STD_ANON_125 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1811, 20)
    _Documentation = None
STD_ANON_125._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_125._InitializeFacetMap(STD_ANON_125._CF_maxLength)
_module_typeBindings.STD_ANON_125 = STD_ANON_125

# Atomic simple type: [anonymous]
class STD_ANON_126 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1824, 20)
    _Documentation = None
STD_ANON_126._InitializeFacetMap()
_module_typeBindings.STD_ANON_126 = STD_ANON_126

# Atomic simple type: [anonymous]
class STD_ANON_127 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1839, 20)
    _Documentation = None
STD_ANON_127._InitializeFacetMap()
_module_typeBindings.STD_ANON_127 = STD_ANON_127

# Atomic simple type: [anonymous]
class STD_ANON_128 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1850, 20)
    _Documentation = None
STD_ANON_128._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_128._InitializeFacetMap(STD_ANON_128._CF_maxLength)
_module_typeBindings.STD_ANON_128 = STD_ANON_128

# Atomic simple type: [anonymous]
class STD_ANON_129 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1863, 20)
    _Documentation = None
STD_ANON_129._InitializeFacetMap()
_module_typeBindings.STD_ANON_129 = STD_ANON_129

# Atomic simple type: [anonymous]
class STD_ANON_130 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1886, 20)
    _Documentation = None
STD_ANON_130._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_130._InitializeFacetMap(STD_ANON_130._CF_maxLength)
_module_typeBindings.STD_ANON_130 = STD_ANON_130

# Atomic simple type: [anonymous]
class STD_ANON_131 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1899, 20)
    _Documentation = None
STD_ANON_131._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
STD_ANON_131._InitializeFacetMap(STD_ANON_131._CF_maxLength)
_module_typeBindings.STD_ANON_131 = STD_ANON_131

# Atomic simple type: {http://walmart.com/}AngleUnitOfMeasure
class AngleUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AngleUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1907, 5)
    _Documentation = None
AngleUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AngleUnitOfMeasure, enum_prefix=None)
AngleUnitOfMeasure.Degree = AngleUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Degree', tag='Degree')
AngleUnitOfMeasure.Radian = AngleUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Radian', tag='Radian')
AngleUnitOfMeasure.Steradian = AngleUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Steradian', tag='Steradian')
AngleUnitOfMeasure._InitializeFacetMap(AngleUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AngleUnitOfMeasure', AngleUnitOfMeasure)
_module_typeBindings.AngleUnitOfMeasure = AngleUnitOfMeasure

# Atomic simple type: {http://walmart.com/}AreaUnitOfMeasure
class AreaUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AreaUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1914, 5)
    _Documentation = None
AreaUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AreaUnitOfMeasure, enum_prefix=None)
AreaUnitOfMeasure.Square_Centimeters = AreaUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Square Centimeters', tag='Square_Centimeters')
AreaUnitOfMeasure.Square_Millimeters = AreaUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Square Millimeters', tag='Square_Millimeters')
AreaUnitOfMeasure.Square_Feet = AreaUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Square Feet', tag='Square_Feet')
AreaUnitOfMeasure.Square_Inches = AreaUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Square Inches', tag='Square_Inches')
AreaUnitOfMeasure.Square_Meters = AreaUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Square Meters', tag='Square_Meters')
AreaUnitOfMeasure.Square_Yards = AreaUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Square Yards', tag='Square_Yards')
AreaUnitOfMeasure._InitializeFacetMap(AreaUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AreaUnitOfMeasure', AreaUnitOfMeasure)
_module_typeBindings.AreaUnitOfMeasure = AreaUnitOfMeasure

# Atomic simple type: {http://walmart.com/}LengthUnitOfMeasure
class LengthUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LengthUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1924, 5)
    _Documentation = None
LengthUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LengthUnitOfMeasure, enum_prefix=None)
LengthUnitOfMeasure.Inches = LengthUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Inches', tag='Inches')
LengthUnitOfMeasure.Micrometers = LengthUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Micrometers', tag='Micrometers')
LengthUnitOfMeasure.Feet = LengthUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Feet', tag='Feet')
LengthUnitOfMeasure.Millimeters = LengthUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Millimeters', tag='Millimeters')
LengthUnitOfMeasure.Centimeters = LengthUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Centimeters', tag='Centimeters')
LengthUnitOfMeasure.Meters = LengthUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Meters', tag='Meters')
LengthUnitOfMeasure.Yards = LengthUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Yards', tag='Yards')
LengthUnitOfMeasure.French = LengthUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='French', tag='French')
LengthUnitOfMeasure.Miles = LengthUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Miles', tag='Miles')
LengthUnitOfMeasure.Mil = LengthUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Mil', tag='Mil')
LengthUnitOfMeasure._InitializeFacetMap(LengthUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LengthUnitOfMeasure', LengthUnitOfMeasure)
_module_typeBindings.LengthUnitOfMeasure = LengthUnitOfMeasure

# Atomic simple type: {http://walmart.com/}PercentageUnitOfMeasure
class PercentageUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentageUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1938, 5)
    _Documentation = None
PercentageUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PercentageUnitOfMeasure, enum_prefix=None)
PercentageUnitOfMeasure.Percentage = PercentageUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Percentage', tag='Percentage')
PercentageUnitOfMeasure._InitializeFacetMap(PercentageUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PercentageUnitOfMeasure', PercentageUnitOfMeasure)
_module_typeBindings.PercentageUnitOfMeasure = PercentageUnitOfMeasure

# Atomic simple type: {http://walmart.com/}VolumetricFlowRateUnitOfMeasure
class VolumetricFlowRateUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VolumetricFlowRateUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1943, 5)
    _Documentation = None
VolumetricFlowRateUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumetricFlowRateUnitOfMeasure, enum_prefix=None)
VolumetricFlowRateUnitOfMeasure.liters_per_second = VolumetricFlowRateUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='liters per second', tag='liters_per_second')
VolumetricFlowRateUnitOfMeasure.cubic_meters_per_second = VolumetricFlowRateUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='cubic meters per second', tag='cubic_meters_per_second')
VolumetricFlowRateUnitOfMeasure.cubic_feet_per_second = VolumetricFlowRateUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='cubic feet per second', tag='cubic_feet_per_second')
VolumetricFlowRateUnitOfMeasure.cubic_meters_per_minute = VolumetricFlowRateUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='cubic meters per minute', tag='cubic_meters_per_minute')
VolumetricFlowRateUnitOfMeasure.gallons_per_second = VolumetricFlowRateUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='gallons per second', tag='gallons_per_second')
VolumetricFlowRateUnitOfMeasure.cubic_feet_per_minute = VolumetricFlowRateUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='cubic feet per minute', tag='cubic_feet_per_minute')
VolumetricFlowRateUnitOfMeasure.liters_per_minute = VolumetricFlowRateUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='liters per minute', tag='liters_per_minute')
VolumetricFlowRateUnitOfMeasure.gallons_per_minute = VolumetricFlowRateUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='gallons per minute', tag='gallons_per_minute')
VolumetricFlowRateUnitOfMeasure._InitializeFacetMap(VolumetricFlowRateUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VolumetricFlowRateUnitOfMeasure', VolumetricFlowRateUnitOfMeasure)
_module_typeBindings.VolumetricFlowRateUnitOfMeasure = VolumetricFlowRateUnitOfMeasure

# Atomic simple type: {http://walmart.com/}PressureUnitOfMeasure
class PressureUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PressureUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1955, 5)
    _Documentation = None
PressureUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PressureUnitOfMeasure, enum_prefix=None)
PressureUnitOfMeasure.Pounds_Per_Square_Inch = PressureUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Pounds Per Square Inch', tag='Pounds_Per_Square_Inch')
PressureUnitOfMeasure.Barye = PressureUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Barye', tag='Barye')
PressureUnitOfMeasure.Pieze = PressureUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Pieze', tag='Pieze')
PressureUnitOfMeasure.Pascal = PressureUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Pascal', tag='Pascal')
PressureUnitOfMeasure.PsigBar = PressureUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Psig/Bar', tag='PsigBar')
PressureUnitOfMeasure.Bar = PressureUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Bar', tag='Bar')
PressureUnitOfMeasure.Torr = PressureUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Torr', tag='Torr')
PressureUnitOfMeasure._InitializeFacetMap(PressureUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PressureUnitOfMeasure', PressureUnitOfMeasure)
_module_typeBindings.PressureUnitOfMeasure = PressureUnitOfMeasure

# Atomic simple type: {http://walmart.com/}VolumeUnitOfMeasure
class VolumeUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VolumeUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1966, 5)
    _Documentation = None
VolumeUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumeUnitOfMeasure, enum_prefix=None)
VolumeUnitOfMeasure.US_Gallons = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='US Gallons', tag='US_Gallons')
VolumeUnitOfMeasure.Imperial_UK_Gallons = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Imperial (UK) Gallons', tag='Imperial_UK_Gallons')
VolumeUnitOfMeasure.Cubic_Feet = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Cubic Feet', tag='Cubic_Feet')
VolumeUnitOfMeasure.Cubic_Inches = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Cubic Inches', tag='Cubic_Inches')
VolumeUnitOfMeasure.Cubic_Centimeters = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Cubic Centimeters', tag='Cubic_Centimeters')
VolumeUnitOfMeasure.Cubic_Meters = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Cubic Meters', tag='Cubic_Meters')
VolumeUnitOfMeasure.Milliliters = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Milliliters', tag='Milliliters')
VolumeUnitOfMeasure.Cubic_Yards = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Cubic Yards', tag='Cubic_Yards')
VolumeUnitOfMeasure.Fluid_Ounces = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Fluid Ounces', tag='Fluid_Ounces')
VolumeUnitOfMeasure.Quarts = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Quarts', tag='Quarts')
VolumeUnitOfMeasure.Liters = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Liters', tag='Liters')
VolumeUnitOfMeasure.Pints = VolumeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Pints', tag='Pints')
VolumeUnitOfMeasure._InitializeFacetMap(VolumeUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VolumeUnitOfMeasure', VolumeUnitOfMeasure)
_module_typeBindings.VolumeUnitOfMeasure = VolumeUnitOfMeasure

# Atomic simple type: {http://walmart.com/}CurrencyUnitOfMeasure
class CurrencyUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1982, 5)
    _Documentation = None
CurrencyUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CurrencyUnitOfMeasure, enum_prefix=None)
CurrencyUnitOfMeasure.USD = CurrencyUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='USD', tag='USD')
CurrencyUnitOfMeasure._InitializeFacetMap(CurrencyUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CurrencyUnitOfMeasure', CurrencyUnitOfMeasure)
_module_typeBindings.CurrencyUnitOfMeasure = CurrencyUnitOfMeasure

# Atomic simple type: {http://walmart.com/}ResolutionUnitOfMeasure
class ResolutionUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResolutionUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1987, 5)
    _Documentation = None
ResolutionUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ResolutionUnitOfMeasure, enum_prefix=None)
ResolutionUnitOfMeasure.Dots_Per_Square_Inch = ResolutionUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Dots Per Square Inch', tag='Dots_Per_Square_Inch')
ResolutionUnitOfMeasure.Pixels_Per_Inch = ResolutionUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Pixels Per Inch', tag='Pixels_Per_Inch')
ResolutionUnitOfMeasure.Volumetric_Pixels = ResolutionUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Volumetric Pixels', tag='Volumetric_Pixels')
ResolutionUnitOfMeasure.Megapixels = ResolutionUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Megapixels', tag='Megapixels')
ResolutionUnitOfMeasure.Resolution_Element = ResolutionUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Resolution Element', tag='Resolution_Element')
ResolutionUnitOfMeasure.Surface_Element = ResolutionUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Surface Element', tag='Surface_Element')
ResolutionUnitOfMeasure.Dots_Per_Inch = ResolutionUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Dots Per Inch', tag='Dots_Per_Inch')
ResolutionUnitOfMeasure.Texels = ResolutionUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Texels', tag='Texels')
ResolutionUnitOfMeasure._InitializeFacetMap(ResolutionUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ResolutionUnitOfMeasure', ResolutionUnitOfMeasure)
_module_typeBindings.ResolutionUnitOfMeasure = ResolutionUnitOfMeasure

# Atomic simple type: {http://walmart.com/}ElectricalMeasurementUnitOfMeasure
class ElectricalMeasurementUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ElectricalMeasurementUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1999, 5)
    _Documentation = None
ElectricalMeasurementUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ElectricalMeasurementUnitOfMeasure, enum_prefix=None)
ElectricalMeasurementUnitOfMeasure.Volts = ElectricalMeasurementUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Volts', tag='Volts')
ElectricalMeasurementUnitOfMeasure.Coulombs = ElectricalMeasurementUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Coulombs', tag='Coulombs')
ElectricalMeasurementUnitOfMeasure.Amps = ElectricalMeasurementUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Amps', tag='Amps')
ElectricalMeasurementUnitOfMeasure._InitializeFacetMap(ElectricalMeasurementUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ElectricalMeasurementUnitOfMeasure', ElectricalMeasurementUnitOfMeasure)
_module_typeBindings.ElectricalMeasurementUnitOfMeasure = ElectricalMeasurementUnitOfMeasure

# Atomic simple type: {http://walmart.com/}WeightUnitOfMeasure
class WeightUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WeightUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 2006, 5)
    _Documentation = None
WeightUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WeightUnitOfMeasure, enum_prefix=None)
WeightUnitOfMeasure.Kilograms_Per_Meter = WeightUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Kilograms Per Meter', tag='Kilograms_Per_Meter')
WeightUnitOfMeasure.Kilograms = WeightUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Kilograms', tag='Kilograms')
WeightUnitOfMeasure.Milligrams = WeightUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Milligrams', tag='Milligrams')
WeightUnitOfMeasure.Ounces = WeightUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Ounces', tag='Ounces')
WeightUnitOfMeasure.Pounds = WeightUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Pounds', tag='Pounds')
WeightUnitOfMeasure.Grams = WeightUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Grams', tag='Grams')
WeightUnitOfMeasure.Carat = WeightUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Carat', tag='Carat')
WeightUnitOfMeasure._InitializeFacetMap(WeightUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WeightUnitOfMeasure', WeightUnitOfMeasure)
_module_typeBindings.WeightUnitOfMeasure = WeightUnitOfMeasure

# Atomic simple type: {http://walmart.com/}FuelEconomyUnitOfMeasure
class FuelEconomyUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FuelEconomyUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 2017, 5)
    _Documentation = None
FuelEconomyUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FuelEconomyUnitOfMeasure, enum_prefix=None)
FuelEconomyUnitOfMeasure.Miles_Per_Gallon = FuelEconomyUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Miles Per Gallon', tag='Miles_Per_Gallon')
FuelEconomyUnitOfMeasure._InitializeFacetMap(FuelEconomyUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FuelEconomyUnitOfMeasure', FuelEconomyUnitOfMeasure)
_module_typeBindings.FuelEconomyUnitOfMeasure = FuelEconomyUnitOfMeasure

# Atomic simple type: {http://walmart.com/}TimeUnitOfMeasure
class TimeUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 2022, 5)
    _Documentation = None
TimeUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TimeUnitOfMeasure, enum_prefix=None)
TimeUnitOfMeasure.Minutes = TimeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Minutes', tag='Minutes')
TimeUnitOfMeasure.Seconds = TimeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Seconds', tag='Seconds')
TimeUnitOfMeasure.Months = TimeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Months', tag='Months')
TimeUnitOfMeasure.Hours = TimeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Hours', tag='Hours')
TimeUnitOfMeasure.Milliseconds = TimeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Milliseconds', tag='Milliseconds')
TimeUnitOfMeasure.Days = TimeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Days', tag='Days')
TimeUnitOfMeasure.Years = TimeUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Years', tag='Years')
TimeUnitOfMeasure._InitializeFacetMap(TimeUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TimeUnitOfMeasure', TimeUnitOfMeasure)
_module_typeBindings.TimeUnitOfMeasure = TimeUnitOfMeasure

# Atomic simple type: {http://walmart.com/}BrightnessUnitOfMeasure
class BrightnessUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BrightnessUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 2033, 5)
    _Documentation = None
BrightnessUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BrightnessUnitOfMeasure, enum_prefix=None)
BrightnessUnitOfMeasure.Lumen_Seconds_Per_Meter = BrightnessUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Lumen Seconds Per Meter', tag='Lumen_Seconds_Per_Meter')
BrightnessUnitOfMeasure.Lumens = BrightnessUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Lumens', tag='Lumens')
BrightnessUnitOfMeasure.Candelas_Per_Square_Meter = BrightnessUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Candelas Per Square Meter', tag='Candelas_Per_Square_Meter')
BrightnessUnitOfMeasure.Lumens_Per_Watt = BrightnessUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Lumens Per Watt', tag='Lumens_Per_Watt')
BrightnessUnitOfMeasure.Lux_Seconds = BrightnessUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Lux Seconds', tag='Lux_Seconds')
BrightnessUnitOfMeasure.Lumen_Seconds = BrightnessUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Lumen Seconds', tag='Lumen_Seconds')
BrightnessUnitOfMeasure.Candelas = BrightnessUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Candelas', tag='Candelas')
BrightnessUnitOfMeasure.Lux = BrightnessUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Lux', tag='Lux')
BrightnessUnitOfMeasure._InitializeFacetMap(BrightnessUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BrightnessUnitOfMeasure', BrightnessUnitOfMeasure)
_module_typeBindings.BrightnessUnitOfMeasure = BrightnessUnitOfMeasure

# Atomic simple type: {http://walmart.com/}FrequencyUnitOfMeasure
class FrequencyUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FrequencyUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 2045, 5)
    _Documentation = None
FrequencyUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FrequencyUnitOfMeasure, enum_prefix=None)
FrequencyUnitOfMeasure.Kilohertz = FrequencyUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Kilohertz', tag='Kilohertz')
FrequencyUnitOfMeasure.Gigahertz = FrequencyUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Gigahertz', tag='Gigahertz')
FrequencyUnitOfMeasure.Megahertz = FrequencyUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Megahertz', tag='Megahertz')
FrequencyUnitOfMeasure.Hertz = FrequencyUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Hertz', tag='Hertz')
FrequencyUnitOfMeasure._InitializeFacetMap(FrequencyUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FrequencyUnitOfMeasure', FrequencyUnitOfMeasure)
_module_typeBindings.FrequencyUnitOfMeasure = FrequencyUnitOfMeasure

# Atomic simple type: {http://walmart.com/}SpeedUnitOfMeasure
class SpeedUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpeedUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 2053, 5)
    _Documentation = None
SpeedUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SpeedUnitOfMeasure, enum_prefix=None)
SpeedUnitOfMeasure.Kilometers_Per_Hour = SpeedUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Kilometers Per Hour', tag='Kilometers_Per_Hour')
SpeedUnitOfMeasure.Meters_Per_Second_Squared = SpeedUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Meters Per Second Squared', tag='Meters_Per_Second_Squared')
SpeedUnitOfMeasure.Meters_Per_Second = SpeedUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Meters Per Second', tag='Meters_Per_Second')
SpeedUnitOfMeasure.Radian_Per_Second = SpeedUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Radian Per Second', tag='Radian_Per_Second')
SpeedUnitOfMeasure.Revolutions_Per_Minute = SpeedUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Revolutions Per Minute', tag='Revolutions_Per_Minute')
SpeedUnitOfMeasure.Feet_Per_Minute = SpeedUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Feet Per Minute', tag='Feet_Per_Minute')
SpeedUnitOfMeasure.Miles_Per_Hour = SpeedUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Miles Per Hour', tag='Miles_Per_Hour')
SpeedUnitOfMeasure._InitializeFacetMap(SpeedUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SpeedUnitOfMeasure', SpeedUnitOfMeasure)
_module_typeBindings.SpeedUnitOfMeasure = SpeedUnitOfMeasure

# Atomic simple type: {http://walmart.com/}PowerUnitOfMeasure
class PowerUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowerUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 2064, 5)
    _Documentation = None
PowerUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PowerUnitOfMeasure, enum_prefix=None)
PowerUnitOfMeasure.Horsepower = PowerUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Horsepower', tag='Horsepower')
PowerUnitOfMeasure.Joules = PowerUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Joules', tag='Joules')
PowerUnitOfMeasure.Decibels = PowerUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Decibels', tag='Decibels')
PowerUnitOfMeasure.Watts = PowerUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Watts', tag='Watts')
PowerUnitOfMeasure._InitializeFacetMap(PowerUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PowerUnitOfMeasure', PowerUnitOfMeasure)
_module_typeBindings.PowerUnitOfMeasure = PowerUnitOfMeasure

# Atomic simple type: {http://walmart.com/}DigitalCapacityUnitOfMeasure
class DigitalCapacityUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DigitalCapacityUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 2072, 5)
    _Documentation = None
DigitalCapacityUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DigitalCapacityUnitOfMeasure, enum_prefix=None)
DigitalCapacityUnitOfMeasure.Terabytes = DigitalCapacityUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Terabytes', tag='Terabytes')
DigitalCapacityUnitOfMeasure.Kibibytes = DigitalCapacityUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Kibibytes', tag='Kibibytes')
DigitalCapacityUnitOfMeasure.Mebibytes = DigitalCapacityUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Mebibytes', tag='Mebibytes')
DigitalCapacityUnitOfMeasure.Gibibytes = DigitalCapacityUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Gibibytes', tag='Gibibytes')
DigitalCapacityUnitOfMeasure.Kilobytes = DigitalCapacityUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Kilobytes', tag='Kilobytes')
DigitalCapacityUnitOfMeasure.Gigabytes = DigitalCapacityUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Gigabytes', tag='Gigabytes')
DigitalCapacityUnitOfMeasure.Tebibytes = DigitalCapacityUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Tebibytes', tag='Tebibytes')
DigitalCapacityUnitOfMeasure.Megabyte = DigitalCapacityUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Megabyte', tag='Megabyte')
DigitalCapacityUnitOfMeasure._InitializeFacetMap(DigitalCapacityUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DigitalCapacityUnitOfMeasure', DigitalCapacityUnitOfMeasure)
_module_typeBindings.DigitalCapacityUnitOfMeasure = DigitalCapacityUnitOfMeasure

# Atomic simple type: {http://walmart.com/}PPUUnitOfMeasure
class PPUUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PPUUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 2084, 5)
    _Documentation = None
PPUUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PPUUnitOfMeasure, enum_prefix=None)
PPUUnitOfMeasure.Inch = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Inch', tag='Inch')
PPUUnitOfMeasure.Kilogram = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Kilogram', tag='Kilogram')
PPUUnitOfMeasure.Each = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Each', tag='Each')
PPUUnitOfMeasure.Ounce = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Ounce', tag='Ounce')
PPUUnitOfMeasure.Centimeter = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Centimeter', tag='Centimeter')
PPUUnitOfMeasure.Per_100_Sheet = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Per 100 Sheet', tag='Per_100_Sheet')
PPUUnitOfMeasure.Pound = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Pound', tag='Pound')
PPUUnitOfMeasure.Square_Foot = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Square Foot', tag='Square_Foot')
PPUUnitOfMeasure.Milliliter = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Milliliter', tag='Milliliter')
PPUUnitOfMeasure.Cubic_Foot = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Cubic Foot', tag='Cubic_Foot')
PPUUnitOfMeasure.Pint = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Pint', tag='Pint')
PPUUnitOfMeasure.Foot = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Foot', tag='Foot')
PPUUnitOfMeasure.Gram = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Gram', tag='Gram')
PPUUnitOfMeasure.Per_100_Count = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Per 100 Count', tag='Per_100_Count')
PPUUnitOfMeasure.Quart = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Quart', tag='Quart')
PPUUnitOfMeasure.Fluid_Ounce = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Fluid Ounce', tag='Fluid_Ounce')
PPUUnitOfMeasure.Gallon = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Gallon', tag='Gallon')
PPUUnitOfMeasure.Liter = PPUUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Liter', tag='Liter')
PPUUnitOfMeasure._InitializeFacetMap(PPUUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PPUUnitOfMeasure', PPUUnitOfMeasure)
_module_typeBindings.PPUUnitOfMeasure = PPUUnitOfMeasure

# Atomic simple type: {http://walmart.com/}TemperatureUnitOfMeasure
class TemperatureUnitOfMeasure (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemperatureUnitOfMeasure')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 2106, 5)
    _Documentation = None
TemperatureUnitOfMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TemperatureUnitOfMeasure, enum_prefix=None)
TemperatureUnitOfMeasure.Degrees_Fahrenheit = TemperatureUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Degrees Fahrenheit', tag='Degrees_Fahrenheit')
TemperatureUnitOfMeasure.Degrees_Celsius = TemperatureUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Degrees Celsius', tag='Degrees_Celsius')
TemperatureUnitOfMeasure.Degrees_Centigrade = TemperatureUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Degrees Centigrade', tag='Degrees_Centigrade')
TemperatureUnitOfMeasure.Kelvin = TemperatureUnitOfMeasure._CF_enumeration.addEnumeration(unicode_value='Kelvin', tag='Kelvin')
TemperatureUnitOfMeasure._InitializeFacetMap(TemperatureUnitOfMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TemperatureUnitOfMeasure', TemperatureUnitOfMeasure)
_module_typeBindings.TemperatureUnitOfMeasure = TemperatureUnitOfMeasure

# Complex type {http://walmart.com/}MainImage with content type ELEMENT_ONLY
class MainImage (pyxb.binding.basis.complexTypeDefinition):
    """The item's primary image. For variations, this image should coincide with each variant item in the group. E.g., for green pants, this image will show green pants. For blue pants, the image will show blue pants. 

Submit the largest, full size image you have. Recommended resolution is 3000 x 3000 pixels at 300 PPI. The minimum image size we will accept is 500 x 500 pixels at 72 PPI.

Recommended format is JPG. PNG, EPS, PSD, BMP, and TIFF are also accepted.

Recommended color mode is RGB. CMYK is also accepted. 

Do not enlarge your image if it does not meet these requirements. Doing so results in an unacceptable, degraded image."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MainImage')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 2, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}mainImageUrl uses Python identifier mainImageUrl
    __mainImageUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mainImageUrl'), 'mainImageUrl', '__httpwalmart_com_MainImage_httpwalmart_commainImageUrl', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 15, 15), )

    
    mainImageUrl = property(__mainImageUrl.value, __mainImageUrl.set, None, 'Location of the image. URLs must begin with http:// or https:// Example: http://www.walmart.com/main_image.jpg')

    
    # Element {http://walmart.com/}altText uses Python identifier altText
    __altText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'altText'), 'altText', '__httpwalmart_com_MainImage_httpwalmart_comaltText', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 28, 15), )

    
    altText = property(__altText.value, __altText.set, None, 'Alternative text of an image, video, or other asset. Use descriptive terms to describe the image.')

    _ElementMap.update({
        __mainImageUrl.name() : __mainImageUrl,
        __altText.name() : __altText
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MainImage = MainImage
Namespace.addCategoryObject('typeBinding', 'MainImage', MainImage)


# Complex type {http://walmart.com/}AdditionalAssets with content type ELEMENT_ONLY
class AdditionalAssets (pyxb.binding.basis.complexTypeDefinition):
    """Additional media (videos, rebate forms, instruction manuals, etc.) to be shown on the item page. List the assets in the order in which you wish them to appear on the site."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdditionalAssets')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 43, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}additionalAsset uses Python identifier additionalAsset
    __additionalAsset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'additionalAsset'), 'additionalAsset', '__httpwalmart_com_AdditionalAssets_httpwalmart_comadditionalAsset', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 48, 15), )

    
    additionalAsset = property(__additionalAsset.value, __additionalAsset.set, None, None)

    _ElementMap.update({
        __additionalAsset.name() : __additionalAsset
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdditionalAssets = AdditionalAssets
Namespace.addCategoryObject('typeBinding', 'AdditionalAssets', AdditionalAssets)


# Complex type {http://walmart.com/}ProductIdentifiers with content type ELEMENT_ONLY
class ProductIdentifiers (pyxb.binding.basis.complexTypeDefinition):
    """Specify at least one Product ID and its ID Type."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductIdentifiers')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 51, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}productIdentifier uses Python identifier productIdentifier
    __productIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productIdentifier'), 'productIdentifier', '__httpwalmart_com_ProductIdentifiers_httpwalmart_comproductIdentifier', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 56, 15), )

    
    productIdentifier = property(__productIdentifier.value, __productIdentifier.set, None, None)

    _ElementMap.update({
        __productIdentifier.name() : __productIdentifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProductIdentifiers = ProductIdentifiers
Namespace.addCategoryObject('typeBinding', 'ProductIdentifiers', ProductIdentifiers)


# Complex type {http://walmart.com/}CurrencyUnit with content type ELEMENT_ONLY
class CurrencyUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}CurrencyUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 59, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_CurrencyUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 61, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_CurrencyUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 62, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CurrencyUnit = CurrencyUnit
Namespace.addCategoryObject('typeBinding', 'CurrencyUnit', CurrencyUnit)


# Complex type {http://walmart.com/}Features with content type ELEMENT_ONLY
class Features (pyxb.binding.basis.complexTypeDefinition):
    """List notable features of the item. Example: Fire-Resistant; Has Handles; Removable Cover"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Features')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 69, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}feature uses Python identifier feature
    __feature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'feature'), 'feature', '__httpwalmart_com_Features_httpwalmart_comfeature', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 74, 15), )

    
    feature = property(__feature.value, __feature.set, None, None)

    _ElementMap.update({
        __feature.name() : __feature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Features = Features
Namespace.addCategoryObject('typeBinding', 'Features', Features)


# Complex type {http://walmart.com/}CertificationsAndClaims with content type ELEMENT_ONLY
class CertificationsAndClaims (pyxb.binding.basis.complexTypeDefinition):
    """List any notable claims, certifications, or compliant standards for the item."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CertificationsAndClaims')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 83, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}certificationsAndClaim uses Python identifier certificationsAndClaim
    __certificationsAndClaim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'certificationsAndClaim'), 'certificationsAndClaim', '__httpwalmart_com_CertificationsAndClaims_httpwalmart_comcertificationsAndClaim', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 88, 15), )

    
    certificationsAndClaim = property(__certificationsAndClaim.value, __certificationsAndClaim.set, None, None)

    _ElementMap.update({
        __certificationsAndClaim.name() : __certificationsAndClaim
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CertificationsAndClaims = CertificationsAndClaims
Namespace.addCategoryObject('typeBinding', 'CertificationsAndClaims', CertificationsAndClaims)


# Complex type {http://walmart.com/}LengthUnit with content type ELEMENT_ONLY
class LengthUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}LengthUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LengthUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 91, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_LengthUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 93, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_LengthUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 94, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LengthUnit = LengthUnit
Namespace.addCategoryObject('typeBinding', 'LengthUnit', LengthUnit)


# Complex type {http://walmart.com/}WeightUnit with content type ELEMENT_ONLY
class WeightUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}WeightUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WeightUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 101, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_WeightUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 103, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_WeightUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 104, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.WeightUnit = WeightUnit
Namespace.addCategoryObject('typeBinding', 'WeightUnit', WeightUnit)


# Complex type {http://walmart.com/}SportsLeague with content type ELEMENT_ONLY
class SportsLeague (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}SportsLeague with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SportsLeague')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 111, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}sportsLeagueValue uses Python identifier sportsLeagueValue
    __sportsLeagueValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sportsLeagueValue'), 'sportsLeagueValue', '__httpwalmart_com_SportsLeague_httpwalmart_comsportsLeagueValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 113, 15), )

    
    sportsLeagueValue = property(__sportsLeagueValue.value, __sportsLeagueValue.set, None, None)

    _ElementMap.update({
        __sportsLeagueValue.name() : __sportsLeagueValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SportsLeague = SportsLeague
Namespace.addCategoryObject('typeBinding', 'SportsLeague', SportsLeague)


# Complex type {http://walmart.com/}SportsTeam with content type ELEMENT_ONLY
class SportsTeam (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}SportsTeam with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SportsTeam')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 122, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}sportsTeamValue uses Python identifier sportsTeamValue
    __sportsTeamValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sportsTeamValue'), 'sportsTeamValue', '__httpwalmart_com_SportsTeam_httpwalmart_comsportsTeamValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 124, 15), )

    
    sportsTeamValue = property(__sportsTeamValue.value, __sportsTeamValue.set, None, None)

    _ElementMap.update({
        __sportsTeamValue.name() : __sportsTeamValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SportsTeam = SportsTeam
Namespace.addCategoryObject('typeBinding', 'SportsTeam', SportsTeam)


# Complex type {http://walmart.com/}Athlete with content type ELEMENT_ONLY
class Athlete (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}Athlete with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Athlete')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 133, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}athleteValue uses Python identifier athleteValue
    __athleteValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'athleteValue'), 'athleteValue', '__httpwalmart_com_Athlete_httpwalmart_comathleteValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 135, 15), )

    
    athleteValue = property(__athleteValue.value, __athleteValue.set, None, None)

    _ElementMap.update({
        __athleteValue.name() : __athleteValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Athlete = Athlete
Namespace.addCategoryObject('typeBinding', 'Athlete', Athlete)


# Complex type {http://walmart.com/}BatteryTypeAndQuantity with content type ELEMENT_ONLY
class BatteryTypeAndQuantity (pyxb.binding.basis.complexTypeDefinition):
    """Required if Has Batteries = Y"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BatteryTypeAndQuantity')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 144, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}batteryTypeAndQuantityValue uses Python identifier batteryTypeAndQuantityValue
    __batteryTypeAndQuantityValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'batteryTypeAndQuantityValue'), 'batteryTypeAndQuantityValue', '__httpwalmart_com_BatteryTypeAndQuantity_httpwalmart_combatteryTypeAndQuantityValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 149, 15), )

    
    batteryTypeAndQuantityValue = property(__batteryTypeAndQuantityValue.value, __batteryTypeAndQuantityValue.set, None, None)

    _ElementMap.update({
        __batteryTypeAndQuantityValue.name() : __batteryTypeAndQuantityValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BatteryTypeAndQuantity = BatteryTypeAndQuantity
Namespace.addCategoryObject('typeBinding', 'BatteryTypeAndQuantity', BatteryTypeAndQuantity)


# Complex type {http://walmart.com/}PPUUnit with content type ELEMENT_ONLY
class PPUUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}PPUUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PPUUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 152, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_PPUUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 154, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_PPUUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 155, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PPUUnit = PPUUnit
Namespace.addCategoryObject('typeBinding', 'PPUUnit', PPUUnit)


# Complex type {http://walmart.com/}TemperatureUnit with content type ELEMENT_ONLY
class TemperatureUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}TemperatureUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemperatureUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 162, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_TemperatureUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 164, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_TemperatureUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 165, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TemperatureUnit = TemperatureUnit
Namespace.addCategoryObject('typeBinding', 'TemperatureUnit', TemperatureUnit)


# Complex type {http://walmart.com/}SmallPartsWarnings with content type ELEMENT_ONLY
class SmallPartsWarnings (pyxb.binding.basis.complexTypeDefinition):
    """Indicates type of choking hazard warning to show on the item page.

Code definitions:
0 - Not Applicable
1 - Any ball with a diameter of 1.75 inches (44.4mm) or less that is intended for use by children 3 years or older
2 - Any toy or game intended for children 3 years or older but less than 8 years that contains a small ball
3 - Any toy and game with small parts intended for use by children at least 3 years old but under 6 years
4 - Any latex balloon, or toy or game that contains a latex balloon
5 - Any marble intended for children 3 years or older
6 - Any toy and game intended for children at least 3 years old but less than 8 years which contains a marble Example: 0; 1; 2; 3; 4; 5; 6"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SmallPartsWarnings')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 172, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}smallPartsWarning uses Python identifier smallPartsWarning
    __smallPartsWarning = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'smallPartsWarning'), 'smallPartsWarning', '__httpwalmart_com_SmallPartsWarnings_httpwalmart_comsmallPartsWarning', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 186, 15), )

    
    smallPartsWarning = property(__smallPartsWarning.value, __smallPartsWarning.set, None, None)

    _ElementMap.update({
        __smallPartsWarning.name() : __smallPartsWarning
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SmallPartsWarnings = SmallPartsWarnings
Namespace.addCategoryObject('typeBinding', 'SmallPartsWarnings', SmallPartsWarnings)


# Complex type {http://walmart.com/}StateRestrictions with content type ELEMENT_ONLY
class StateRestrictions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}StateRestrictions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StateRestrictions')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 193, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}stateRestriction uses Python identifier stateRestriction
    __stateRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stateRestriction'), 'stateRestriction', '__httpwalmart_com_StateRestrictions_httpwalmart_comstateRestriction', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 195, 15), )

    
    stateRestriction = property(__stateRestriction.value, __stateRestriction.set, None, None)

    _ElementMap.update({
        __stateRestriction.name() : __stateRestriction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StateRestrictions = StateRestrictions
Namespace.addCategoryObject('typeBinding', 'StateRestrictions', StateRestrictions)


# Complex type {http://walmart.com/}AdditionalProductAttributes with content type ELEMENT_ONLY
class AdditionalProductAttributes (pyxb.binding.basis.complexTypeDefinition):
    """Additional product attributes not enumerated in the spec using name-value pairs."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdditionalProductAttributes')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 198, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}additionalProductAttribute uses Python identifier additionalProductAttribute
    __additionalProductAttribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'additionalProductAttribute'), 'additionalProductAttribute', '__httpwalmart_com_AdditionalProductAttributes_httpwalmart_comadditionalProductAttribute', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 203, 15), )

    
    additionalProductAttribute = property(__additionalProductAttribute.value, __additionalProductAttribute.set, None, None)

    _ElementMap.update({
        __additionalProductAttribute.name() : __additionalProductAttribute
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdditionalProductAttributes = AdditionalProductAttributes
Namespace.addCategoryObject('typeBinding', 'AdditionalProductAttributes', AdditionalProductAttributes)


# Complex type {http://walmart.com/}SwatchImages with content type ELEMENT_ONLY
class SwatchImages (pyxb.binding.basis.complexTypeDefinition):
    """Enter the swatch image location in "Swatch Image URL," and its corresponding variant attribute name in "Swatch Variant Attribute." Required for products with visual variations, like color or pattern. List the swatches in the order you recommend they appear on the site."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SwatchImages')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 206, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}swatchImage uses Python identifier swatchImage
    __swatchImage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'swatchImage'), 'swatchImage', '__httpwalmart_com_SwatchImages_httpwalmart_comswatchImage', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 211, 15), )

    
    swatchImage = property(__swatchImage.value, __swatchImage.set, None, None)

    _ElementMap.update({
        __swatchImage.name() : __swatchImage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SwatchImages = SwatchImages
Namespace.addCategoryObject('typeBinding', 'SwatchImages', SwatchImages)


# Complex type {http://walmart.com/}AccessoriesIncluded with content type ELEMENT_ONLY
class AccessoriesIncluded (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}AccessoriesIncluded with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AccessoriesIncluded')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 214, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}accessoriesIncludedValue uses Python identifier accessoriesIncludedValue
    __accessoriesIncludedValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accessoriesIncludedValue'), 'accessoriesIncludedValue', '__httpwalmart_com_AccessoriesIncluded_httpwalmart_comaccessoriesIncludedValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 216, 15), )

    
    accessoriesIncludedValue = property(__accessoriesIncludedValue.value, __accessoriesIncludedValue.set, None, None)

    _ElementMap.update({
        __accessoriesIncludedValue.name() : __accessoriesIncludedValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AccessoriesIncluded = AccessoriesIncluded
Namespace.addCategoryObject('typeBinding', 'AccessoriesIncluded', AccessoriesIncluded)


# Complex type {http://walmart.com/}VariantAttributeNames with content type ELEMENT_ONLY
class VariantAttributeNames (pyxb.binding.basis.complexTypeDefinition):
    """Designate all attributes by which the item is varying. This list may include variants that the category spec has not explicitly identified. 
Ex: If partner provides data for "Collar Size," and "Collar Size" is not in the list of valid variants, then input "Collar Size" as a value here. Example: collarSize; color; shirtSize"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VariantAttributeNames')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 225, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}variantAttributeName uses Python identifier variantAttributeName
    __variantAttributeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'variantAttributeName'), 'variantAttributeName', '__httpwalmart_com_VariantAttributeNames_httpwalmart_comvariantAttributeName', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 231, 15), )

    
    variantAttributeName = property(__variantAttributeName.value, __variantAttributeName.set, None, None)

    _ElementMap.update({
        __variantAttributeName.name() : __variantAttributeName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VariantAttributeNames = VariantAttributeNames
Namespace.addCategoryObject('typeBinding', 'VariantAttributeNames', VariantAttributeNames)


# Complex type {http://walmart.com/}Color with content type ELEMENT_ONLY
class Color (pyxb.binding.basis.complexTypeDefinition):
    """Color value as provided by the manufacturer. Example: Aqua; Burgundy; Mauve; Fuchsia"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Color')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 240, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}colorValue uses Python identifier colorValue
    __colorValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'colorValue'), 'colorValue', '__httpwalmart_com_Color_httpwalmart_comcolorValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 245, 15), )

    
    colorValue = property(__colorValue.value, __colorValue.set, None, None)

    _ElementMap.update({
        __colorValue.name() : __colorValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Color = Color
Namespace.addCategoryObject('typeBinding', 'Color', Color)


# Complex type {http://walmart.com/}Material with content type ELEMENT_ONLY
class Material (pyxb.binding.basis.complexTypeDefinition):
    """Material makeup of the item. Fabric materials should be entered using the "Fabric Content" attribute. Example: Nickel; Metal; Plastic"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Material')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 254, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}materialValue uses Python identifier materialValue
    __materialValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'materialValue'), 'materialValue', '__httpwalmart_com_Material_httpwalmart_commaterialValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 259, 15), )

    
    materialValue = property(__materialValue.value, __materialValue.set, None, None)

    _ElementMap.update({
        __materialValue.name() : __materialValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Material = Material
Namespace.addCategoryObject('typeBinding', 'Material', Material)


# Complex type {http://walmart.com/}RecommendedUses with content type ELEMENT_ONLY
class RecommendedUses (pyxb.binding.basis.complexTypeDefinition):
    """Further clarification of what is the item may be used for. Example: Television; Home Audio; GPS"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecommendedUses')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 268, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}recommendedUse uses Python identifier recommendedUse
    __recommendedUse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recommendedUse'), 'recommendedUse', '__httpwalmart_com_RecommendedUses_httpwalmart_comrecommendedUse', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 273, 15), )

    
    recommendedUse = property(__recommendedUse.value, __recommendedUse.set, None, None)

    _ElementMap.update({
        __recommendedUse.name() : __recommendedUse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RecommendedUses = RecommendedUses
Namespace.addCategoryObject('typeBinding', 'RecommendedUses', RecommendedUses)


# Complex type {http://walmart.com/}MountType with content type ELEMENT_ONLY
class MountType (pyxb.binding.basis.complexTypeDefinition):
    """How the item is mounted, for use especially with shelves. Example: Wall Mount; Ceiling Mount"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MountType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 282, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}mountTypeValue uses Python identifier mountTypeValue
    __mountTypeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mountTypeValue'), 'mountTypeValue', '__httpwalmart_com_MountType_httpwalmart_commountTypeValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 287, 15), )

    
    mountTypeValue = property(__mountTypeValue.value, __mountTypeValue.set, None, None)

    _ElementMap.update({
        __mountTypeValue.name() : __mountTypeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MountType = MountType
Namespace.addCategoryObject('typeBinding', 'MountType', MountType)


# Complex type {http://walmart.com/}VolumeUnit with content type ELEMENT_ONLY
class VolumeUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}VolumeUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VolumeUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 296, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_VolumeUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 298, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_VolumeUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 299, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VolumeUnit = VolumeUnit
Namespace.addCategoryObject('typeBinding', 'VolumeUnit', VolumeUnit)


# Complex type {http://walmart.com/}ElectricalMeasurementUnit with content type ELEMENT_ONLY
class ElectricalMeasurementUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}ElectricalMeasurementUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ElectricalMeasurementUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 306, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_ElectricalMeasurementUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 308, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_ElectricalMeasurementUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 309, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ElectricalMeasurementUnit = ElectricalMeasurementUnit
Namespace.addCategoryObject('typeBinding', 'ElectricalMeasurementUnit', ElectricalMeasurementUnit)


# Complex type {http://walmart.com/}PowerUnit with content type ELEMENT_ONLY
class PowerUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}PowerUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowerUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 316, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_PowerUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 318, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_PowerUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 319, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PowerUnit = PowerUnit
Namespace.addCategoryObject('typeBinding', 'PowerUnit', PowerUnit)


# Complex type {http://walmart.com/}AreaUnit with content type ELEMENT_ONLY
class AreaUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}AreaUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AreaUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 326, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_AreaUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 328, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_AreaUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 329, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AreaUnit = AreaUnit
Namespace.addCategoryObject('typeBinding', 'AreaUnit', AreaUnit)


# Complex type {http://walmart.com/}Pattern with content type ELEMENT_ONLY
class Pattern (pyxb.binding.basis.complexTypeDefinition):
    """Decorative design or visual ornamentation, often with a thematic, recurring motif. Example: Floral; Plaid; Paisley"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Pattern')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 336, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}patternValue uses Python identifier patternValue
    __patternValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'patternValue'), 'patternValue', '__httpwalmart_com_Pattern_httpwalmart_compatternValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 341, 15), )

    
    patternValue = property(__patternValue.value, __patternValue.set, None, None)

    _ElementMap.update({
        __patternValue.name() : __patternValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Pattern = Pattern
Namespace.addCategoryObject('typeBinding', 'Pattern', Pattern)


# Complex type {http://walmart.com/}CompatibleSurfaces with content type ELEMENT_ONLY
class CompatibleSurfaces (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}CompatibleSurfaces with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompatibleSurfaces')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 350, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}compatibleSurface uses Python identifier compatibleSurface
    __compatibleSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'compatibleSurface'), 'compatibleSurface', '__httpwalmart_com_CompatibleSurfaces_httpwalmart_comcompatibleSurface', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 352, 15), )

    
    compatibleSurface = property(__compatibleSurface.value, __compatibleSurface.set, None, None)

    _ElementMap.update({
        __compatibleSurface.name() : __compatibleSurface
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CompatibleSurfaces = CompatibleSurfaces
Namespace.addCategoryObject('typeBinding', 'CompatibleSurfaces', CompatibleSurfaces)


# Complex type {http://walmart.com/}TimeUnit with content type ELEMENT_ONLY
class TimeUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}TimeUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 361, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_TimeUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 363, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_TimeUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 364, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TimeUnit = TimeUnit
Namespace.addCategoryObject('typeBinding', 'TimeUnit', TimeUnit)


# Complex type {http://walmart.com/}RecycledMaterialContent with content type ELEMENT_ONLY
class RecycledMaterialContent (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}RecycledMaterialContent with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecycledMaterialContent')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 371, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}recycledMaterialContentValue uses Python identifier recycledMaterialContentValue
    __recycledMaterialContentValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recycledMaterialContentValue'), 'recycledMaterialContentValue', '__httpwalmart_com_RecycledMaterialContent_httpwalmart_comrecycledMaterialContentValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 373, 15), )

    
    recycledMaterialContentValue = property(__recycledMaterialContentValue.value, __recycledMaterialContentValue.set, None, None)

    _ElementMap.update({
        __recycledMaterialContentValue.name() : __recycledMaterialContentValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RecycledMaterialContent = RecycledMaterialContent
Namespace.addCategoryObject('typeBinding', 'RecycledMaterialContent', RecycledMaterialContent)


# Complex type {http://walmart.com/}RecommendedSurfaces with content type ELEMENT_ONLY
class RecommendedSurfaces (pyxb.binding.basis.complexTypeDefinition):
    """ Example: Wood; Concrete; Vinyl"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecommendedSurfaces')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 376, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}recommendedSurface uses Python identifier recommendedSurface
    __recommendedSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recommendedSurface'), 'recommendedSurface', '__httpwalmart_com_RecommendedSurfaces_httpwalmart_comrecommendedSurface', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 381, 15), )

    
    recommendedSurface = property(__recommendedSurface.value, __recommendedSurface.set, None, None)

    _ElementMap.update({
        __recommendedSurface.name() : __recommendedSurface
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RecommendedSurfaces = RecommendedSurfaces
Namespace.addCategoryObject('typeBinding', 'RecommendedSurfaces', RecommendedSurfaces)


# Complex type {http://walmart.com/}PressureUnit with content type ELEMENT_ONLY
class PressureUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}PressureUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PressureUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 390, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_PressureUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 392, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_PressureUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 393, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PressureUnit = PressureUnit
Namespace.addCategoryObject('typeBinding', 'PressureUnit', PressureUnit)


# Complex type {http://walmart.com/}PercentageUnit with content type ELEMENT_ONLY
class PercentageUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}PercentageUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentageUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 400, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_PercentageUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 402, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_PercentageUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 403, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PercentageUnit = PercentageUnit
Namespace.addCategoryObject('typeBinding', 'PercentageUnit', PercentageUnit)


# Complex type {http://walmart.com/}ActiveIngredients with content type ELEMENT_ONLY
class ActiveIngredients (pyxb.binding.basis.complexTypeDefinition):
    """The list of active ingredients in order of potency, as shown on the item label."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActiveIngredients')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 410, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}activeIngredient uses Python identifier activeIngredient
    __activeIngredient = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activeIngredient'), 'activeIngredient', '__httpwalmart_com_ActiveIngredients_httpwalmart_comactiveIngredient', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 415, 15), )

    
    activeIngredient = property(__activeIngredient.value, __activeIngredient.set, None, None)

    _ElementMap.update({
        __activeIngredient.name() : __activeIngredient
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ActiveIngredients = ActiveIngredients
Namespace.addCategoryObject('typeBinding', 'ActiveIngredients', ActiveIngredients)


# Complex type {http://walmart.com/}InactiveIngredients with content type ELEMENT_ONLY
class InactiveIngredients (pyxb.binding.basis.complexTypeDefinition):
    """The list of inactive ingredients in order of potency, as shown on the item label."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InactiveIngredients')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 418, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}inactiveIngredient uses Python identifier inactiveIngredient
    __inactiveIngredient = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inactiveIngredient'), 'inactiveIngredient', '__httpwalmart_com_InactiveIngredients_httpwalmart_cominactiveIngredient', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 423, 15), )

    
    inactiveIngredient = property(__inactiveIngredient.value, __inactiveIngredient.set, None, None)

    _ElementMap.update({
        __inactiveIngredient.name() : __inactiveIngredient
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InactiveIngredients = InactiveIngredients
Namespace.addCategoryObject('typeBinding', 'InactiveIngredients', InactiveIngredients)


# Complex type {http://walmart.com/}SpeedUnit with content type ELEMENT_ONLY
class SpeedUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}SpeedUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpeedUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 432, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_SpeedUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 434, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_SpeedUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 435, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SpeedUnit = SpeedUnit
Namespace.addCategoryObject('typeBinding', 'SpeedUnit', SpeedUnit)


# Complex type {http://walmart.com/}Character with content type ELEMENT_ONLY
class Character (pyxb.binding.basis.complexTypeDefinition):
    """A person or entity portrayed in print or visual media. A character might be a fictional personality or an actual living person. Example: Dora the Explorer; SpongeBob SquarePants"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Character')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 442, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}characterValue uses Python identifier characterValue
    __characterValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'characterValue'), 'characterValue', '__httpwalmart_com_Character_httpwalmart_comcharacterValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 447, 15), )

    
    characterValue = property(__characterValue.value, __characterValue.set, None, None)

    _ElementMap.update({
        __characterValue.name() : __characterValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Character = Character
Namespace.addCategoryObject('typeBinding', 'Character', Character)


# Complex type {http://walmart.com/}AngleUnit with content type ELEMENT_ONLY
class AngleUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}AngleUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AngleUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 456, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_AngleUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 458, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_AngleUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 459, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AngleUnit = AngleUnit
Namespace.addCategoryObject('typeBinding', 'AngleUnit', AngleUnit)


# Complex type {http://walmart.com/}BrightnessUnit with content type ELEMENT_ONLY
class BrightnessUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}BrightnessUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BrightnessUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 466, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_BrightnessUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 468, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_BrightnessUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 469, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BrightnessUnit = BrightnessUnit
Namespace.addCategoryObject('typeBinding', 'BrightnessUnit', BrightnessUnit)


# Complex type {http://walmart.com/}FabricContent with content type ELEMENT_ONLY
class FabricContent (pyxb.binding.basis.complexTypeDefinition):
    """Material makeup of the item."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FabricContent')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 476, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}fabricContentValue uses Python identifier fabricContentValue
    __fabricContentValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fabricContentValue'), 'fabricContentValue', '__httpwalmart_com_FabricContent_httpwalmart_comfabricContentValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 481, 15), )

    
    fabricContentValue = property(__fabricContentValue.value, __fabricContentValue.set, None, None)

    _ElementMap.update({
        __fabricContentValue.name() : __fabricContentValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FabricContent = FabricContent
Namespace.addCategoryObject('typeBinding', 'FabricContent', FabricContent)


# Complex type {http://walmart.com/}FabricCareInstructions with content type ELEMENT_ONLY
class FabricCareInstructions (pyxb.binding.basis.complexTypeDefinition):
    """Enter details of the fabric care label. Example: Dry Clean Only; Machine Washable; Hand Wash"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FabricCareInstructions')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 484, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}fabricCareInstruction uses Python identifier fabricCareInstruction
    __fabricCareInstruction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fabricCareInstruction'), 'fabricCareInstruction', '__httpwalmart_com_FabricCareInstructions_httpwalmart_comfabricCareInstruction', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 489, 15), )

    
    fabricCareInstruction = property(__fabricCareInstruction.value, __fabricCareInstruction.set, None, None)

    _ElementMap.update({
        __fabricCareInstruction.name() : __fabricCareInstruction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FabricCareInstructions = FabricCareInstructions
Namespace.addCategoryObject('typeBinding', 'FabricCareInstructions', FabricCareInstructions)


# Complex type {http://walmart.com/}Theme with content type ELEMENT_ONLY
class Theme (pyxb.binding.basis.complexTypeDefinition):
    """A dominant idea carried in an artwork or piece of furniture Example: Animals  Insects; Automobiles; Space; Baseball; Princesses;"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Theme')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 498, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}themeValue uses Python identifier themeValue
    __themeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'themeValue'), 'themeValue', '__httpwalmart_com_Theme_httpwalmart_comthemeValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 503, 15), )

    
    themeValue = property(__themeValue.value, __themeValue.set, None, None)

    _ElementMap.update({
        __themeValue.name() : __themeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Theme = Theme
Namespace.addCategoryObject('typeBinding', 'Theme', Theme)


# Complex type {http://walmart.com/}AgeGroup with content type ELEMENT_ONLY
class AgeGroup (pyxb.binding.basis.complexTypeDefinition):
    """General grouping of ages into commonly used demographic labels. Example: Child; Teen; Adult"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AgeGroup')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 512, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}ageGroupValue uses Python identifier ageGroupValue
    __ageGroupValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ageGroupValue'), 'ageGroupValue', '__httpwalmart_com_AgeGroup_httpwalmart_comageGroupValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 517, 15), )

    
    ageGroupValue = property(__ageGroupValue.value, __ageGroupValue.set, None, None)

    _ElementMap.update({
        __ageGroupValue.name() : __ageGroupValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AgeGroup = AgeGroup
Namespace.addCategoryObject('typeBinding', 'AgeGroup', AgeGroup)


# Complex type {http://walmart.com/}RecommendedRooms with content type ELEMENT_ONLY
class RecommendedRooms (pyxb.binding.basis.complexTypeDefinition):
    """The rooms recommended for the item's use. Example: Family Room; Home Office; Kitchen; Dining Room"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecommendedRooms')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 526, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}recommendedRoom uses Python identifier recommendedRoom
    __recommendedRoom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recommendedRoom'), 'recommendedRoom', '__httpwalmart_com_RecommendedRooms_httpwalmart_comrecommendedRoom', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 531, 15), )

    
    recommendedRoom = property(__recommendedRoom.value, __recommendedRoom.set, None, None)

    _ElementMap.update({
        __recommendedRoom.name() : __recommendedRoom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RecommendedRooms = RecommendedRooms
Namespace.addCategoryObject('typeBinding', 'RecommendedRooms', RecommendedRooms)


# Complex type {http://walmart.com/}Occasion with content type ELEMENT_ONLY
class Occasion (pyxb.binding.basis.complexTypeDefinition):
    """The particular target time, event, or holiday for the product Example: Halloween; Christmas; Wedding; Anniversary"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Occasion')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 540, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}occasionValue uses Python identifier occasionValue
    __occasionValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'occasionValue'), 'occasionValue', '__httpwalmart_com_Occasion_httpwalmart_comoccasionValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 545, 15), )

    
    occasionValue = property(__occasionValue.value, __occasionValue.set, None, None)

    _ElementMap.update({
        __occasionValue.name() : __occasionValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Occasion = Occasion
Namespace.addCategoryObject('typeBinding', 'Occasion', Occasion)


# Complex type {http://walmart.com/}FillMaterial with content type ELEMENT_ONLY
class FillMaterial (pyxb.binding.basis.complexTypeDefinition):
    """The stuffing material of the item, as for cushions or plush toys. Example: Down; Polyester"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FillMaterial')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 554, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}fillMaterialValue uses Python identifier fillMaterialValue
    __fillMaterialValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fillMaterialValue'), 'fillMaterialValue', '__httpwalmart_com_FillMaterial_httpwalmart_comfillMaterialValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 559, 15), )

    
    fillMaterialValue = property(__fillMaterialValue.value, __fillMaterialValue.set, None, None)

    _ElementMap.update({
        __fillMaterialValue.name() : __fillMaterialValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FillMaterial = FillMaterial
Namespace.addCategoryObject('typeBinding', 'FillMaterial', FillMaterial)


# Complex type {http://walmart.com/}HolidayLightingStyle with content type ELEMENT_ONLY
class HolidayLightingStyle (pyxb.binding.basis.complexTypeDefinition):
    """ Example: Blinking Lights; String Lights"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HolidayLightingStyle')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 568, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}holidayLightingStyleValue uses Python identifier holidayLightingStyleValue
    __holidayLightingStyleValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'holidayLightingStyleValue'), 'holidayLightingStyleValue', '__httpwalmart_com_HolidayLightingStyle_httpwalmart_comholidayLightingStyleValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 573, 15), )

    
    holidayLightingStyleValue = property(__holidayLightingStyleValue.value, __holidayLightingStyleValue.set, None, None)

    _ElementMap.update({
        __holidayLightingStyleValue.name() : __holidayLightingStyleValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HolidayLightingStyle = HolidayLightingStyle
Namespace.addCategoryObject('typeBinding', 'HolidayLightingStyle', HolidayLightingStyle)


# Complex type {http://walmart.com/}TargetAudience with content type ELEMENT_ONLY
class TargetAudience (pyxb.binding.basis.complexTypeDefinition):
    """The demographic for which the item is targeted. Example: Family; Parties; Kids"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TargetAudience')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 582, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}targetAudienceValue uses Python identifier targetAudienceValue
    __targetAudienceValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'targetAudienceValue'), 'targetAudienceValue', '__httpwalmart_com_TargetAudience_httpwalmart_comtargetAudienceValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 587, 15), )

    
    targetAudienceValue = property(__targetAudienceValue.value, __targetAudienceValue.set, None, None)

    _ElementMap.update({
        __targetAudienceValue.name() : __targetAudienceValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TargetAudience = TargetAudience
Namespace.addCategoryObject('typeBinding', 'TargetAudience', TargetAudience)


# Complex type {http://walmart.com/}HairLength with content type ELEMENT_ONLY
class HairLength (pyxb.binding.basis.complexTypeDefinition):
    """The length of hair that grooming product is intended for. Example: Short; Medium; Long"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HairLength')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 596, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}hairLengthValue uses Python identifier hairLengthValue
    __hairLengthValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hairLengthValue'), 'hairLengthValue', '__httpwalmart_com_HairLength_httpwalmart_comhairLengthValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 601, 15), )

    
    hairLengthValue = property(__hairLengthValue.value, __hairLengthValue.set, None, None)

    _ElementMap.update({
        __hairLengthValue.name() : __hairLengthValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HairLength = HairLength
Namespace.addCategoryObject('typeBinding', 'HairLength', HairLength)


# Complex type {http://walmart.com/}StopUseIndications with content type ELEMENT_ONLY
class StopUseIndications (pyxb.binding.basis.complexTypeDefinition):
    """ Example: Stop using immediately if you experience severe burning, itching..."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StopUseIndications')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 610, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}stopUseIndication uses Python identifier stopUseIndication
    __stopUseIndication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stopUseIndication'), 'stopUseIndication', '__httpwalmart_com_StopUseIndications_httpwalmart_comstopUseIndication', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 615, 15), )

    
    stopUseIndication = property(__stopUseIndication.value, __stopUseIndication.set, None, None)

    _ElementMap.update({
        __stopUseIndication.name() : __stopUseIndication
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StopUseIndications = StopUseIndications
Namespace.addCategoryObject('typeBinding', 'StopUseIndications', StopUseIndications)


# Complex type {http://walmart.com/}NutrientContentClaims with content type ELEMENT_ONLY
class NutrientContentClaims (pyxb.binding.basis.complexTypeDefinition):
    """A claim on a food item that directly or by implication characterizes the level of a nutrient in the food. Example: Low Fat; Sugar-Free; Fat-Free; Gluten-Free; Kosher; Natural; Alcohol-Free; Contains No Milk Products; Vegan; High in Oat Bran; 100 Calories"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NutrientContentClaims')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 624, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}nutrientContentClaim uses Python identifier nutrientContentClaim
    __nutrientContentClaim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nutrientContentClaim'), 'nutrientContentClaim', '__httpwalmart_com_NutrientContentClaims_httpwalmart_comnutrientContentClaim', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 629, 15), )

    
    nutrientContentClaim = property(__nutrientContentClaim.value, __nutrientContentClaim.set, None, None)

    _ElementMap.update({
        __nutrientContentClaim.name() : __nutrientContentClaim
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NutrientContentClaims = NutrientContentClaims
Namespace.addCategoryObject('typeBinding', 'NutrientContentClaims', NutrientContentClaims)


# Complex type {http://walmart.com/}Sport with content type ELEMENT_ONLY
class Sport (pyxb.binding.basis.complexTypeDefinition):
    """If the game is sports-related, please provide the specific sport. Example: Hiking; Wrestling; Olympic Sports; Cycling; Surfing; Basketball; Baseball; Rowing; Dance  Fitness"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Sport')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 638, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}sportValue uses Python identifier sportValue
    __sportValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sportValue'), 'sportValue', '__httpwalmart_com_Sport_httpwalmart_comsportValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 643, 15), )

    
    sportValue = property(__sportValue.value, __sportValue.set, None, None)

    _ElementMap.update({
        __sportValue.name() : __sportValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Sport = Sport
Namespace.addCategoryObject('typeBinding', 'Sport', Sport)


# Complex type {http://walmart.com/}DiaposableBabyDiaperType with content type ELEMENT_ONLY
class DiaposableBabyDiaperType (pyxb.binding.basis.complexTypeDefinition):
    """Type of disposable diaper Example: Pull-up; Swim"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DiaposableBabyDiaperType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 652, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}diaposableBabyDiaperTypeValue uses Python identifier diaposableBabyDiaperTypeValue
    __diaposableBabyDiaperTypeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'diaposableBabyDiaperTypeValue'), 'diaposableBabyDiaperTypeValue', '__httpwalmart_com_DiaposableBabyDiaperType_httpwalmart_comdiaposableBabyDiaperTypeValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 657, 15), )

    
    diaposableBabyDiaperTypeValue = property(__diaposableBabyDiaperTypeValue.value, __diaposableBabyDiaperTypeValue.set, None, None)

    _ElementMap.update({
        __diaposableBabyDiaperTypeValue.name() : __diaposableBabyDiaperTypeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DiaposableBabyDiaperType = DiaposableBabyDiaperType
Namespace.addCategoryObject('typeBinding', 'DiaposableBabyDiaperType', DiaposableBabyDiaperType)


# Complex type {http://walmart.com/}OrganicCertifications with content type ELEMENT_ONLY
class OrganicCertifications (pyxb.binding.basis.complexTypeDefinition):
    """Indicates that the item is certified organic by designating the certifying agent. Example: EU Organic; Global Organic Textile Standard (GOTS); Oregon Tilth Certified Organic (OTCO); California Certified Organic; Farmers (CCOF); USDA Organic; Ecocert; Farm Verified Organic (FVO); OCIA-Certified Organic; QIA Organic; Canadian Organic Standards (COS)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrganicCertifications')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 666, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}organicCertification uses Python identifier organicCertification
    __organicCertification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'organicCertification'), 'organicCertification', '__httpwalmart_com_OrganicCertifications_httpwalmart_comorganicCertification', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 671, 15), )

    
    organicCertification = property(__organicCertification.value, __organicCertification.set, None, None)

    _ElementMap.update({
        __organicCertification.name() : __organicCertification
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrganicCertifications = OrganicCertifications
Namespace.addCategoryObject('typeBinding', 'OrganicCertifications', OrganicCertifications)


# Complex type {http://walmart.com/}Season with content type ELEMENT_ONLY
class Season (pyxb.binding.basis.complexTypeDefinition):
    """ Example: Spring; Summer; Fall; Winter; All-Season"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Season')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 680, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}seasonValue uses Python identifier seasonValue
    __seasonValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'seasonValue'), 'seasonValue', '__httpwalmart_com_Season_httpwalmart_comseasonValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 685, 15), )

    
    seasonValue = property(__seasonValue.value, __seasonValue.set, None, None)

    _ElementMap.update({
        __seasonValue.name() : __seasonValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Season = Season
Namespace.addCategoryObject('typeBinding', 'Season', Season)


# Complex type {http://walmart.com/}AwardsWon with content type ELEMENT_ONLY
class AwardsWon (pyxb.binding.basis.complexTypeDefinition):
    """ Example: Oppenheim Toy Portfolio Best Toy Award"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AwardsWon')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 694, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}awardsWonValue uses Python identifier awardsWonValue
    __awardsWonValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'awardsWonValue'), 'awardsWonValue', '__httpwalmart_com_AwardsWon_httpwalmart_comawardsWonValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 699, 15), )

    
    awardsWonValue = property(__awardsWonValue.value, __awardsWonValue.set, None, None)

    _ElementMap.update({
        __awardsWonValue.name() : __awardsWonValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AwardsWon = AwardsWon
Namespace.addCategoryObject('typeBinding', 'AwardsWon', AwardsWon)


# Complex type {http://walmart.com/}EducationalFocus with content type ELEMENT_ONLY
class EducationalFocus (pyxb.binding.basis.complexTypeDefinition):
    """ Example: Shape Identification; Language; Motor Skills; Pretend Play; Color Identification; Science; Nature; Math; Counting; Music; Reading; Writing; Creativity"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EducationalFocus')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 708, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}educationalFocu uses Python identifier educationalFocu
    __educationalFocu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'educationalFocu'), 'educationalFocu', '__httpwalmart_com_EducationalFocus_httpwalmart_comeducationalFocu', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 713, 15), )

    
    educationalFocu = property(__educationalFocu.value, __educationalFocu.set, None, None)

    _ElementMap.update({
        __educationalFocu.name() : __educationalFocu
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EducationalFocus = EducationalFocus
Namespace.addCategoryObject('typeBinding', 'EducationalFocus', EducationalFocus)


# Complex type {http://walmart.com/}Nutrients with content type ELEMENT_ONLY
class Nutrients (pyxb.binding.basis.complexTypeDefinition):
    """Additional nutrients, not including total fat or total carbohydrates, which should be entered in "Total Fat" and "Total Carbohydrate" respectively."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Nutrients')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 722, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}nutrient uses Python identifier nutrient
    __nutrient = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nutrient'), 'nutrient', '__httpwalmart_com_Nutrients_httpwalmart_comnutrient', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 727, 15), )

    
    nutrient = property(__nutrient.value, __nutrient.set, None, None)

    _ElementMap.update({
        __nutrient.name() : __nutrient
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Nutrients = Nutrients
Namespace.addCategoryObject('typeBinding', 'Nutrients', Nutrients)


# Complex type {http://walmart.com/}RecommendedLocations with content type ELEMENT_ONLY
class RecommendedLocations (pyxb.binding.basis.complexTypeDefinition):
    """The primary location recommended for the item's use. Example: Indoor; Outdoor; Vehicle"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecommendedLocations')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 730, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}recommendedLocation uses Python identifier recommendedLocation
    __recommendedLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recommendedLocation'), 'recommendedLocation', '__httpwalmart_com_RecommendedLocations_httpwalmart_comrecommendedLocation', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 735, 15), )

    
    recommendedLocation = property(__recommendedLocation.value, __recommendedLocation.set, None, None)

    _ElementMap.update({
        __recommendedLocation.name() : __recommendedLocation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RecommendedLocations = RecommendedLocations
Namespace.addCategoryObject('typeBinding', 'RecommendedLocations', RecommendedLocations)


# Complex type {http://walmart.com/}FrameMaterial with content type ELEMENT_ONLY
class FrameMaterial (pyxb.binding.basis.complexTypeDefinition):
    """The material used in the item's frame if different than its main material makeup, which is described using the "Material" attribute. Example: Metal; Plastic; Rubber; Titanium; Wood"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FrameMaterial')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 744, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}frameMaterialValue uses Python identifier frameMaterialValue
    __frameMaterialValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'frameMaterialValue'), 'frameMaterialValue', '__httpwalmart_com_FrameMaterial_httpwalmart_comframeMaterialValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 749, 15), )

    
    frameMaterialValue = property(__frameMaterialValue.value, __frameMaterialValue.set, None, None)

    _ElementMap.update({
        __frameMaterialValue.name() : __frameMaterialValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FrameMaterial = FrameMaterial
Namespace.addCategoryObject('typeBinding', 'FrameMaterial', FrameMaterial)


# Complex type {http://walmart.com/}Connections with content type ELEMENT_ONLY
class Connections (pyxb.binding.basis.complexTypeDefinition):
    """The standardized connections provided on the item. Example: HDMI; S-Video; RCA"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Connections')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 758, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}connection uses Python identifier connection
    __connection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'connection'), 'connection', '__httpwalmart_com_Connections_httpwalmart_comconnection', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 763, 15), )

    
    connection = property(__connection.value, __connection.set, None, None)

    _ElementMap.update({
        __connection.name() : __connection
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Connections = Connections
Namespace.addCategoryObject('typeBinding', 'Connections', Connections)


# Complex type {http://walmart.com/}AudioFeatures with content type ELEMENT_ONLY
class AudioFeatures (pyxb.binding.basis.complexTypeDefinition):
    """ Example: Noise-Canceling; High-Fidelity; Surround Sound; Stereo; Mono"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AudioFeatures')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 772, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}audioFeature uses Python identifier audioFeature
    __audioFeature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'audioFeature'), 'audioFeature', '__httpwalmart_com_AudioFeatures_httpwalmart_comaudioFeature', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 777, 15), )

    
    audioFeature = property(__audioFeature.value, __audioFeature.set, None, None)

    _ElementMap.update({
        __audioFeature.name() : __audioFeature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AudioFeatures = AudioFeatures
Namespace.addCategoryObject('typeBinding', 'AudioFeatures', AudioFeatures)


# Complex type {http://walmart.com/}MobileOperatingSystem with content type ELEMENT_ONLY
class MobileOperatingSystem (pyxb.binding.basis.complexTypeDefinition):
    """The operating system loaded on the device or upon which the software is designed to operate. Example: Android; iOS; Windows Phone; Symbian; CyanogenMod"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MobileOperatingSystem')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 786, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}mobileOperatingSystemValue uses Python identifier mobileOperatingSystemValue
    __mobileOperatingSystemValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mobileOperatingSystemValue'), 'mobileOperatingSystemValue', '__httpwalmart_com_MobileOperatingSystem_httpwalmart_commobileOperatingSystemValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 791, 15), )

    
    mobileOperatingSystemValue = property(__mobileOperatingSystemValue.value, __mobileOperatingSystemValue.set, None, None)

    _ElementMap.update({
        __mobileOperatingSystemValue.name() : __mobileOperatingSystemValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MobileOperatingSystem = MobileOperatingSystem
Namespace.addCategoryObject('typeBinding', 'MobileOperatingSystem', MobileOperatingSystem)


# Complex type {http://walmart.com/}ResolutionUnit with content type ELEMENT_ONLY
class ResolutionUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}ResolutionUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResolutionUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 800, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_ResolutionUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 802, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_ResolutionUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 803, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ResolutionUnit = ResolutionUnit
Namespace.addCategoryObject('typeBinding', 'ResolutionUnit', ResolutionUnit)


# Complex type {http://walmart.com/}DigitalCapacityUnit with content type ELEMENT_ONLY
class DigitalCapacityUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}DigitalCapacityUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DigitalCapacityUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 810, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_DigitalCapacityUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 812, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_DigitalCapacityUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 813, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DigitalCapacityUnit = DigitalCapacityUnit
Namespace.addCategoryObject('typeBinding', 'DigitalCapacityUnit', DigitalCapacityUnit)


# Complex type {http://walmart.com/}FrequencyUnit with content type ELEMENT_ONLY
class FrequencyUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}FrequencyUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FrequencyUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 820, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_FrequencyUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 822, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_FrequencyUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 823, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FrequencyUnit = FrequencyUnit
Namespace.addCategoryObject('typeBinding', 'FrequencyUnit', FrequencyUnit)


# Complex type {http://walmart.com/}ProcessorType with content type ELEMENT_ONLY
class ProcessorType (pyxb.binding.basis.complexTypeDefinition):
    """Commonly used retail name for the central processing unit. Example: Celeron; Intel Core i7; Snapdragon; ARM Cortex A7"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessorType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 830, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}processorTypeValue uses Python identifier processorTypeValue
    __processorTypeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'processorTypeValue'), 'processorTypeValue', '__httpwalmart_com_ProcessorType_httpwalmart_comprocessorTypeValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 835, 15), )

    
    processorTypeValue = property(__processorTypeValue.value, __processorTypeValue.set, None, None)

    _ElementMap.update({
        __processorTypeValue.name() : __processorTypeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProcessorType = ProcessorType
Namespace.addCategoryObject('typeBinding', 'ProcessorType', ProcessorType)


# Complex type {http://walmart.com/}WirelessTechnologies with content type ELEMENT_ONLY
class WirelessTechnologies (pyxb.binding.basis.complexTypeDefinition):
    """Any wireless communications standard used within or by the item. Example: Bluetooth; 802.11a; 5.8 GHz; 802.11g; 900 Mhz; Wi-Fi; 2.4GHz; None; 802.11b; 802.11n"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WirelessTechnologies')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 844, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}wirelessTechnology uses Python identifier wirelessTechnology
    __wirelessTechnology = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wirelessTechnology'), 'wirelessTechnology', '__httpwalmart_com_WirelessTechnologies_httpwalmart_comwirelessTechnology', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 849, 15), )

    
    wirelessTechnology = property(__wirelessTechnology.value, __wirelessTechnology.set, None, None)

    _ElementMap.update({
        __wirelessTechnology.name() : __wirelessTechnology
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.WirelessTechnologies = WirelessTechnologies
Namespace.addCategoryObject('typeBinding', 'WirelessTechnologies', WirelessTechnologies)


# Complex type {http://walmart.com/}TelevisionType with content type ELEMENT_ONLY
class TelevisionType (pyxb.binding.basis.complexTypeDefinition):
    """The type of TV with reference to its technology and capabilities. Example: Plasma TV; OLED TV; LCD TV; DLP TV; LED TV; CRT TV; Curved TV; Smart TV; 3D TV; Outdoor TV; TV/DVD Combo"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TelevisionType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 858, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}televisionTypeValue uses Python identifier televisionTypeValue
    __televisionTypeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'televisionTypeValue'), 'televisionTypeValue', '__httpwalmart_com_TelevisionType_httpwalmart_comtelevisionTypeValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 863, 15), )

    
    televisionTypeValue = property(__televisionTypeValue.value, __televisionTypeValue.set, None, None)

    _ElementMap.update({
        __televisionTypeValue.name() : __televisionTypeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TelevisionType = TelevisionType
Namespace.addCategoryObject('typeBinding', 'TelevisionType', TelevisionType)


# Complex type {http://walmart.com/}InputsAndOutputs with content type ELEMENT_ONLY
class InputsAndOutputs (pyxb.binding.basis.complexTypeDefinition):
    """Delimited list of the number and type of each connection on the item."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InputsAndOutputs')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 872, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}inputsAndOutput uses Python identifier inputsAndOutput
    __inputsAndOutput = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inputsAndOutput'), 'inputsAndOutput', '__httpwalmart_com_InputsAndOutputs_httpwalmart_cominputsAndOutput', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 877, 15), )

    
    inputsAndOutput = property(__inputsAndOutput.value, __inputsAndOutput.set, None, None)

    _ElementMap.update({
        __inputsAndOutput.name() : __inputsAndOutput
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InputsAndOutputs = InputsAndOutputs
Namespace.addCategoryObject('typeBinding', 'InputsAndOutputs', InputsAndOutputs)


# Complex type {http://walmart.com/}CompatibleDevices with content type ELEMENT_ONLY
class CompatibleDevices (pyxb.binding.basis.complexTypeDefinition):
    """A list of the devices compatible with the item. Example: iPad; Tablet Computers; CD Players; GPS; Desktop Computers; Blu-ray players; DVD Players"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompatibleDevices')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 880, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}compatibleDevice uses Python identifier compatibleDevice
    __compatibleDevice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'compatibleDevice'), 'compatibleDevice', '__httpwalmart_com_CompatibleDevices_httpwalmart_comcompatibleDevice', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 885, 15), )

    
    compatibleDevice = property(__compatibleDevice.value, __compatibleDevice.set, None, None)

    _ElementMap.update({
        __compatibleDevice.name() : __compatibleDevice
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CompatibleDevices = CompatibleDevices
Namespace.addCategoryObject('typeBinding', 'CompatibleDevices', CompatibleDevices)


# Complex type {http://walmart.com/}SoftwareCategory with content type ELEMENT_ONLY
class SoftwareCategory (pyxb.binding.basis.complexTypeDefinition):
    """The general category of software by which the item is most closely associated. Example: Antivirus  Security; Web  Desktop Publishing; Drivers  Utilities; Maps; Personal Finance, Tax  Legal; Productivity; Business  Office; Operating Systems; Image, Video  Audio; Servers, Development  DBMS; Hobbies  Leisure; Mobile Phone; Education, Language,  Reference; Voice Recognition"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoftwareCategory')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 894, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}softwareCategoryValue uses Python identifier softwareCategoryValue
    __softwareCategoryValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'softwareCategoryValue'), 'softwareCategoryValue', '__httpwalmart_com_SoftwareCategory_httpwalmart_comsoftwareCategoryValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 899, 15), )

    
    softwareCategoryValue = property(__softwareCategoryValue.value, __softwareCategoryValue.set, None, None)

    _ElementMap.update({
        __softwareCategoryValue.name() : __softwareCategoryValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SoftwareCategory = SoftwareCategory
Namespace.addCategoryObject('typeBinding', 'SoftwareCategory', SoftwareCategory)


# Complex type {http://walmart.com/}SystemRequirements with content type ELEMENT_ONLY
class SystemRequirements (pyxb.binding.basis.complexTypeDefinition):
    """The basic requirements necessary of any system in order to satisfactorily run the software. Example: Windows 7 or later; Intel Core 2 Duo 1.8Ghz or AMD Athlon X2 64 2.4Ghz Processor; 2GB RAM; 15GB Free Hard Drive Space"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SystemRequirements')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 908, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}systemRequirement uses Python identifier systemRequirement
    __systemRequirement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'systemRequirement'), 'systemRequirement', '__httpwalmart_com_SystemRequirements_httpwalmart_comsystemRequirement', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 913, 15), )

    
    systemRequirement = property(__systemRequirement.value, __systemRequirement.set, None, None)

    _ElementMap.update({
        __systemRequirement.name() : __systemRequirement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SystemRequirements = SystemRequirements
Namespace.addCategoryObject('typeBinding', 'SystemRequirements', SystemRequirements)


# Complex type {http://walmart.com/}OperatingSystem with content type ELEMENT_ONLY
class OperatingSystem (pyxb.binding.basis.complexTypeDefinition):
    """The operating system loaded on the device or upon which the software is designed to operate. Example: Microsoft Windows 8.1; OS X v10.8 Mountain Lion; Android KitKat"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OperatingSystem')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 922, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}operatingSystemValue uses Python identifier operatingSystemValue
    __operatingSystemValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'operatingSystemValue'), 'operatingSystemValue', '__httpwalmart_com_OperatingSystem_httpwalmart_comoperatingSystemValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 927, 15), )

    
    operatingSystemValue = property(__operatingSystemValue.value, __operatingSystemValue.set, None, None)

    _ElementMap.update({
        __operatingSystemValue.name() : __operatingSystemValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OperatingSystem = OperatingSystem
Namespace.addCategoryObject('typeBinding', 'OperatingSystem', OperatingSystem)


# Complex type {http://walmart.com/}CpuSocketType with content type ELEMENT_ONLY
class CpuSocketType (pyxb.binding.basis.complexTypeDefinition):
    """The interface of, or required by, the central processing unit. Example: AM3; LGA 1150"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CpuSocketType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 936, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}cpuSocketTypeValue uses Python identifier cpuSocketTypeValue
    __cpuSocketTypeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cpuSocketTypeValue'), 'cpuSocketTypeValue', '__httpwalmart_com_CpuSocketType_httpwalmart_comcpuSocketTypeValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 941, 15), )

    
    cpuSocketTypeValue = property(__cpuSocketTypeValue.value, __cpuSocketTypeValue.set, None, None)

    _ElementMap.update({
        __cpuSocketTypeValue.name() : __cpuSocketTypeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CpuSocketType = CpuSocketType
Namespace.addCategoryObject('typeBinding', 'CpuSocketType', CpuSocketType)


# Complex type {http://walmart.com/}MotherboardFormFactor with content type ELEMENT_ONLY
class MotherboardFormFactor (pyxb.binding.basis.complexTypeDefinition):
    """The standardized form factor with which the motherboard complies. Example: ATX; Micro ATX"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MotherboardFormFactor')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 950, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}motherboardFormFactorValue uses Python identifier motherboardFormFactorValue
    __motherboardFormFactorValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'motherboardFormFactorValue'), 'motherboardFormFactorValue', '__httpwalmart_com_MotherboardFormFactor_httpwalmart_commotherboardFormFactorValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 955, 15), )

    
    motherboardFormFactorValue = property(__motherboardFormFactorValue.value, __motherboardFormFactorValue.set, None, None)

    _ElementMap.update({
        __motherboardFormFactorValue.name() : __motherboardFormFactorValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MotherboardFormFactor = MotherboardFormFactor
Namespace.addCategoryObject('typeBinding', 'MotherboardFormFactor', MotherboardFormFactor)


# Complex type {http://walmart.com/}RecordableMediaFormats with content type ELEMENT_ONLY
class RecordableMediaFormats (pyxb.binding.basis.complexTypeDefinition):
    """The recording technologies compatible with the item. Example: DVD-R; DVD-RW; motion JPEG; Blu-Ray; MPEG-1;"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecordableMediaFormats')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 964, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}recordableMediaFormat uses Python identifier recordableMediaFormat
    __recordableMediaFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordableMediaFormat'), 'recordableMediaFormat', '__httpwalmart_com_RecordableMediaFormats_httpwalmart_comrecordableMediaFormat', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 969, 15), )

    
    recordableMediaFormat = property(__recordableMediaFormat.value, __recordableMediaFormat.set, None, None)

    _ElementMap.update({
        __recordableMediaFormat.name() : __recordableMediaFormat
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RecordableMediaFormats = RecordableMediaFormats
Namespace.addCategoryObject('typeBinding', 'RecordableMediaFormats', RecordableMediaFormats)


# Complex type {http://walmart.com/}CompatibleBrands with content type ELEMENT_ONLY
class CompatibleBrands (pyxb.binding.basis.complexTypeDefinition):
    """A list of the brands most commonly compatible with the item. Example: Toshiba; Dell; HP"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompatibleBrands')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 978, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}compatibleBrand uses Python identifier compatibleBrand
    __compatibleBrand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'compatibleBrand'), 'compatibleBrand', '__httpwalmart_com_CompatibleBrands_httpwalmart_comcompatibleBrand', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 983, 15), )

    
    compatibleBrand = property(__compatibleBrand.value, __compatibleBrand.set, None, None)

    _ElementMap.update({
        __compatibleBrand.name() : __compatibleBrand
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CompatibleBrands = CompatibleBrands
Namespace.addCategoryObject('typeBinding', 'CompatibleBrands', CompatibleBrands)


# Complex type {http://walmart.com/}HeadphoneFeatures with content type ELEMENT_ONLY
class HeadphoneFeatures (pyxb.binding.basis.complexTypeDefinition):
    """ Example: In-Ear; Over-Ear; On-Ear; Ear-Clip; Behind-the-Neck; Closed Cup; Open Cup; Microphone; Memory Foam"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HeadphoneFeatures')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 992, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}headphoneFeature uses Python identifier headphoneFeature
    __headphoneFeature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'headphoneFeature'), 'headphoneFeature', '__httpwalmart_com_HeadphoneFeatures_httpwalmart_comheadphoneFeature', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 997, 15), )

    
    headphoneFeature = property(__headphoneFeature.value, __headphoneFeature.set, None, None)

    _ElementMap.update({
        __headphoneFeature.name() : __headphoneFeature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HeadphoneFeatures = HeadphoneFeatures
Namespace.addCategoryObject('typeBinding', 'HeadphoneFeatures', HeadphoneFeatures)


# Complex type {http://walmart.com/}VolumetricFlowRateUnit with content type ELEMENT_ONLY
class VolumetricFlowRateUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}VolumetricFlowRateUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VolumetricFlowRateUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1006, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_VolumetricFlowRateUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1008, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_VolumetricFlowRateUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1009, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VolumetricFlowRateUnit = VolumetricFlowRateUnit
Namespace.addCategoryObject('typeBinding', 'VolumetricFlowRateUnit', VolumetricFlowRateUnit)


# Complex type {http://walmart.com/}OriginalLanguages with content type ELEMENT_ONLY
class OriginalLanguages (pyxb.binding.basis.complexTypeDefinition):
    """The original language of the work. Usually this will be one language, but occasionally more than one is appropriate. For example, if a movie is dubbed in English but the original language is Chinese, enter "Chinese." Example: Spanish; English; Dutch; Kurdish; Swahili; Klingon"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OriginalLanguages')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1016, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}originalLanguage uses Python identifier originalLanguage
    __originalLanguage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalLanguage'), 'originalLanguage', '__httpwalmart_com_OriginalLanguages_httpwalmart_comoriginalLanguage', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1021, 15), )

    
    originalLanguage = property(__originalLanguage.value, __originalLanguage.set, None, None)

    _ElementMap.update({
        __originalLanguage.name() : __originalLanguage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OriginalLanguages = OriginalLanguages
Namespace.addCategoryObject('typeBinding', 'OriginalLanguages', OriginalLanguages)


# Complex type {http://walmart.com/}Actors with content type ELEMENT_ONLY
class Actors (pyxb.binding.basis.complexTypeDefinition):
    """Actors who receive top billing in a movie or television show. Example: Humphrey Bogart; Julia Roberts; Brad Pitt; Marilyn Monroe"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Actors')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1030, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}actor uses Python identifier actor
    __actor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actor'), 'actor', '__httpwalmart_com_Actors_httpwalmart_comactor', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1035, 15), )

    
    actor = property(__actor.value, __actor.set, None, None)

    _ElementMap.update({
        __actor.name() : __actor
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Actors = Actors
Namespace.addCategoryObject('typeBinding', 'Actors', Actors)


# Complex type {http://walmart.com/}DubbedLanguages with content type ELEMENT_ONLY
class DubbedLanguages (pyxb.binding.basis.complexTypeDefinition):
    """Language(s) that a film has been dubbed with Example: Korean; Czech; Hindi; Spanish; German"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DubbedLanguages')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1044, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}dubbedLanguage uses Python identifier dubbedLanguage
    __dubbedLanguage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dubbedLanguage'), 'dubbedLanguage', '__httpwalmart_com_DubbedLanguages_httpwalmart_comdubbedLanguage', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1049, 15), )

    
    dubbedLanguage = property(__dubbedLanguage.value, __dubbedLanguage.set, None, None)

    _ElementMap.update({
        __dubbedLanguage.name() : __dubbedLanguage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DubbedLanguages = DubbedLanguages
Namespace.addCategoryObject('typeBinding', 'DubbedLanguages', DubbedLanguages)


# Complex type {http://walmart.com/}SubtitledLanguages with content type ELEMENT_ONLY
class SubtitledLanguages (pyxb.binding.basis.complexTypeDefinition):
    """Language(s) that a film's subtitles have been written in Example: English; Portuguese; Turkish; Russian; Thai"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubtitledLanguages')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1058, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}subtitledLanguage uses Python identifier subtitledLanguage
    __subtitledLanguage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subtitledLanguage'), 'subtitledLanguage', '__httpwalmart_com_SubtitledLanguages_httpwalmart_comsubtitledLanguage', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1063, 15), )

    
    subtitledLanguage = property(__subtitledLanguage.value, __subtitledLanguage.set, None, None)

    _ElementMap.update({
        __subtitledLanguage.name() : __subtitledLanguage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SubtitledLanguages = SubtitledLanguages
Namespace.addCategoryObject('typeBinding', 'SubtitledLanguages', SubtitledLanguages)


# Complex type {http://walmart.com/}Performer with content type ELEMENT_ONLY
class Performer (pyxb.binding.basis.complexTypeDefinition):
    """The performer/s or name of group on the album or single. Example: Beyonce; Kelly Clarkson; George Strait; Queen; The Grateful Dead; They Might Be Giants; The Boston Pops Orchestra"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Performer')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1072, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}performerValue uses Python identifier performerValue
    __performerValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'performerValue'), 'performerValue', '__httpwalmart_com_Performer_httpwalmart_comperformerValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1077, 15), )

    
    performerValue = property(__performerValue.value, __performerValue.set, None, None)

    _ElementMap.update({
        __performerValue.name() : __performerValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Performer = Performer
Namespace.addCategoryObject('typeBinding', 'Performer', Performer)


# Complex type {http://walmart.com/}TrackListings with content type ELEMENT_ONLY
class TrackListings (pyxb.binding.basis.complexTypeDefinition):
    """List each track on the album with track name, number, and duration."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrackListings')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1086, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}trackListing uses Python identifier trackListing
    __trackListing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trackListing'), 'trackListing', '__httpwalmart_com_TrackListings_httpwalmart_comtrackListing', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1091, 15), )

    
    trackListing = property(__trackListing.value, __trackListing.set, None, None)

    _ElementMap.update({
        __trackListing.name() : __trackListing
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TrackListings = TrackListings
Namespace.addCategoryObject('typeBinding', 'TrackListings', TrackListings)


# Complex type {http://walmart.com/}Author with content type ELEMENT_ONLY
class Author (pyxb.binding.basis.complexTypeDefinition):
    """The name (or pseudonym) of the person who wrote a book, as written on the cover and/or title page. Example: Dr. Seuss; William Shakespeare; Beatrix Potter"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Author')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1094, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}authorValue uses Python identifier authorValue
    __authorValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'authorValue'), 'authorValue', '__httpwalmart_com_Author_httpwalmart_comauthorValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1099, 15), )

    
    authorValue = property(__authorValue.value, __authorValue.set, None, None)

    _ElementMap.update({
        __authorValue.name() : __authorValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Author = Author
Namespace.addCategoryObject('typeBinding', 'Author', Author)


# Complex type {http://walmart.com/}InkColor with content type ELEMENT_ONLY
class InkColor (pyxb.binding.basis.complexTypeDefinition):
    """The ink color of pens, markers, ink pads, and other writing implements. Example: Black; Red; Blue"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InkColor')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1108, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}inkColorValue uses Python identifier inkColorValue
    __inkColorValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inkColorValue'), 'inkColorValue', '__httpwalmart_com_InkColor_httpwalmart_cominkColorValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1113, 15), )

    
    inkColorValue = property(__inkColorValue.value, __inkColorValue.set, None, None)

    _ElementMap.update({
        __inkColorValue.name() : __inkColorValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InkColor = InkColor
Namespace.addCategoryObject('typeBinding', 'InkColor', InkColor)


# Complex type {http://walmart.com/}PaperSize with content type ELEMENT_ONLY
class PaperSize (pyxb.binding.basis.complexTypeDefinition):
    """ Example: A1; B4"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaperSize')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1122, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}paperSizeValue uses Python identifier paperSizeValue
    __paperSizeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paperSizeValue'), 'paperSizeValue', '__httpwalmart_com_PaperSize_httpwalmart_compaperSizeValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1127, 15), )

    
    paperSizeValue = property(__paperSizeValue.value, __paperSizeValue.set, None, None)

    _ElementMap.update({
        __paperSizeValue.name() : __paperSizeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PaperSize = PaperSize
Namespace.addCategoryObject('typeBinding', 'PaperSize', PaperSize)


# Complex type {http://walmart.com/}Instrument with content type ELEMENT_ONLY
class Instrument (pyxb.binding.basis.complexTypeDefinition):
    """The name(s) of the musical instrument(s) or equipment this accessory is intended for/compatible with. Example: clarinet; guitar; trumpet; kazoo"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Instrument')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1136, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}instrumentValue uses Python identifier instrumentValue
    __instrumentValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'instrumentValue'), 'instrumentValue', '__httpwalmart_com_Instrument_httpwalmart_cominstrumentValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1141, 15), )

    
    instrumentValue = property(__instrumentValue.value, __instrumentValue.set, None, None)

    _ElementMap.update({
        __instrumentValue.name() : __instrumentValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Instrument = Instrument
Namespace.addCategoryObject('typeBinding', 'Instrument', Instrument)


# Complex type {http://walmart.com/}NumberOfPlayer with content type ELEMENT_ONLY
class NumberOfPlayer (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}NumberOfPlayer with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NumberOfPlayer')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1150, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}minimumNumberOfPlayers uses Python identifier minimumNumberOfPlayers
    __minimumNumberOfPlayers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minimumNumberOfPlayers'), 'minimumNumberOfPlayers', '__httpwalmart_com_NumberOfPlayer_httpwalmart_comminimumNumberOfPlayers', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1152, 15), )

    
    minimumNumberOfPlayers = property(__minimumNumberOfPlayers.value, __minimumNumberOfPlayers.set, None, 'The minimum number of people required to play the game. Example: 2.0')

    
    # Element {http://walmart.com/}maximumNumberOfPlayers uses Python identifier maximumNumberOfPlayers
    __maximumNumberOfPlayers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maximumNumberOfPlayers'), 'maximumNumberOfPlayers', '__httpwalmart_com_NumberOfPlayer_httpwalmart_commaximumNumberOfPlayers', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1163, 15), )

    
    maximumNumberOfPlayers = property(__maximumNumberOfPlayers.value, __maximumNumberOfPlayers.set, None, 'The maximum number of people for which the game is intended. Example: 4.0')

    _ElementMap.update({
        __minimumNumberOfPlayers.name() : __minimumNumberOfPlayers,
        __maximumNumberOfPlayers.name() : __maximumNumberOfPlayers
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NumberOfPlayer = NumberOfPlayer
Namespace.addCategoryObject('typeBinding', 'NumberOfPlayer', NumberOfPlayer)


# Complex type {http://walmart.com/}FoodAllergenStatements with content type ELEMENT_ONLY
class FoodAllergenStatements (pyxb.binding.basis.complexTypeDefinition):
    """Statement regarding any ingredients that may be food allergens. Example: Contains Peanuts, Soy, and MSG"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FoodAllergenStatements')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1176, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}foodAllergenStatement uses Python identifier foodAllergenStatement
    __foodAllergenStatement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'foodAllergenStatement'), 'foodAllergenStatement', '__httpwalmart_com_FoodAllergenStatements_httpwalmart_comfoodAllergenStatement', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1181, 15), )

    
    foodAllergenStatement = property(__foodAllergenStatement.value, __foodAllergenStatement.set, None, None)

    _ElementMap.update({
        __foodAllergenStatement.name() : __foodAllergenStatement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FoodAllergenStatements = FoodAllergenStatements
Namespace.addCategoryObject('typeBinding', 'FoodAllergenStatements', FoodAllergenStatements)


# Complex type {http://walmart.com/}MemoryCardType with content type ELEMENT_ONLY
class MemoryCardType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}MemoryCardType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MemoryCardType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1190, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}memoryCardTypeValue uses Python identifier memoryCardTypeValue
    __memoryCardTypeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'memoryCardTypeValue'), 'memoryCardTypeValue', '__httpwalmart_com_MemoryCardType_httpwalmart_commemoryCardTypeValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1192, 15), )

    
    memoryCardTypeValue = property(__memoryCardTypeValue.value, __memoryCardTypeValue.set, None, None)

    _ElementMap.update({
        __memoryCardTypeValue.name() : __memoryCardTypeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MemoryCardType = MemoryCardType
Namespace.addCategoryObject('typeBinding', 'MemoryCardType', MemoryCardType)


# Complex type {http://walmart.com/}FocusType with content type ELEMENT_ONLY
class FocusType (pyxb.binding.basis.complexTypeDefinition):
    """ Example: Auto; Center; Fixed"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FocusType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1201, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}focusTypeValue uses Python identifier focusTypeValue
    __focusTypeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'focusTypeValue'), 'focusTypeValue', '__httpwalmart_com_FocusType_httpwalmart_comfocusTypeValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1206, 15), )

    
    focusTypeValue = property(__focusTypeValue.value, __focusTypeValue.set, None, None)

    _ElementMap.update({
        __focusTypeValue.name() : __focusTypeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FocusType = FocusType
Namespace.addCategoryObject('typeBinding', 'FocusType', FocusType)


# Complex type {http://walmart.com/}ExposureModes with content type ELEMENT_ONLY
class ExposureModes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}ExposureModes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExposureModes')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1215, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}exposureMode uses Python identifier exposureMode
    __exposureMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exposureMode'), 'exposureMode', '__httpwalmart_com_ExposureModes_httpwalmart_comexposureMode', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1217, 15), )

    
    exposureMode = property(__exposureMode.value, __exposureMode.set, None, None)

    _ElementMap.update({
        __exposureMode.name() : __exposureMode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExposureModes = ExposureModes
Namespace.addCategoryObject('typeBinding', 'ExposureModes', ExposureModes)


# Complex type {http://walmart.com/}LensType with content type ELEMENT_ONLY
class LensType (pyxb.binding.basis.complexTypeDefinition):
    """Whether the lens is single, multifocal, or tinted Example: Single Vision; Bifocal; Progressive; Trifocal; Sunglasses"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LensType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1226, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}lensTypeValue uses Python identifier lensTypeValue
    __lensTypeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lensTypeValue'), 'lensTypeValue', '__httpwalmart_com_LensType_httpwalmart_comlensTypeValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1231, 15), )

    
    lensTypeValue = property(__lensTypeValue.value, __lensTypeValue.set, None, None)

    _ElementMap.update({
        __lensTypeValue.name() : __lensTypeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LensType = LensType
Namespace.addCategoryObject('typeBinding', 'LensType', LensType)


# Complex type {http://walmart.com/}HandleMaterial with content type ELEMENT_ONLY
class HandleMaterial (pyxb.binding.basis.complexTypeDefinition):
    """Material of the handle, if different from the rest of the item. Example: Leather; Imitation Leather; Fabric; Suede"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HandleMaterial')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1240, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}handleMaterialValue uses Python identifier handleMaterialValue
    __handleMaterialValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'handleMaterialValue'), 'handleMaterialValue', '__httpwalmart_com_HandleMaterial_httpwalmart_comhandleMaterialValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1245, 15), )

    
    handleMaterialValue = property(__handleMaterialValue.value, __handleMaterialValue.set, None, None)

    _ElementMap.update({
        __handleMaterialValue.name() : __handleMaterialValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HandleMaterial = HandleMaterial
Namespace.addCategoryObject('typeBinding', 'HandleMaterial', HandleMaterial)


# Complex type {http://walmart.com/}Gemstone with content type ELEMENT_ONLY
class Gemstone (pyxb.binding.basis.complexTypeDefinition):
    """ Example: Amethyst; Aquamarine; Citrine; Coral; Crystal; Cubic Zirconia; Diamond; Emerald; Garnet; Jade; Mother of Pearl; Multigemstone; Onyx; Opal; Pearl; Peridot; Quartz; Ruby; Sapphire; Tanzanite; Tiger's Eye; Topaz; Turquoise"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Gemstone')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1254, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}gemstoneValue uses Python identifier gemstoneValue
    __gemstoneValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gemstoneValue'), 'gemstoneValue', '__httpwalmart_com_Gemstone_httpwalmart_comgemstoneValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1259, 15), )

    
    gemstoneValue = property(__gemstoneValue.value, __gemstoneValue.set, None, None)

    _ElementMap.update({
        __gemstoneValue.name() : __gemstoneValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Gemstone = Gemstone
Namespace.addCategoryObject('typeBinding', 'Gemstone', Gemstone)


# Complex type {http://walmart.com/}BodyParts with content type ELEMENT_ONLY
class BodyParts (pyxb.binding.basis.complexTypeDefinition):
    """The body part/s for which the item is intended. Example: Ankle; Hand; Wrist"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BodyParts')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1268, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}bodyPart uses Python identifier bodyPart
    __bodyPart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bodyPart'), 'bodyPart', '__httpwalmart_com_BodyParts_httpwalmart_combodyPart', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1273, 15), )

    
    bodyPart = property(__bodyPart.value, __bodyPart.set, None, None)

    _ElementMap.update({
        __bodyPart.name() : __bodyPart
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BodyParts = BodyParts
Namespace.addCategoryObject('typeBinding', 'BodyParts', BodyParts)


# Complex type {http://walmart.com/}RingStyle with content type ELEMENT_ONLY
class RingStyle (pyxb.binding.basis.complexTypeDefinition):
    """Form or design of a ring Example: Cocktail; Hearts; Engagement; Stacking; Halo; Solitaire; Three-Stone; Eternity; Semi-Eternity; No Stone; Claddah; Midi"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RingStyle')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1282, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}ringStyleValue uses Python identifier ringStyleValue
    __ringStyleValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ringStyleValue'), 'ringStyleValue', '__httpwalmart_com_RingStyle_httpwalmart_comringStyleValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1287, 15), )

    
    ringStyleValue = property(__ringStyleValue.value, __ringStyleValue.set, None, None)

    _ElementMap.update({
        __ringStyleValue.name() : __ringStyleValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RingStyle = RingStyle
Namespace.addCategoryObject('typeBinding', 'RingStyle', RingStyle)


# Complex type {http://walmart.com/}WatchBandMaterial with content type ELEMENT_ONLY
class WatchBandMaterial (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}WatchBandMaterial with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WatchBandMaterial')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1296, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}watchBandMaterialValue uses Python identifier watchBandMaterialValue
    __watchBandMaterialValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'watchBandMaterialValue'), 'watchBandMaterialValue', '__httpwalmart_com_WatchBandMaterial_httpwalmart_comwatchBandMaterialValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1298, 15), )

    
    watchBandMaterialValue = property(__watchBandMaterialValue.value, __watchBandMaterialValue.set, None, None)

    _ElementMap.update({
        __watchBandMaterialValue.name() : __watchBandMaterialValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.WatchBandMaterial = WatchBandMaterial
Namespace.addCategoryObject('typeBinding', 'WatchBandMaterial', WatchBandMaterial)


# Complex type {http://walmart.com/}WatchStyle with content type ELEMENT_ONLY
class WatchStyle (pyxb.binding.basis.complexTypeDefinition):
    """Level of formality or type of dress Example: Casual; Dress; Fashion; Sport"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WatchStyle')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1307, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}watchStyleValue uses Python identifier watchStyleValue
    __watchStyleValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'watchStyleValue'), 'watchStyleValue', '__httpwalmart_com_WatchStyle_httpwalmart_comwatchStyleValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1312, 15), )

    
    watchStyleValue = property(__watchStyleValue.value, __watchStyleValue.set, None, None)

    _ElementMap.update({
        __watchStyleValue.name() : __watchStyleValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.WatchStyle = WatchStyle
Namespace.addCategoryObject('typeBinding', 'WatchStyle', WatchStyle)


# Complex type {http://walmart.com/}FuelEconomyUnit with content type ELEMENT_ONLY
class FuelEconomyUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}FuelEconomyUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FuelEconomyUnit')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1321, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwalmart_com_FuelEconomyUnit_httpwalmart_comunit', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1323, 15), )

    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Element {http://walmart.com/}measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measure'), 'measure', '__httpwalmart_com_FuelEconomyUnit_httpwalmart_commeasure', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1324, 15), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __unit.name() : __unit,
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FuelEconomyUnit = FuelEconomyUnit
Namespace.addCategoryObject('typeBinding', 'FuelEconomyUnit', FuelEconomyUnit)


# Complex type {http://walmart.com/}InterfaceType with content type ELEMENT_ONLY
class InterfaceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}InterfaceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InterfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1331, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}interfaceTypeValue uses Python identifier interfaceTypeValue
    __interfaceTypeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'interfaceTypeValue'), 'interfaceTypeValue', '__httpwalmart_com_InterfaceType_httpwalmart_cominterfaceTypeValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1333, 15), )

    
    interfaceTypeValue = property(__interfaceTypeValue.value, __interfaceTypeValue.set, None, None)

    _ElementMap.update({
        __interfaceTypeValue.name() : __interfaceTypeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InterfaceType = InterfaceType
Namespace.addCategoryObject('typeBinding', 'InterfaceType', InterfaceType)


# Complex type {http://walmart.com/}BraSize with content type ELEMENT_ONLY
class BraSize (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}BraSize with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BraSize')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1342, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}braBandSize uses Python identifier braBandSize
    __braBandSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'braBandSize'), 'braBandSize', '__httpwalmart_com_BraSize_httpwalmart_combraBandSize', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1344, 15), )

    
    braBandSize = property(__braBandSize.value, __braBandSize.set, None, 'Bra band size in inches. Example: 34 in')

    
    # Element {http://walmart.com/}braCupSize uses Python identifier braCupSize
    __braCupSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'braCupSize'), 'braCupSize', '__httpwalmart_com_BraSize_httpwalmart_combraCupSize', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1355, 15), )

    
    braCupSize = property(__braCupSize.value, __braCupSize.set, None, ' Example: A; AA; B; C; D; DD')

    _ElementMap.update({
        __braBandSize.name() : __braBandSize,
        __braCupSize.name() : __braCupSize
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BraSize = BraSize
Namespace.addCategoryObject('typeBinding', 'BraSize', BraSize)


# Complex type {http://walmart.com/}PantSize with content type ELEMENT_ONLY
class PantSize (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}PantSize with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PantSize')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1370, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}inseam uses Python identifier inseam
    __inseam = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inseam'), 'inseam', '__httpwalmart_com_PantSize_httpwalmart_cominseam', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1372, 15), )

    
    inseam = property(__inseam.value, __inseam.set, None, 'Pant inseam in inches. Example: 32 in')

    
    # Element {http://walmart.com/}waistSize uses Python identifier waistSize
    __waistSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'waistSize'), 'waistSize', '__httpwalmart_com_PantSize_httpwalmart_comwaistSize', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1383, 15), )

    
    waistSize = property(__waistSize.value, __waistSize.set, None, 'Waist size in inches. Example: 38 in')

    _ElementMap.update({
        __inseam.name() : __inseam,
        __waistSize.name() : __waistSize
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PantSize = PantSize
Namespace.addCategoryObject('typeBinding', 'PantSize', PantSize)


# Complex type {http://walmart.com/}DressShirtSize with content type ELEMENT_ONLY
class DressShirtSize (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}DressShirtSize with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DressShirtSize')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1395, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}neckSize uses Python identifier neckSize
    __neckSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'neckSize'), 'neckSize', '__httpwalmart_com_DressShirtSize_httpwalmart_comneckSize', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1397, 15), )

    
    neckSize = property(__neckSize.value, __neckSize.set, None, 'Neck size in inches. Example: 15.5 in; 16 in')

    
    # Element {http://walmart.com/}sleeveLength uses Python identifier sleeveLength
    __sleeveLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sleeveLength'), 'sleeveLength', '__httpwalmart_com_DressShirtSize_httpwalmart_comsleeveLength', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1408, 15), )

    
    sleeveLength = property(__sleeveLength.value, __sleeveLength.set, None, 'Sleeve length in inches if available for the item. Example: 34 in')

    _ElementMap.update({
        __neckSize.name() : __neckSize,
        __sleeveLength.name() : __sleeveLength
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DressShirtSize = DressShirtSize
Namespace.addCategoryObject('typeBinding', 'DressShirtSize', DressShirtSize)


# Complex type {http://walmart.com/}BallCoreMaterial with content type ELEMENT_ONLY
class BallCoreMaterial (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}BallCoreMaterial with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BallCoreMaterial')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1421, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}ballCoreMaterialValue uses Python identifier ballCoreMaterialValue
    __ballCoreMaterialValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ballCoreMaterialValue'), 'ballCoreMaterialValue', '__httpwalmart_com_BallCoreMaterial_httpwalmart_comballCoreMaterialValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1423, 15), )

    
    ballCoreMaterialValue = property(__ballCoreMaterialValue.value, __ballCoreMaterialValue.set, None, None)

    _ElementMap.update({
        __ballCoreMaterialValue.name() : __ballCoreMaterialValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BallCoreMaterial = BallCoreMaterial
Namespace.addCategoryObject('typeBinding', 'BallCoreMaterial', BallCoreMaterial)


# Complex type {http://walmart.com/}HealthConcerns with content type ELEMENT_ONLY
class HealthConcerns (pyxb.binding.basis.complexTypeDefinition):
    """ Example: Cold; Fever; Allergy; Prenatal"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HealthConcerns')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1432, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}healthConcern uses Python identifier healthConcern
    __healthConcern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'healthConcern'), 'healthConcern', '__httpwalmart_com_HealthConcerns_httpwalmart_comhealthConcern', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1437, 15), )

    
    healthConcern = property(__healthConcern.value, __healthConcern.set, None, None)

    _ElementMap.update({
        __healthConcern.name() : __healthConcern
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HealthConcerns = HealthConcerns
Namespace.addCategoryObject('typeBinding', 'HealthConcerns', HealthConcerns)


# Complex type {http://walmart.com/}IngredientClaim with content type ELEMENT_ONLY
class IngredientClaim (pyxb.binding.basis.complexTypeDefinition):
    """A claim that advertises the lack or presence of ingredients for the purpose of sellability. Example: All Natural Ingredients; Vegan; BPA-Free;"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IngredientClaim')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1446, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}ingredientClaimValue uses Python identifier ingredientClaimValue
    __ingredientClaimValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ingredientClaimValue'), 'ingredientClaimValue', '__httpwalmart_com_IngredientClaim_httpwalmart_comingredientClaimValue', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1451, 15), )

    
    ingredientClaimValue = property(__ingredientClaimValue.value, __ingredientClaimValue.set, None, None)

    _ElementMap.update({
        __ingredientClaimValue.name() : __ingredientClaimValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IngredientClaim = IngredientClaim
Namespace.addCategoryObject('typeBinding', 'IngredientClaim', IngredientClaim)


# Complex type {http://walmart.com/}additionalAsset with content type ELEMENT_ONLY
class additionalAsset (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}additionalAsset with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'additionalAsset')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1460, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}altText uses Python identifier altText
    __altText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'altText'), 'altText', '__httpwalmart_com_additionalAsset_httpwalmart_comaltText', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1462, 15), )

    
    altText = property(__altText.value, __altText.set, None, 'Alternative text of an image, video, or other asset. Use descriptive terms to describe the image.')

    
    # Element {http://walmart.com/}assetUrl uses Python identifier assetUrl
    __assetUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'assetUrl'), 'assetUrl', '__httpwalmart_com_additionalAsset_httpwalmart_comassetUrl', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1475, 15), )

    
    assetUrl = property(__assetUrl.value, __assetUrl.set, None, 'Location of the additional assets. Required if additional assets beyond the main image are provided. URLs must begin with http:// or https:// Example: http://www.walmart.com/video1.jpg')

    
    # Element {http://walmart.com/}assetType uses Python identifier assetType
    __assetType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'assetType'), 'assetType', '__httpwalmart_com_additionalAsset_httpwalmart_comassetType', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1488, 15), )

    
    assetType = property(__assetType.value, __assetType.set, None, 'Provides additional information on the assets. Example: Secondary Image; Video; Instruction Manual; Assembly Instructions; Badge; Manufacturer Logo')

    
    # Element {http://walmart.com/}additionalAssetAttributes uses Python identifier additionalAssetAttributes
    __additionalAssetAttributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'additionalAssetAttributes'), 'additionalAssetAttributes', '__httpwalmart_com_additionalAsset_httpwalmart_comadditionalAssetAttributes', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1501, 15), )

    
    additionalAssetAttributes = property(__additionalAssetAttributes.value, __additionalAssetAttributes.set, None, '')

    _ElementMap.update({
        __altText.name() : __altText,
        __assetUrl.name() : __assetUrl,
        __assetType.name() : __assetType,
        __additionalAssetAttributes.name() : __additionalAssetAttributes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.additionalAsset = additionalAsset
Namespace.addCategoryObject('typeBinding', 'additionalAsset', additionalAsset)


# Complex type {http://walmart.com/}productIdentifier with content type ELEMENT_ONLY
class productIdentifier (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}productIdentifier with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'productIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1510, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}productIdType uses Python identifier productIdType
    __productIdType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productIdType'), 'productIdType', '__httpwalmart_com_productIdentifier_httpwalmart_comproductIdType', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1512, 15), )

    
    productIdType = property(__productIdType.value, __productIdType.set, None, 'Type of unique identifier used in the "Product ID" field. Example: UPC; GTIN; ISBN; ISSN; EAN')

    
    # Element {http://walmart.com/}productId uses Python identifier productId
    __productId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productId'), 'productId', '__httpwalmart_com_productIdentifier_httpwalmart_comproductId', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1529, 15), )

    
    productId = property(__productId.value, __productId.set, None, 'Alphanumeric ID that uniquely identifies the product. Example: X12345')

    _ElementMap.update({
        __productIdType.name() : __productIdType,
        __productId.name() : __productId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.productIdentifier = productIdentifier
Namespace.addCategoryObject('typeBinding', 'productIdentifier', productIdentifier)


# Complex type {http://walmart.com/}certificationsAndClaim with content type ELEMENT_ONLY
class certificationsAndClaim (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}certificationsAndClaim with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'certificationsAndClaim')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1544, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}certificationAndClaimType uses Python identifier certificationAndClaimType
    __certificationAndClaimType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'certificationAndClaimType'), 'certificationAndClaimType', '__httpwalmart_com_certificationsAndClaim_httpwalmart_comcertificationAndClaimType', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1546, 15), )

    
    certificationAndClaimType = property(__certificationAndClaimType.value, __certificationAndClaimType.set, None, 'Type of certification or claim. Example: Organic; BPA-Free; Fair Trade')

    
    # Element {http://walmart.com/}certifyingAgent uses Python identifier certifyingAgent
    __certifyingAgent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'certifyingAgent'), 'certifyingAgent', '__httpwalmart_com_certificationsAndClaim_httpwalmart_comcertifyingAgent', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1559, 15), )

    
    certifyingAgent = property(__certifyingAgent.value, __certifyingAgent.set, None, 'Certifying agency for claim. Not all claims have a certifying agent. Example: Oregon Tilth; GOTS')

    _ElementMap.update({
        __certificationAndClaimType.name() : __certificationAndClaimType,
        __certifyingAgent.name() : __certifyingAgent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.certificationsAndClaim = certificationsAndClaim
Namespace.addCategoryObject('typeBinding', 'certificationsAndClaim', certificationsAndClaim)


# Complex type {http://walmart.com/}batteryTypeAndQuantityValue with content type ELEMENT_ONLY
class batteryTypeAndQuantityValue (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}batteryTypeAndQuantityValue with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'batteryTypeAndQuantityValue')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1574, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}batteryTechnologyType uses Python identifier batteryTechnologyType
    __batteryTechnologyType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'batteryTechnologyType'), 'batteryTechnologyType', '__httpwalmart_com_batteryTypeAndQuantityValue_httpwalmart_combatteryTechnologyType', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1576, 15), )

    
    batteryTechnologyType = property(__batteryTechnologyType.value, __batteryTechnologyType.set, None, 'If battery type is lead acid, lead acid (nonspillable), lithium ion, or lithium metal, the item requires a hazardous materials risk assessment via WERCS. Example: Does Not Contain a Battery; Alkaline; Carbon Zinc; Lead Acid; Lead Acid (Nonspillable); Lithium Primary (Lithium Metal); Lithium Ion; Magnesium; Mercury; Nickel Cadmium; Nickel Metal Hydride; Silver; Thermal; Other; Multiple Types')

    
    # Element {http://walmart.com/}numberOfBatteries uses Python identifier numberOfBatteries
    __numberOfBatteries = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'numberOfBatteries'), 'numberOfBatteries', '__httpwalmart_com_batteryTypeAndQuantityValue_httpwalmart_comnumberOfBatteries', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1603, 15), )

    
    numberOfBatteries = property(__numberOfBatteries.value, __numberOfBatteries.set, None, 'Required if "Has Batteries = Y"')

    _ElementMap.update({
        __batteryTechnologyType.name() : __batteryTechnologyType,
        __numberOfBatteries.name() : __numberOfBatteries
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.batteryTypeAndQuantityValue = batteryTypeAndQuantityValue
Namespace.addCategoryObject('typeBinding', 'batteryTypeAndQuantityValue', batteryTypeAndQuantityValue)


# Complex type {http://walmart.com/}stateRestriction with content type EMPTY
class stateRestriction (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}stateRestriction with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stateRestriction')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1616, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.stateRestriction = stateRestriction
Namespace.addCategoryObject('typeBinding', 'stateRestriction', stateRestriction)


# Complex type {http://walmart.com/}additionalProductAttribute with content type ELEMENT_ONLY
class additionalProductAttribute (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}additionalProductAttribute with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'additionalProductAttribute')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1619, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}productAttributeName uses Python identifier productAttributeName
    __productAttributeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productAttributeName'), 'productAttributeName', '__httpwalmart_com_additionalProductAttribute_httpwalmart_comproductAttributeName', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1621, 15), )

    
    productAttributeName = property(__productAttributeName.value, __productAttributeName.set, None, 'A name of a single attribute for the additional detail name-value pair. Example: isCFLLightBulb')

    
    # Element {http://walmart.com/}productAttributeValue uses Python identifier productAttributeValue
    __productAttributeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productAttributeValue'), 'productAttributeValue', '__httpwalmart_com_additionalProductAttribute_httpwalmart_comproductAttributeValue', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1634, 15), )

    
    productAttributeValue = property(__productAttributeValue.value, __productAttributeValue.set, None, 'A value of a single attribute for the additional detail name-value pair. Example: true')

    _ElementMap.update({
        __productAttributeName.name() : __productAttributeName,
        __productAttributeValue.name() : __productAttributeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.additionalProductAttribute = additionalProductAttribute
Namespace.addCategoryObject('typeBinding', 'additionalProductAttribute', additionalProductAttribute)


# Complex type {http://walmart.com/}swatchImage with content type ELEMENT_ONLY
class swatchImage (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}swatchImage with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'swatchImage')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1649, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}swatchImageUrl uses Python identifier swatchImageUrl
    __swatchImageUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'swatchImageUrl'), 'swatchImageUrl', '__httpwalmart_com_swatchImage_httpwalmart_comswatchImageUrl', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1651, 15), )

    
    swatchImageUrl = property(__swatchImageUrl.value, __swatchImageUrl.set, None, 'URL of the color or pattern swatch image. This will be shown as a small square on the item page. Recommended resolution is 100 x 100 pixels. URLs must begin with http:// or https:// Example: http://www.walmart.com/swatch1.jpg')

    
    # Element {http://walmart.com/}swatchVariantAttribute uses Python identifier swatchVariantAttribute
    __swatchVariantAttribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'swatchVariantAttribute'), 'swatchVariantAttribute', '__httpwalmart_com_swatchImage_httpwalmart_comswatchVariantAttribute', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1664, 15), )

    
    swatchVariantAttribute = property(__swatchVariantAttribute.value, __swatchVariantAttribute.set, None, 'Attribute name corresponding to the swatch. Example: color; pattern')

    _ElementMap.update({
        __swatchImageUrl.name() : __swatchImageUrl,
        __swatchVariantAttribute.name() : __swatchVariantAttribute
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.swatchImage = swatchImage
Namespace.addCategoryObject('typeBinding', 'swatchImage', swatchImage)


# Complex type {http://walmart.com/}recycledMaterialContentValue with content type ELEMENT_ONLY
class recycledMaterialContentValue (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}recycledMaterialContentValue with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'recycledMaterialContentValue')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1679, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}recycledMaterial uses Python identifier recycledMaterial
    __recycledMaterial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recycledMaterial'), 'recycledMaterial', '__httpwalmart_com_recycledMaterialContentValue_httpwalmart_comrecycledMaterial', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1681, 15), )

    
    recycledMaterial = property(__recycledMaterial.value, __recycledMaterial.set, None, 'Type of recycled material used to create the item. Example: Bamboo; Cotton')

    
    # Element {http://walmart.com/}percentageOfRecycledMaterial uses Python identifier percentageOfRecycledMaterial
    __percentageOfRecycledMaterial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'percentageOfRecycledMaterial'), 'percentageOfRecycledMaterial', '__httpwalmart_com_recycledMaterialContentValue_httpwalmart_compercentageOfRecycledMaterial', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1694, 15), )

    
    percentageOfRecycledMaterial = property(__percentageOfRecycledMaterial.value, __percentageOfRecycledMaterial.set, None, 'Corresponding percentage of the recycled material used to create the item. Example: 90%; 80%')

    _ElementMap.update({
        __recycledMaterial.name() : __recycledMaterial,
        __percentageOfRecycledMaterial.name() : __percentageOfRecycledMaterial
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.recycledMaterialContentValue = recycledMaterialContentValue
Namespace.addCategoryObject('typeBinding', 'recycledMaterialContentValue', recycledMaterialContentValue)


# Complex type {http://walmart.com/}activeIngredient with content type ELEMENT_ONLY
class activeIngredient (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}activeIngredient with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'activeIngredient')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1707, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}activeIngredientName uses Python identifier activeIngredientName
    __activeIngredientName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activeIngredientName'), 'activeIngredientName', '__httpwalmart_com_activeIngredient_httpwalmart_comactiveIngredientName', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1709, 15), )

    
    activeIngredientName = property(__activeIngredientName.value, __activeIngredientName.set, None, 'Ingredient name. Example: Benzoyl Peroxide')

    
    # Element {http://walmart.com/}activeIngredientPercentage uses Python identifier activeIngredientPercentage
    __activeIngredientPercentage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activeIngredientPercentage'), 'activeIngredientPercentage', '__httpwalmart_com_activeIngredient_httpwalmart_comactiveIngredientPercentage', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1722, 15), )

    
    activeIngredientPercentage = property(__activeIngredientPercentage.value, __activeIngredientPercentage.set, None, 'The percent of the active ingredient in the item. Example: 0.02')

    _ElementMap.update({
        __activeIngredientName.name() : __activeIngredientName,
        __activeIngredientPercentage.name() : __activeIngredientPercentage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.activeIngredient = activeIngredient
Namespace.addCategoryObject('typeBinding', 'activeIngredient', activeIngredient)


# Complex type {http://walmart.com/}fabricContentValue with content type ELEMENT_ONLY
class fabricContentValue (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}fabricContentValue with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fabricContentValue')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1735, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}materialName uses Python identifier materialName
    __materialName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'materialName'), 'materialName', '__httpwalmart_com_fabricContentValue_httpwalmart_commaterialName', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1737, 15), )

    
    materialName = property(__materialName.value, __materialName.set, None, 'Material name. Example: Cotton; Rayon')

    
    # Element {http://walmart.com/}materialPercentage uses Python identifier materialPercentage
    __materialPercentage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'materialPercentage'), 'materialPercentage', '__httpwalmart_com_fabricContentValue_httpwalmart_commaterialPercentage', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1750, 15), )

    
    materialPercentage = property(__materialPercentage.value, __materialPercentage.set, None, 'Corresponding material percentage. Example: 98%; 2%')

    _ElementMap.update({
        __materialName.name() : __materialName,
        __materialPercentage.name() : __materialPercentage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.fabricContentValue = fabricContentValue
Namespace.addCategoryObject('typeBinding', 'fabricContentValue', fabricContentValue)


# Complex type {http://walmart.com/}nutrient with content type ELEMENT_ONLY
class nutrient (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}nutrient with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nutrient')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1763, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}nutrientName uses Python identifier nutrientName
    __nutrientName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nutrientName'), 'nutrientName', '__httpwalmart_com_nutrient_httpwalmart_comnutrientName', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1765, 15), )

    
    nutrientName = property(__nutrientName.value, __nutrientName.set, None, 'Name of additional nutrient.')

    
    # Element {http://walmart.com/}nutrientAmount uses Python identifier nutrientAmount
    __nutrientAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nutrientAmount'), 'nutrientAmount', '__httpwalmart_com_nutrient_httpwalmart_comnutrientAmount', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1778, 15), )

    
    nutrientAmount = property(__nutrientAmount.value, __nutrientAmount.set, None, 'Amount of the nutrient present in one serving. Example: 30 g')

    
    # Element {http://walmart.com/}nutrientPercentageDailyValue uses Python identifier nutrientPercentageDailyValue
    __nutrientPercentageDailyValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nutrientPercentageDailyValue'), 'nutrientPercentageDailyValue', '__httpwalmart_com_nutrient_httpwalmart_comnutrientPercentageDailyValue', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1789, 15), )

    
    nutrientPercentageDailyValue = property(__nutrientPercentageDailyValue.value, __nutrientPercentageDailyValue.set, None, 'Percent daily value of the nutrient present in one serving. Example: 0.15')

    _ElementMap.update({
        __nutrientName.name() : __nutrientName,
        __nutrientAmount.name() : __nutrientAmount,
        __nutrientPercentageDailyValue.name() : __nutrientPercentageDailyValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.nutrient = nutrient
Namespace.addCategoryObject('typeBinding', 'nutrient', nutrient)


# Complex type {http://walmart.com/}inputsAndOutput with content type ELEMENT_ONLY
class inputsAndOutput (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}inputsAndOutput with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'inputsAndOutput')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1802, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}inputOutputType uses Python identifier inputOutputType
    __inputOutputType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inputOutputType'), 'inputOutputType', '__httpwalmart_com_inputsAndOutput_httpwalmart_cominputOutputType', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1804, 15), )

    
    inputOutputType = property(__inputOutputType.value, __inputOutputType.set, None, 'Type of connection. Example: HDMI; S/PDIF; USB 3.0; DVI')

    
    # Element {http://walmart.com/}inputOutputQuantity uses Python identifier inputOutputQuantity
    __inputOutputQuantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inputOutputQuantity'), 'inputOutputQuantity', '__httpwalmart_com_inputsAndOutput_httpwalmart_cominputOutputQuantity', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1817, 15), )

    
    inputOutputQuantity = property(__inputOutputQuantity.value, __inputOutputQuantity.set, None, 'Number of connections corresponding to the Input/Output type. Example: 2; 1; 3; 1')

    _ElementMap.update({
        __inputOutputType.name() : __inputOutputType,
        __inputOutputQuantity.name() : __inputOutputQuantity
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.inputsAndOutput = inputsAndOutput
Namespace.addCategoryObject('typeBinding', 'inputsAndOutput', inputsAndOutput)


# Complex type {http://walmart.com/}trackListing with content type ELEMENT_ONLY
class trackListing (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}trackListing with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'trackListing')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1830, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}trackNumber uses Python identifier trackNumber
    __trackNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trackNumber'), 'trackNumber', '__httpwalmart_com_trackListing_httpwalmart_comtrackNumber', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1832, 15), )

    
    trackNumber = property(__trackNumber.value, __trackNumber.set, None, 'The number of the individual track on an album. Example: 2.0')

    
    # Element {http://walmart.com/}trackName uses Python identifier trackName
    __trackName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trackName'), 'trackName', '__httpwalmart_com_trackListing_httpwalmart_comtrackName', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1843, 15), )

    
    trackName = property(__trackName.value, __trackName.set, None, 'The name of the individual track on an album. Example: Blue Suede Shoes')

    
    # Element {http://walmart.com/}trackDuration uses Python identifier trackDuration
    __trackDuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trackDuration'), 'trackDuration', '__httpwalmart_com_trackListing_httpwalmart_comtrackDuration', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1856, 15), )

    
    trackDuration = property(__trackDuration.value, __trackDuration.set, None, 'The duration of the individual track on an album. Example: 4.23 min')

    _ElementMap.update({
        __trackNumber.name() : __trackNumber,
        __trackName.name() : __trackName,
        __trackDuration.name() : __trackDuration
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.trackListing = trackListing
Namespace.addCategoryObject('typeBinding', 'trackListing', trackListing)


# Complex type {http://walmart.com/}AdditionalAssetAttributes with content type ELEMENT_ONLY
class AdditionalAssetAttributes (pyxb.binding.basis.complexTypeDefinition):
    """Additional details about the provided assets using name-value pairs."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdditionalAssetAttributes')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1869, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}additionalAssetAttribute uses Python identifier additionalAssetAttribute
    __additionalAssetAttribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'additionalAssetAttribute'), 'additionalAssetAttribute', '__httpwalmart_com_AdditionalAssetAttributes_httpwalmart_comadditionalAssetAttribute', True, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1874, 15), )

    
    additionalAssetAttribute = property(__additionalAssetAttribute.value, __additionalAssetAttribute.set, None, None)

    _ElementMap.update({
        __additionalAssetAttribute.name() : __additionalAssetAttribute
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdditionalAssetAttributes = AdditionalAssetAttributes
Namespace.addCategoryObject('typeBinding', 'AdditionalAssetAttributes', AdditionalAssetAttributes)


# Complex type {http://walmart.com/}additionalAssetAttribute with content type ELEMENT_ONLY
class additionalAssetAttribute (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://walmart.com/}additionalAssetAttribute with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'additionalAssetAttribute')
    _XSDLocation = pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1877, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://walmart.com/}attributeName uses Python identifier attributeName
    __attributeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributeName'), 'attributeName', '__httpwalmart_com_additionalAssetAttribute_httpwalmart_comattributeName', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1879, 15), )

    
    attributeName = property(__attributeName.value, __attributeName.set, None, 'A name of a single attribute for the additional detail name-value pair. Example: documentType')

    
    # Element {http://walmart.com/}attributeValue uses Python identifier attributeValue
    __attributeValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributeValue'), 'attributeValue', '__httpwalmart_com_additionalAssetAttribute_httpwalmart_comattributeValue', False, pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1892, 15), )

    
    attributeValue = property(__attributeValue.value, __attributeValue.set, None, 'A value of a single attribute for the additional detail name-value pair. Example: PDF')

    _ElementMap.update({
        __attributeName.name() : __attributeName,
        __attributeValue.name() : __attributeValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.additionalAssetAttribute = additionalAssetAttribute
Namespace.addCategoryObject('typeBinding', 'additionalAssetAttribute', additionalAssetAttribute)




MainImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mainImageUrl'), STD_ANON, scope=MainImage, documentation='Location of the image. URLs must begin with http:// or https:// Example: http://www.walmart.com/main_image.jpg', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 15, 15)))

MainImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'altText'), STD_ANON_, scope=MainImage, documentation='Alternative text of an image, video, or other asset. Use descriptive terms to describe the image.', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 28, 15)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 28, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MainImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mainImageUrl')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 15, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MainImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'altText')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 28, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MainImage._Automaton = _BuildAutomaton()




AdditionalAssets._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'additionalAsset'), additionalAsset, scope=AdditionalAssets, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 48, 15)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 48, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalAssets._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'additionalAsset')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 48, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AdditionalAssets._Automaton = _BuildAutomaton_()




ProductIdentifiers._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productIdentifier'), productIdentifier, scope=ProductIdentifiers, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 56, 15)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 56, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProductIdentifiers._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productIdentifier')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 56, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ProductIdentifiers._Automaton = _BuildAutomaton_2()




CurrencyUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), CurrencyUnitOfMeasure, scope=CurrencyUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 61, 15)))

CurrencyUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_2, scope=CurrencyUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 62, 15)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 61, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 62, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CurrencyUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 61, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CurrencyUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 62, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CurrencyUnit._Automaton = _BuildAutomaton_3()




Features._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'feature'), STD_ANON_3, scope=Features, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 74, 15)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 74, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Features._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'feature')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 74, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Features._Automaton = _BuildAutomaton_4()




CertificationsAndClaims._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'certificationsAndClaim'), certificationsAndClaim, scope=CertificationsAndClaims, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 88, 15)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 88, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CertificationsAndClaims._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'certificationsAndClaim')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 88, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CertificationsAndClaims._Automaton = _BuildAutomaton_5()




LengthUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), LengthUnitOfMeasure, scope=LengthUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 93, 15)))

LengthUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_4, scope=LengthUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 94, 15)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 93, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 94, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LengthUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 93, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LengthUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 94, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LengthUnit._Automaton = _BuildAutomaton_6()




WeightUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), WeightUnitOfMeasure, scope=WeightUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 103, 15)))

WeightUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_5, scope=WeightUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 104, 15)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 103, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 104, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(WeightUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 103, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(WeightUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 104, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
WeightUnit._Automaton = _BuildAutomaton_7()




SportsLeague._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sportsLeagueValue'), STD_ANON_6, scope=SportsLeague, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 113, 15)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 113, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SportsLeague._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sportsLeagueValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 113, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SportsLeague._Automaton = _BuildAutomaton_8()




SportsTeam._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sportsTeamValue'), STD_ANON_7, scope=SportsTeam, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 124, 15)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 124, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SportsTeam._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sportsTeamValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 124, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SportsTeam._Automaton = _BuildAutomaton_9()




Athlete._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'athleteValue'), STD_ANON_8, scope=Athlete, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 135, 15)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 135, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Athlete._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'athleteValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 135, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Athlete._Automaton = _BuildAutomaton_10()




BatteryTypeAndQuantity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'batteryTypeAndQuantityValue'), batteryTypeAndQuantityValue, scope=BatteryTypeAndQuantity, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 149, 15)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 149, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BatteryTypeAndQuantity._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'batteryTypeAndQuantityValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 149, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BatteryTypeAndQuantity._Automaton = _BuildAutomaton_11()




PPUUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), PPUUnitOfMeasure, scope=PPUUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 154, 15)))

PPUUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_9, scope=PPUUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 155, 15)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 154, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 155, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PPUUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 154, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PPUUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 155, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PPUUnit._Automaton = _BuildAutomaton_12()




TemperatureUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), TemperatureUnitOfMeasure, scope=TemperatureUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 164, 15)))

TemperatureUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_10, scope=TemperatureUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 165, 15)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 164, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 165, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TemperatureUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 164, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TemperatureUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 165, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TemperatureUnit._Automaton = _BuildAutomaton_13()




SmallPartsWarnings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'smallPartsWarning'), STD_ANON_11, scope=SmallPartsWarnings, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 186, 15)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 186, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SmallPartsWarnings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'smallPartsWarning')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 186, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SmallPartsWarnings._Automaton = _BuildAutomaton_14()




StateRestrictions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stateRestriction'), stateRestriction, scope=StateRestrictions, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 195, 15)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 195, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StateRestrictions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stateRestriction')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 195, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StateRestrictions._Automaton = _BuildAutomaton_15()




AdditionalProductAttributes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'additionalProductAttribute'), additionalProductAttribute, scope=AdditionalProductAttributes, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 203, 15)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 203, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalProductAttributes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'additionalProductAttribute')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 203, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AdditionalProductAttributes._Automaton = _BuildAutomaton_16()




SwatchImages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'swatchImage'), swatchImage, scope=SwatchImages, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 211, 15)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 211, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SwatchImages._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'swatchImage')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 211, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SwatchImages._Automaton = _BuildAutomaton_17()




AccessoriesIncluded._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accessoriesIncludedValue'), STD_ANON_12, scope=AccessoriesIncluded, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 216, 15)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 216, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AccessoriesIncluded._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accessoriesIncludedValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 216, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AccessoriesIncluded._Automaton = _BuildAutomaton_18()




VariantAttributeNames._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'variantAttributeName'), STD_ANON_13, scope=VariantAttributeNames, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 231, 15)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 231, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VariantAttributeNames._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'variantAttributeName')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 231, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
VariantAttributeNames._Automaton = _BuildAutomaton_19()




Color._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'colorValue'), STD_ANON_14, scope=Color, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 245, 15)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 245, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Color._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'colorValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 245, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Color._Automaton = _BuildAutomaton_20()




Material._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'materialValue'), STD_ANON_15, scope=Material, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 259, 15)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 259, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Material._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'materialValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 259, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Material._Automaton = _BuildAutomaton_21()




RecommendedUses._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recommendedUse'), STD_ANON_16, scope=RecommendedUses, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 273, 15)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 273, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RecommendedUses._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recommendedUse')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 273, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RecommendedUses._Automaton = _BuildAutomaton_22()




MountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mountTypeValue'), STD_ANON_17, scope=MountType, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 287, 15)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 287, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mountTypeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 287, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MountType._Automaton = _BuildAutomaton_23()




VolumeUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), VolumeUnitOfMeasure, scope=VolumeUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 298, 15)))

VolumeUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_18, scope=VolumeUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 299, 15)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 298, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 299, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VolumeUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 298, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(VolumeUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 299, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
VolumeUnit._Automaton = _BuildAutomaton_24()




ElectricalMeasurementUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), ElectricalMeasurementUnitOfMeasure, scope=ElectricalMeasurementUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 308, 15)))

ElectricalMeasurementUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_19, scope=ElectricalMeasurementUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 309, 15)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 308, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 309, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ElectricalMeasurementUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 308, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ElectricalMeasurementUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 309, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ElectricalMeasurementUnit._Automaton = _BuildAutomaton_25()




PowerUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), PowerUnitOfMeasure, scope=PowerUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 318, 15)))

PowerUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_20, scope=PowerUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 319, 15)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 318, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 319, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PowerUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 318, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PowerUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 319, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PowerUnit._Automaton = _BuildAutomaton_26()




AreaUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), AreaUnitOfMeasure, scope=AreaUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 328, 15)))

AreaUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_21, scope=AreaUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 329, 15)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 328, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 329, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AreaUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 328, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AreaUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 329, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AreaUnit._Automaton = _BuildAutomaton_27()




Pattern._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'patternValue'), STD_ANON_22, scope=Pattern, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 341, 15)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 341, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Pattern._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'patternValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 341, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Pattern._Automaton = _BuildAutomaton_28()




CompatibleSurfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'compatibleSurface'), STD_ANON_23, scope=CompatibleSurfaces, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 352, 15)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 352, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CompatibleSurfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'compatibleSurface')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 352, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CompatibleSurfaces._Automaton = _BuildAutomaton_29()




TimeUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), TimeUnitOfMeasure, scope=TimeUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 363, 15)))

TimeUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_24, scope=TimeUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 364, 15)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 363, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 364, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TimeUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 363, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TimeUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 364, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TimeUnit._Automaton = _BuildAutomaton_30()




RecycledMaterialContent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recycledMaterialContentValue'), recycledMaterialContentValue, scope=RecycledMaterialContent, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 373, 15)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 373, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RecycledMaterialContent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recycledMaterialContentValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 373, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RecycledMaterialContent._Automaton = _BuildAutomaton_31()




RecommendedSurfaces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recommendedSurface'), STD_ANON_25, scope=RecommendedSurfaces, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 381, 15)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 381, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RecommendedSurfaces._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recommendedSurface')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 381, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RecommendedSurfaces._Automaton = _BuildAutomaton_32()




PressureUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), PressureUnitOfMeasure, scope=PressureUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 392, 15)))

PressureUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_26, scope=PressureUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 393, 15)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 392, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 393, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PressureUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 392, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PressureUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 393, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PressureUnit._Automaton = _BuildAutomaton_33()




PercentageUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), PercentageUnitOfMeasure, scope=PercentageUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 402, 15)))

PercentageUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_27, scope=PercentageUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 403, 15)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 402, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 403, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PercentageUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 402, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PercentageUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 403, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PercentageUnit._Automaton = _BuildAutomaton_34()




ActiveIngredients._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activeIngredient'), activeIngredient, scope=ActiveIngredients, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 415, 15)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 415, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ActiveIngredients._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activeIngredient')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 415, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ActiveIngredients._Automaton = _BuildAutomaton_35()




InactiveIngredients._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inactiveIngredient'), STD_ANON_28, scope=InactiveIngredients, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 423, 15)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 423, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InactiveIngredients._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inactiveIngredient')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 423, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InactiveIngredients._Automaton = _BuildAutomaton_36()




SpeedUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), SpeedUnitOfMeasure, scope=SpeedUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 434, 15)))

SpeedUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_29, scope=SpeedUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 435, 15)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 434, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 435, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpeedUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 434, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SpeedUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 435, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SpeedUnit._Automaton = _BuildAutomaton_37()




Character._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'characterValue'), STD_ANON_30, scope=Character, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 447, 15)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 447, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Character._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'characterValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 447, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Character._Automaton = _BuildAutomaton_38()




AngleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), AngleUnitOfMeasure, scope=AngleUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 458, 15)))

AngleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_31, scope=AngleUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 459, 15)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 458, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 459, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AngleUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 458, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AngleUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 459, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AngleUnit._Automaton = _BuildAutomaton_39()




BrightnessUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), BrightnessUnitOfMeasure, scope=BrightnessUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 468, 15)))

BrightnessUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_32, scope=BrightnessUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 469, 15)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 468, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 469, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BrightnessUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 468, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BrightnessUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 469, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BrightnessUnit._Automaton = _BuildAutomaton_40()




FabricContent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fabricContentValue'), fabricContentValue, scope=FabricContent, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 481, 15)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 481, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FabricContent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fabricContentValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 481, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FabricContent._Automaton = _BuildAutomaton_41()




FabricCareInstructions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fabricCareInstruction'), STD_ANON_33, scope=FabricCareInstructions, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 489, 15)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 489, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FabricCareInstructions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fabricCareInstruction')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 489, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FabricCareInstructions._Automaton = _BuildAutomaton_42()




Theme._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'themeValue'), STD_ANON_34, scope=Theme, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 503, 15)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 503, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Theme._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'themeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 503, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Theme._Automaton = _BuildAutomaton_43()




AgeGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ageGroupValue'), STD_ANON_35, scope=AgeGroup, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 517, 15)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 517, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AgeGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ageGroupValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 517, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AgeGroup._Automaton = _BuildAutomaton_44()




RecommendedRooms._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recommendedRoom'), STD_ANON_36, scope=RecommendedRooms, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 531, 15)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 531, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RecommendedRooms._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recommendedRoom')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 531, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RecommendedRooms._Automaton = _BuildAutomaton_45()




Occasion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'occasionValue'), STD_ANON_37, scope=Occasion, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 545, 15)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 545, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Occasion._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'occasionValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 545, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Occasion._Automaton = _BuildAutomaton_46()




FillMaterial._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fillMaterialValue'), STD_ANON_38, scope=FillMaterial, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 559, 15)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 559, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FillMaterial._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fillMaterialValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 559, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FillMaterial._Automaton = _BuildAutomaton_47()




HolidayLightingStyle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'holidayLightingStyleValue'), STD_ANON_39, scope=HolidayLightingStyle, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 573, 15)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 573, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(HolidayLightingStyle._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'holidayLightingStyleValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 573, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
HolidayLightingStyle._Automaton = _BuildAutomaton_48()




TargetAudience._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'targetAudienceValue'), STD_ANON_40, scope=TargetAudience, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 587, 15)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 587, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TargetAudience._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'targetAudienceValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 587, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TargetAudience._Automaton = _BuildAutomaton_49()




HairLength._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hairLengthValue'), STD_ANON_41, scope=HairLength, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 601, 15)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 601, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(HairLength._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hairLengthValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 601, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
HairLength._Automaton = _BuildAutomaton_50()




StopUseIndications._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stopUseIndication'), STD_ANON_42, scope=StopUseIndications, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 615, 15)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 615, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StopUseIndications._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stopUseIndication')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 615, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StopUseIndications._Automaton = _BuildAutomaton_51()




NutrientContentClaims._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nutrientContentClaim'), STD_ANON_43, scope=NutrientContentClaims, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 629, 15)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 629, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NutrientContentClaims._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nutrientContentClaim')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 629, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NutrientContentClaims._Automaton = _BuildAutomaton_52()




Sport._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sportValue'), STD_ANON_44, scope=Sport, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 643, 15)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 643, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Sport._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sportValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 643, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Sport._Automaton = _BuildAutomaton_53()




DiaposableBabyDiaperType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'diaposableBabyDiaperTypeValue'), STD_ANON_45, scope=DiaposableBabyDiaperType, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 657, 15)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 657, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DiaposableBabyDiaperType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'diaposableBabyDiaperTypeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 657, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DiaposableBabyDiaperType._Automaton = _BuildAutomaton_54()




OrganicCertifications._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'organicCertification'), STD_ANON_46, scope=OrganicCertifications, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 671, 15)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 671, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrganicCertifications._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'organicCertification')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 671, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OrganicCertifications._Automaton = _BuildAutomaton_55()




Season._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'seasonValue'), STD_ANON_47, scope=Season, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 685, 15)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 685, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Season._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'seasonValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 685, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Season._Automaton = _BuildAutomaton_56()




AwardsWon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'awardsWonValue'), STD_ANON_48, scope=AwardsWon, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 699, 15)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 699, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AwardsWon._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'awardsWonValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 699, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AwardsWon._Automaton = _BuildAutomaton_57()




EducationalFocus._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'educationalFocu'), STD_ANON_49, scope=EducationalFocus, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 713, 15)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 713, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EducationalFocus._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'educationalFocu')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 713, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EducationalFocus._Automaton = _BuildAutomaton_58()




Nutrients._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nutrient'), nutrient, scope=Nutrients, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 727, 15)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 727, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Nutrients._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nutrient')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 727, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Nutrients._Automaton = _BuildAutomaton_59()




RecommendedLocations._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recommendedLocation'), STD_ANON_50, scope=RecommendedLocations, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 735, 15)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 735, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RecommendedLocations._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recommendedLocation')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 735, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RecommendedLocations._Automaton = _BuildAutomaton_60()




FrameMaterial._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'frameMaterialValue'), STD_ANON_51, scope=FrameMaterial, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 749, 15)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 749, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FrameMaterial._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'frameMaterialValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 749, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FrameMaterial._Automaton = _BuildAutomaton_61()




Connections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'connection'), STD_ANON_52, scope=Connections, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 763, 15)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 763, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Connections._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'connection')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 763, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Connections._Automaton = _BuildAutomaton_62()




AudioFeatures._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'audioFeature'), STD_ANON_53, scope=AudioFeatures, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 777, 15)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 777, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AudioFeatures._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'audioFeature')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 777, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AudioFeatures._Automaton = _BuildAutomaton_63()




MobileOperatingSystem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mobileOperatingSystemValue'), STD_ANON_54, scope=MobileOperatingSystem, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 791, 15)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 791, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MobileOperatingSystem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mobileOperatingSystemValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 791, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MobileOperatingSystem._Automaton = _BuildAutomaton_64()




ResolutionUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), ResolutionUnitOfMeasure, scope=ResolutionUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 802, 15)))

ResolutionUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_55, scope=ResolutionUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 803, 15)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 802, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 803, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ResolutionUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 802, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ResolutionUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 803, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ResolutionUnit._Automaton = _BuildAutomaton_65()




DigitalCapacityUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), DigitalCapacityUnitOfMeasure, scope=DigitalCapacityUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 812, 15)))

DigitalCapacityUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_56, scope=DigitalCapacityUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 813, 15)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 812, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 813, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DigitalCapacityUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 812, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DigitalCapacityUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 813, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DigitalCapacityUnit._Automaton = _BuildAutomaton_66()




FrequencyUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), FrequencyUnitOfMeasure, scope=FrequencyUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 822, 15)))

FrequencyUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_57, scope=FrequencyUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 823, 15)))

def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 822, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 823, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FrequencyUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 822, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FrequencyUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 823, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FrequencyUnit._Automaton = _BuildAutomaton_67()




ProcessorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'processorTypeValue'), STD_ANON_58, scope=ProcessorType, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 835, 15)))

def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 835, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProcessorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'processorTypeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 835, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ProcessorType._Automaton = _BuildAutomaton_68()




WirelessTechnologies._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wirelessTechnology'), STD_ANON_59, scope=WirelessTechnologies, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 849, 15)))

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 849, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(WirelessTechnologies._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wirelessTechnology')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 849, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
WirelessTechnologies._Automaton = _BuildAutomaton_69()




TelevisionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'televisionTypeValue'), STD_ANON_60, scope=TelevisionType, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 863, 15)))

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 863, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TelevisionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'televisionTypeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 863, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TelevisionType._Automaton = _BuildAutomaton_70()




InputsAndOutputs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inputsAndOutput'), inputsAndOutput, scope=InputsAndOutputs, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 877, 15)))

def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 877, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InputsAndOutputs._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inputsAndOutput')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 877, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InputsAndOutputs._Automaton = _BuildAutomaton_71()




CompatibleDevices._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'compatibleDevice'), STD_ANON_61, scope=CompatibleDevices, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 885, 15)))

def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 885, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CompatibleDevices._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'compatibleDevice')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 885, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CompatibleDevices._Automaton = _BuildAutomaton_72()




SoftwareCategory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'softwareCategoryValue'), STD_ANON_62, scope=SoftwareCategory, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 899, 15)))

def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 899, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SoftwareCategory._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'softwareCategoryValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 899, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SoftwareCategory._Automaton = _BuildAutomaton_73()




SystemRequirements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'systemRequirement'), STD_ANON_63, scope=SystemRequirements, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 913, 15)))

def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 913, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SystemRequirements._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'systemRequirement')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 913, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SystemRequirements._Automaton = _BuildAutomaton_74()




OperatingSystem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'operatingSystemValue'), STD_ANON_64, scope=OperatingSystem, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 927, 15)))

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 927, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OperatingSystem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'operatingSystemValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 927, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OperatingSystem._Automaton = _BuildAutomaton_75()




CpuSocketType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpuSocketTypeValue'), STD_ANON_65, scope=CpuSocketType, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 941, 15)))

def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 941, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CpuSocketType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cpuSocketTypeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 941, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CpuSocketType._Automaton = _BuildAutomaton_76()




MotherboardFormFactor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'motherboardFormFactorValue'), STD_ANON_66, scope=MotherboardFormFactor, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 955, 15)))

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 955, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MotherboardFormFactor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'motherboardFormFactorValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 955, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MotherboardFormFactor._Automaton = _BuildAutomaton_77()




RecordableMediaFormats._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordableMediaFormat'), STD_ANON_67, scope=RecordableMediaFormats, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 969, 15)))

def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 969, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RecordableMediaFormats._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordableMediaFormat')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 969, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RecordableMediaFormats._Automaton = _BuildAutomaton_78()




CompatibleBrands._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'compatibleBrand'), STD_ANON_68, scope=CompatibleBrands, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 983, 15)))

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 983, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CompatibleBrands._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'compatibleBrand')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 983, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CompatibleBrands._Automaton = _BuildAutomaton_79()




HeadphoneFeatures._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'headphoneFeature'), STD_ANON_69, scope=HeadphoneFeatures, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 997, 15)))

def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 997, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(HeadphoneFeatures._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'headphoneFeature')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 997, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
HeadphoneFeatures._Automaton = _BuildAutomaton_80()




VolumetricFlowRateUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), VolumetricFlowRateUnitOfMeasure, scope=VolumetricFlowRateUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1008, 15)))

VolumetricFlowRateUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_70, scope=VolumetricFlowRateUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1009, 15)))

def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1008, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1009, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VolumetricFlowRateUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1008, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(VolumetricFlowRateUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1009, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
VolumetricFlowRateUnit._Automaton = _BuildAutomaton_81()




OriginalLanguages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalLanguage'), STD_ANON_71, scope=OriginalLanguages, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1021, 15)))

def _BuildAutomaton_82 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1021, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OriginalLanguages._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalLanguage')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1021, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OriginalLanguages._Automaton = _BuildAutomaton_82()




Actors._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actor'), STD_ANON_72, scope=Actors, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1035, 15)))

def _BuildAutomaton_83 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_83
    del _BuildAutomaton_83
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1035, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Actors._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actor')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1035, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Actors._Automaton = _BuildAutomaton_83()




DubbedLanguages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dubbedLanguage'), STD_ANON_73, scope=DubbedLanguages, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1049, 15)))

def _BuildAutomaton_84 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1049, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DubbedLanguages._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dubbedLanguage')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1049, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DubbedLanguages._Automaton = _BuildAutomaton_84()




SubtitledLanguages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subtitledLanguage'), STD_ANON_74, scope=SubtitledLanguages, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1063, 15)))

def _BuildAutomaton_85 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1063, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SubtitledLanguages._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subtitledLanguage')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1063, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SubtitledLanguages._Automaton = _BuildAutomaton_85()




Performer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'performerValue'), STD_ANON_75, scope=Performer, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1077, 15)))

def _BuildAutomaton_86 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_86
    del _BuildAutomaton_86
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1077, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Performer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'performerValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1077, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Performer._Automaton = _BuildAutomaton_86()




TrackListings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trackListing'), trackListing, scope=TrackListings, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1091, 15)))

def _BuildAutomaton_87 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_87
    del _BuildAutomaton_87
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1091, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TrackListings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trackListing')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1091, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TrackListings._Automaton = _BuildAutomaton_87()




Author._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authorValue'), STD_ANON_76, scope=Author, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1099, 15)))

def _BuildAutomaton_88 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1099, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Author._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'authorValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1099, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Author._Automaton = _BuildAutomaton_88()




InkColor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inkColorValue'), STD_ANON_77, scope=InkColor, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1113, 15)))

def _BuildAutomaton_89 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_89
    del _BuildAutomaton_89
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1113, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InkColor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inkColorValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1113, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InkColor._Automaton = _BuildAutomaton_89()




PaperSize._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paperSizeValue'), STD_ANON_78, scope=PaperSize, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1127, 15)))

def _BuildAutomaton_90 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_90
    del _BuildAutomaton_90
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1127, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PaperSize._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paperSizeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1127, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PaperSize._Automaton = _BuildAutomaton_90()




Instrument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'instrumentValue'), STD_ANON_79, scope=Instrument, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1141, 15)))

def _BuildAutomaton_91 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1141, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Instrument._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instrumentValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1141, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Instrument._Automaton = _BuildAutomaton_91()




NumberOfPlayer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minimumNumberOfPlayers'), STD_ANON_80, scope=NumberOfPlayer, documentation='The minimum number of people required to play the game. Example: 2.0', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1152, 15)))

NumberOfPlayer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maximumNumberOfPlayers'), STD_ANON_81, scope=NumberOfPlayer, documentation='The maximum number of people for which the game is intended. Example: 4.0', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1163, 15)))

def _BuildAutomaton_92 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1152, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1163, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NumberOfPlayer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minimumNumberOfPlayers')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1152, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NumberOfPlayer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maximumNumberOfPlayers')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1163, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NumberOfPlayer._Automaton = _BuildAutomaton_92()




FoodAllergenStatements._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'foodAllergenStatement'), STD_ANON_82, scope=FoodAllergenStatements, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1181, 15)))

def _BuildAutomaton_93 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1181, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FoodAllergenStatements._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'foodAllergenStatement')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1181, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FoodAllergenStatements._Automaton = _BuildAutomaton_93()




MemoryCardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'memoryCardTypeValue'), STD_ANON_83, scope=MemoryCardType, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1192, 15)))

def _BuildAutomaton_94 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_94
    del _BuildAutomaton_94
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1192, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MemoryCardType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memoryCardTypeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1192, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MemoryCardType._Automaton = _BuildAutomaton_94()




FocusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'focusTypeValue'), STD_ANON_84, scope=FocusType, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1206, 15)))

def _BuildAutomaton_95 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_95
    del _BuildAutomaton_95
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1206, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FocusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'focusTypeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1206, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FocusType._Automaton = _BuildAutomaton_95()




ExposureModes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exposureMode'), STD_ANON_85, scope=ExposureModes, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1217, 15)))

def _BuildAutomaton_96 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_96
    del _BuildAutomaton_96
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1217, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExposureModes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exposureMode')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1217, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExposureModes._Automaton = _BuildAutomaton_96()




LensType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lensTypeValue'), STD_ANON_86, scope=LensType, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1231, 15)))

def _BuildAutomaton_97 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_97
    del _BuildAutomaton_97
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1231, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LensType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lensTypeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1231, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LensType._Automaton = _BuildAutomaton_97()




HandleMaterial._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'handleMaterialValue'), STD_ANON_87, scope=HandleMaterial, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1245, 15)))

def _BuildAutomaton_98 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_98
    del _BuildAutomaton_98
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1245, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(HandleMaterial._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'handleMaterialValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1245, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
HandleMaterial._Automaton = _BuildAutomaton_98()




Gemstone._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gemstoneValue'), STD_ANON_88, scope=Gemstone, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1259, 15)))

def _BuildAutomaton_99 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_99
    del _BuildAutomaton_99
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1259, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Gemstone._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gemstoneValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1259, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Gemstone._Automaton = _BuildAutomaton_99()




BodyParts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bodyPart'), STD_ANON_89, scope=BodyParts, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1273, 15)))

def _BuildAutomaton_100 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_100
    del _BuildAutomaton_100
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1273, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BodyParts._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bodyPart')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1273, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BodyParts._Automaton = _BuildAutomaton_100()




RingStyle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ringStyleValue'), STD_ANON_90, scope=RingStyle, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1287, 15)))

def _BuildAutomaton_101 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_101
    del _BuildAutomaton_101
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1287, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RingStyle._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ringStyleValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1287, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RingStyle._Automaton = _BuildAutomaton_101()




WatchBandMaterial._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'watchBandMaterialValue'), STD_ANON_91, scope=WatchBandMaterial, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1298, 15)))

def _BuildAutomaton_102 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_102
    del _BuildAutomaton_102
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1298, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(WatchBandMaterial._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'watchBandMaterialValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1298, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
WatchBandMaterial._Automaton = _BuildAutomaton_102()




WatchStyle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'watchStyleValue'), STD_ANON_92, scope=WatchStyle, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1312, 15)))

def _BuildAutomaton_103 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_103
    del _BuildAutomaton_103
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1312, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(WatchStyle._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'watchStyleValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1312, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
WatchStyle._Automaton = _BuildAutomaton_103()




FuelEconomyUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), FuelEconomyUnitOfMeasure, scope=FuelEconomyUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1323, 15)))

FuelEconomyUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measure'), STD_ANON_93, scope=FuelEconomyUnit, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1324, 15)))

def _BuildAutomaton_104 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_104
    del _BuildAutomaton_104
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1323, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1324, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FuelEconomyUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1323, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FuelEconomyUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measure')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1324, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FuelEconomyUnit._Automaton = _BuildAutomaton_104()




InterfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'interfaceTypeValue'), STD_ANON_94, scope=InterfaceType, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1333, 15)))

def _BuildAutomaton_105 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_105
    del _BuildAutomaton_105
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1333, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InterfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interfaceTypeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1333, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InterfaceType._Automaton = _BuildAutomaton_105()




BraSize._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'braBandSize'), STD_ANON_95, scope=BraSize, documentation='Bra band size in inches. Example: 34 in', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1344, 15)))

BraSize._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'braCupSize'), STD_ANON_96, scope=BraSize, documentation=' Example: A; AA; B; C; D; DD', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1355, 15)))

def _BuildAutomaton_106 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_106
    del _BuildAutomaton_106
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1344, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1355, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BraSize._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'braBandSize')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1344, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BraSize._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'braCupSize')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1355, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BraSize._Automaton = _BuildAutomaton_106()




PantSize._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inseam'), STD_ANON_97, scope=PantSize, documentation='Pant inseam in inches. Example: 32 in', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1372, 15)))

PantSize._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'waistSize'), LengthUnit, scope=PantSize, documentation='Waist size in inches. Example: 38 in', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1383, 15)))

def _BuildAutomaton_107 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_107
    del _BuildAutomaton_107
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1372, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1383, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PantSize._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inseam')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1372, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PantSize._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'waistSize')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1383, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PantSize._Automaton = _BuildAutomaton_107()




DressShirtSize._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'neckSize'), STD_ANON_98, scope=DressShirtSize, documentation='Neck size in inches. Example: 15.5 in; 16 in', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1397, 15)))

DressShirtSize._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sleeveLength'), STD_ANON_99, scope=DressShirtSize, documentation='Sleeve length in inches if available for the item. Example: 34 in', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1408, 15)))

def _BuildAutomaton_108 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_108
    del _BuildAutomaton_108
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1408, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DressShirtSize._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'neckSize')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1397, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DressShirtSize._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sleeveLength')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1408, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DressShirtSize._Automaton = _BuildAutomaton_108()




BallCoreMaterial._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ballCoreMaterialValue'), STD_ANON_100, scope=BallCoreMaterial, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1423, 15)))

def _BuildAutomaton_109 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_109
    del _BuildAutomaton_109
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1423, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BallCoreMaterial._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ballCoreMaterialValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1423, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BallCoreMaterial._Automaton = _BuildAutomaton_109()




HealthConcerns._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'healthConcern'), STD_ANON_101, scope=HealthConcerns, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1437, 15)))

def _BuildAutomaton_110 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_110
    del _BuildAutomaton_110
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1437, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(HealthConcerns._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'healthConcern')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1437, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
HealthConcerns._Automaton = _BuildAutomaton_110()




IngredientClaim._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ingredientClaimValue'), STD_ANON_102, scope=IngredientClaim, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1451, 15)))

def _BuildAutomaton_111 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_111
    del _BuildAutomaton_111
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1451, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IngredientClaim._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ingredientClaimValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1451, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IngredientClaim._Automaton = _BuildAutomaton_111()




additionalAsset._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'altText'), STD_ANON_103, scope=additionalAsset, documentation='Alternative text of an image, video, or other asset. Use descriptive terms to describe the image.', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1462, 15)))

additionalAsset._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'assetUrl'), STD_ANON_104, scope=additionalAsset, documentation='Location of the additional assets. Required if additional assets beyond the main image are provided. URLs must begin with http:// or https:// Example: http://www.walmart.com/video1.jpg', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1475, 15)))

additionalAsset._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'assetType'), STD_ANON_105, scope=additionalAsset, documentation='Provides additional information on the assets. Example: Secondary Image; Video; Instruction Manual; Assembly Instructions; Badge; Manufacturer Logo', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1488, 15)))

additionalAsset._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'additionalAssetAttributes'), AdditionalAssetAttributes, scope=additionalAsset, documentation='', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1501, 15)))

def _BuildAutomaton_112 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_112
    del _BuildAutomaton_112
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1462, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1488, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1501, 15))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(additionalAsset._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'altText')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1462, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(additionalAsset._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'assetUrl')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1475, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(additionalAsset._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'assetType')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1488, 15))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(additionalAsset._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'additionalAssetAttributes')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1501, 15))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
additionalAsset._Automaton = _BuildAutomaton_112()




productIdentifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productIdType'), STD_ANON_106, scope=productIdentifier, documentation='Type of unique identifier used in the "Product ID" field. Example: UPC; GTIN; ISBN; ISSN; EAN', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1512, 15)))

productIdentifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productId'), STD_ANON_107, scope=productIdentifier, documentation='Alphanumeric ID that uniquely identifies the product. Example: X12345', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1529, 15)))

def _BuildAutomaton_113 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_113
    del _BuildAutomaton_113
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(productIdentifier._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productIdType')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1512, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(productIdentifier._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productId')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1529, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
productIdentifier._Automaton = _BuildAutomaton_113()




certificationsAndClaim._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'certificationAndClaimType'), STD_ANON_108, scope=certificationsAndClaim, documentation='Type of certification or claim. Example: Organic; BPA-Free; Fair Trade', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1546, 15)))

certificationsAndClaim._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'certifyingAgent'), STD_ANON_109, scope=certificationsAndClaim, documentation='Certifying agency for claim. Not all claims have a certifying agent. Example: Oregon Tilth; GOTS', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1559, 15)))

def _BuildAutomaton_114 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_114
    del _BuildAutomaton_114
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1559, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(certificationsAndClaim._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'certificationAndClaimType')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1546, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(certificationsAndClaim._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'certifyingAgent')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1559, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
certificationsAndClaim._Automaton = _BuildAutomaton_114()




batteryTypeAndQuantityValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'batteryTechnologyType'), STD_ANON_110, scope=batteryTypeAndQuantityValue, documentation='If battery type is lead acid, lead acid (nonspillable), lithium ion, or lithium metal, the item requires a hazardous materials risk assessment via WERCS. Example: Does Not Contain a Battery; Alkaline; Carbon Zinc; Lead Acid; Lead Acid (Nonspillable); Lithium Primary (Lithium Metal); Lithium Ion; Magnesium; Mercury; Nickel Cadmium; Nickel Metal Hydride; Silver; Thermal; Other; Multiple Types', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1576, 15)))

batteryTypeAndQuantityValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'numberOfBatteries'), STD_ANON_111, scope=batteryTypeAndQuantityValue, documentation='Required if "Has Batteries = Y"', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1603, 15)))

def _BuildAutomaton_115 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_115
    del _BuildAutomaton_115
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1576, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1603, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(batteryTypeAndQuantityValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'batteryTechnologyType')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1576, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(batteryTypeAndQuantityValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'numberOfBatteries')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1603, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
batteryTypeAndQuantityValue._Automaton = _BuildAutomaton_115()




additionalProductAttribute._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productAttributeName'), STD_ANON_112, scope=additionalProductAttribute, documentation='A name of a single attribute for the additional detail name-value pair. Example: isCFLLightBulb', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1621, 15)))

additionalProductAttribute._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productAttributeValue'), STD_ANON_113, scope=additionalProductAttribute, documentation='A value of a single attribute for the additional detail name-value pair. Example: true', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1634, 15)))

def _BuildAutomaton_116 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_116
    del _BuildAutomaton_116
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(additionalProductAttribute._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productAttributeName')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1621, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(additionalProductAttribute._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productAttributeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1634, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
additionalProductAttribute._Automaton = _BuildAutomaton_116()




swatchImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'swatchImageUrl'), STD_ANON_114, scope=swatchImage, documentation='URL of the color or pattern swatch image. This will be shown as a small square on the item page. Recommended resolution is 100 x 100 pixels. URLs must begin with http:// or https:// Example: http://www.walmart.com/swatch1.jpg', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1651, 15)))

swatchImage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'swatchVariantAttribute'), STD_ANON_115, scope=swatchImage, documentation='Attribute name corresponding to the swatch. Example: color; pattern', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1664, 15)))

def _BuildAutomaton_117 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_117
    del _BuildAutomaton_117
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(swatchImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'swatchImageUrl')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1651, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(swatchImage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'swatchVariantAttribute')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1664, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
swatchImage._Automaton = _BuildAutomaton_117()




recycledMaterialContentValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recycledMaterial'), STD_ANON_116, scope=recycledMaterialContentValue, documentation='Type of recycled material used to create the item. Example: Bamboo; Cotton', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1681, 15)))

recycledMaterialContentValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'percentageOfRecycledMaterial'), STD_ANON_117, scope=recycledMaterialContentValue, documentation='Corresponding percentage of the recycled material used to create the item. Example: 90%; 80%', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1694, 15)))

def _BuildAutomaton_118 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_118
    del _BuildAutomaton_118
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1694, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(recycledMaterialContentValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recycledMaterial')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1681, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(recycledMaterialContentValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'percentageOfRecycledMaterial')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1694, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
recycledMaterialContentValue._Automaton = _BuildAutomaton_118()




activeIngredient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activeIngredientName'), STD_ANON_118, scope=activeIngredient, documentation='Ingredient name. Example: Benzoyl Peroxide', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1709, 15)))

activeIngredient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activeIngredientPercentage'), STD_ANON_119, scope=activeIngredient, documentation='The percent of the active ingredient in the item. Example: 0.02', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1722, 15)))

def _BuildAutomaton_119 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_119
    del _BuildAutomaton_119
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1722, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activeIngredient._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activeIngredientName')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1709, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activeIngredient._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activeIngredientPercentage')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1722, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
activeIngredient._Automaton = _BuildAutomaton_119()




fabricContentValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'materialName'), STD_ANON_120, scope=fabricContentValue, documentation='Material name. Example: Cotton; Rayon', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1737, 15)))

fabricContentValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'materialPercentage'), STD_ANON_121, scope=fabricContentValue, documentation='Corresponding material percentage. Example: 98%; 2%', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1750, 15)))

def _BuildAutomaton_120 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_120
    del _BuildAutomaton_120
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1750, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fabricContentValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'materialName')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1737, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(fabricContentValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'materialPercentage')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1750, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
fabricContentValue._Automaton = _BuildAutomaton_120()




nutrient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nutrientName'), STD_ANON_122, scope=nutrient, documentation='Name of additional nutrient.', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1765, 15)))

nutrient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nutrientAmount'), STD_ANON_123, scope=nutrient, documentation='Amount of the nutrient present in one serving. Example: 30 g', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1778, 15)))

nutrient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nutrientPercentageDailyValue'), STD_ANON_124, scope=nutrient, documentation='Percent daily value of the nutrient present in one serving. Example: 0.15', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1789, 15)))

def _BuildAutomaton_121 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_121
    del _BuildAutomaton_121
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1778, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1789, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(nutrient._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nutrientName')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1765, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(nutrient._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nutrientAmount')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1778, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(nutrient._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nutrientPercentageDailyValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1789, 15))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
nutrient._Automaton = _BuildAutomaton_121()




inputsAndOutput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inputOutputType'), STD_ANON_125, scope=inputsAndOutput, documentation='Type of connection. Example: HDMI; S/PDIF; USB 3.0; DVI', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1804, 15)))

inputsAndOutput._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inputOutputQuantity'), STD_ANON_126, scope=inputsAndOutput, documentation='Number of connections corresponding to the Input/Output type. Example: 2; 1; 3; 1', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1817, 15)))

def _BuildAutomaton_122 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_122
    del _BuildAutomaton_122
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1817, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(inputsAndOutput._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inputOutputType')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1804, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputsAndOutput._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inputOutputQuantity')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1817, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
inputsAndOutput._Automaton = _BuildAutomaton_122()




trackListing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trackNumber'), STD_ANON_127, scope=trackListing, documentation='The number of the individual track on an album. Example: 2.0', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1832, 15)))

trackListing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trackName'), STD_ANON_128, scope=trackListing, documentation='The name of the individual track on an album. Example: Blue Suede Shoes', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1843, 15)))

trackListing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trackDuration'), STD_ANON_129, scope=trackListing, documentation='The duration of the individual track on an album. Example: 4.23 min', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1856, 15)))

def _BuildAutomaton_123 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_123
    del _BuildAutomaton_123
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1832, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1843, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1856, 15))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(trackListing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trackNumber')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1832, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(trackListing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trackName')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1843, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(trackListing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trackDuration')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1856, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
trackListing._Automaton = _BuildAutomaton_123()




AdditionalAssetAttributes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'additionalAssetAttribute'), additionalAssetAttribute, scope=AdditionalAssetAttributes, location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1874, 15)))

def _BuildAutomaton_124 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_124
    del _BuildAutomaton_124
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1874, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalAssetAttributes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'additionalAssetAttribute')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1874, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AdditionalAssetAttributes._Automaton = _BuildAutomaton_124()




additionalAssetAttribute._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributeName'), STD_ANON_130, scope=additionalAssetAttribute, documentation='A name of a single attribute for the additional detail name-value pair. Example: documentType', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1879, 15)))

additionalAssetAttribute._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributeValue'), STD_ANON_131, scope=additionalAssetAttribute, documentation='A value of a single attribute for the additional detail name-value pair. Example: PDF', location=pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1892, 15)))

def _BuildAutomaton_125 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_125
    del _BuildAutomaton_125
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(additionalAssetAttribute._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributeName')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1879, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(additionalAssetAttribute._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributeValue')), pyxb.utils.utility.Location('/Users/wangmingye/Documents/Personal/Businesses/Sources/AndrewAmanda/ecomstore/templates/marketplaces/WalmartMarketplaceXSDs-2.1.2/mp/MPProductCommons.xsd', 1892, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
additionalAssetAttribute._Automaton = _BuildAutomaton_125()

