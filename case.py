"""An API to the CASE ontology."""

import datetime
import uuid

import rdflib
from rdflib import RDF, XSD
import rdflib.term

CASE = rdflib.Namespace('http://case.example.org/core#')


# TODO: Perhaps inherit from RDFlib graph?
class Document(object):

    def __init__(self, graph=None):
        """Initializes the CASE document.

        Args:
            graph: The graph to populate (instance of rdflib.Graph)
                   If not provided, a graph in memory will be used.
        """
        if not graph:
            graph = rdflib.Graph()
        graph.namespace_manager.bind('case', CASE)
        self.graph = graph

    def _sanitize_triple(self, (s, p, o)):
        """Santizes the triple to contains pure rdflib terms."""

        if isinstance(s, Node):
            s = s._node

        if isinstance(o, Node):
            o = o._node
        elif o is not None and not isinstance(o, rdflib.term.Node):
            o = rdflib.Literal(o)

        if p is not None and not isinstance(p, rdflib.term.Node):
            p = CASE[p]

        return s, p, o

    def __iter__(self):
        """Wrapper for iterating over all triples in the graph"""
        return iter(self.graph)

    def __contains__(self, (s, p, o)):
        """Wrapper for checking if triple is contained in the graph."""
        return self._sanitize_triple((s, p, o)) in self.graph

    def triples(self, (s, p, o)):
        """Generator over the triple store in graph."""
        return self.graph.triples(self._sanitize_triple((s, p, o)))

    def _json_ld_context(self):
        context = dict(
            (pfx, unicode(ns))
            for (pfx, ns) in self.graph.namespaces() if pfx and
            unicode(ns) != u"http://www.w3.org/XML/1998/namespace")
        context['@vocab'] = str(CASE)
        return context

    def create_uco_object(self, type=None, **properties):
        """Creates and returns a UcoObject."""
        return UcoObject(self.graph, rdf_type=type, **properties)

    # Make separate function for creating Trace because it's very common.
    def create_trace(self, **properties):
        """Creates and returns a Trace object."""
        return Trace(self.graph, **properties)

    # Manually specify properties to help inforce both properties are supplied.
    def create_hash(self, hashMethod, hashValue):
        return self.create_node(
                CASE.Hash, bnode=True, hashMethod=hashMethod, hashValue=hashValue)

    def create_node(self, rdf_type=None, uri=None, bnode=False, **properties):
        return Node(self.graph, rdf_type=rdf_type, uri=uri, bnode=bnode,  **properties)

    # We are going to default to json-ld instead of rdflib's default of xml.
    def serialize(self, format='json-ld', **kwargs):
        """Serializes the document's graph to a destination.
        (Follows same arguments as rdflib.Graph().serialize())"""
        if format == 'json-ld':
            if 'context' not in kwargs:
                kwargs['context'] = self._json_ld_context()
            if 'auto_compact' not in kwargs:
                kwargs['auto_compact'] = True
        return self.graph.serialize(format=format, **kwargs)

    def validate(self):
        """Validates that the document follows the CASE ontology."""
        # TODO: Validate document through by parsing the ontology or perhaps
        # using an OWL reasoner.
        pass


class Node(object):
    """Implements a generic node in the graph."""
    RDF_TYPE = None

    # Namespace to use when adding properties that are not of type rdflib.URIRef.
    NAMESPACE = CASE

    def __init__(self, graph, uri=None, bnode=False, rdf_type=None, **properties):
        """Initializes and adds a node to the graph.
        NOTE: At least the type or a property must be supplied for the Node
        to exist in the graph.

        Args:
            graph: The graph to add this node to. (instance of rdflib.Graph)
            uri: Optional string to set th URI to. (If not provided a UUID will be generated.)
            bnode: Whether to create a blank node or a uri reference.
            rdf_type: The RDF type to set this node to.
            properties: Extra properties to add to this node.
            (More properties can be set after initialization by using the add() function.)
        """
        super(Node, self).__init__()
        if uri:
            self.uri = uri
        else:
            self.uri = str(uuid.uuid4())
        if bnode:
            self._node = rdflib.BNode(self.uri)
        else:
            self._node = rdflib.URIRef(self.uri)
        self._graph = graph
        if not rdf_type:
            rdf_type = self.RDF_TYPE
        # Add namespace prefix to non URIRef to allow abstraction from rdflib.
        if not isinstance(rdf_type, rdflib.term.Node):
            rdf_type = self.NAMESPACE[rdf_type]
        self.add(RDF.type, rdf_type)
        for key, value in iter(properties.items()):
            self.add(key, value)

    def add(self, property, value):
        """Adds a property and its value to the node."""
        # Ignore setting properties with a None value.
        if value is None:
            return

        # Lists and other iterables as values are the equivelent of having multiple properties.
        # NOTE: Lists obviously lose their order.
        # TODO: Add support for ordered lists.
        if isinstance(value, (list, tuple, set)):
            for item in value:
                self.add(property, item)
            return

        if isinstance(value, Node):
            value = value._node

        # Convert basic python datatypes to literals.
        elif not isinstance(value, rdflib.term.Node):
            value = rdflib.Literal(value)

        # Automatically convert non-node properties to URIRef using default prefix.
        if not isinstance(property, rdflib.term.Node):
            property = self.NAMESPACE[property]

        self._graph.add((self._node, property, value))


#  ===== Convenience Classes  =====
# TODO: Auto generate these classes by parsing the ontology.

class UcoObject(Node):
    RDF_TYPE = CASE.UcoObject

    def __init__(self, graph, rdf_type=None, **properties):
        """Initializes and adds a node to the graph.
        NOTE: At least the type or a property must be supplied for the Node
        to exist in the graph.

        Args:
            graph: The graph to add this node to. (instance of rdflib.Graph)
            rdf_type: The RDF type to set this node to.
            properties: Extra properties to add to this node.
            (More properties can be set after initialization by using the add() function.)
        """
        super(UcoObject, self).__init__(graph, rdf_type=rdf_type, **properties)
        self.add('createdTime', datetime.datetime.now())
        # TODO: Add "createdBy" property.

    def create_property_bundle(self, type=None, **properties):
        """Convenience function for adding property bundles to this Trace.

        Args:
            type: The @type of property bundle (can be of type rdflib.URIRef or string).
            properties: Properties to add to the created property bundle.

        Returns:
            The property bundle created (instance of PropertyBundle).
        """
        pb = PropertyBundle(self._graph, rdf_type=type, **properties)
        self.add(CASE.propertyBundle, pb)
        return pb


# TODO: Do we need these extra classes?
class Trace(UcoObject):
    RDF_TYPE = CASE.Trace


class PropertyBundle(Node):
    RDF_TYPE = CASE.PropertyBundle

    def __init__(self, graph, rdf_type=None, **properties):
        """Initializes and adds a node to the graph.
        NOTE: At least the type or a property must be supplied for the Node
        to exist in the graph.

        Args:
            graph: The graph to add this node to. (instance of rdflib.Graph)
            rdf_type: The RDF type to set this node to.
            properties: Extra properties to add to this node.
            (More properties can be set after initialization by using the add() function.)
        """
        # Property bundles should be blank nodes because we should be referencing them
        # through UcoObjects.
        super(PropertyBundle, self).__init__(
                graph, bnode=True, rdf_type=rdf_type, **properties)
