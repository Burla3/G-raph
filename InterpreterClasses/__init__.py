# import sys
# import importlib
# import pkgutil
#
#
# def import_submodules(package_name):
#     """ Import all submodules of a module, recursively
#
#     :param package_name: Package name
#     :type package_name: str
#     :rtype: dict[types.ModuleType]
#     """
#     package = sys.modules[package_name]
#     return {
#         name: importlib.import_module(package_name + '.' + name)
#         for loader, name, is_pkg in pkgutil.walk_packages(package.__path__)
#     }
#
# __all__ = import_submodules(__name__).keys()

from InterpreterClasses.EdgeDecleration import EdgeDecleration
from InterpreterClasses.FormalActualTuple import FormalActualTuple
from InterpreterClasses.Graph import Graph
from InterpreterClasses.Stack import Stack
from InterpreterClasses.ValueTypeTuple import ValueTypeTuple
from InterpreterClasses.VertexDecleration import VertexDecleration
from InterpreterClasses.Types import Types
from InterpreterClasses.Molecule import Molecule
