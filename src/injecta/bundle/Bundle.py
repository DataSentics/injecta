from typing import List
from box import Box
from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerInterface import ContainerInterface
from injecta.definition.Definition import Definition

class Bundle:

    def getCompilerPasses(self) -> List[CompilerPassInterface]:
        return []

    def modifyDefinitions(self, definitions: List[Definition]):
        return definitions

    def modifyRawConfig(self, rawConfig: dict) -> dict:
        return rawConfig

    def modifyParameters(self, parameters: Box) -> Box:
        return parameters

    def boot(self, container: ContainerInterface):
        pass