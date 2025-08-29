from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Material, CreateMaterialRequest, UpdateMaterialRequest


class MaterialRepository(ABC):
    """
    Repositorio abstracto para Material
    Define los contratos que debe cumplir cualquier implementación de repositorio
    """

    @abstractmethod
    async def create(self, material_data: CreateMaterialRequest) -> Material:
        """
        Crear un nuevo material

        Args:
            material_data: Datos del material a crear

        Returns:
            Material: Material creado

        Raises:
            Exception: Si no se puede crear el material
        """
        pass

    @abstractmethod
    async def get_by_id(self, material_id: int) -> Optional[Material]:
        """
        Obtener un material por su ID

        Args:
            material_id: ID del material

        Returns:
            Optional[Material]: Material encontrado o None si no existe
        """
        pass

    @abstractmethod
    async def get_by_class_id(self, class_id: int) -> List[Material]:
        """
        Obtener todos los materiales de una clase específica

        Args:
            class_id: ID de la clase

        Returns:
            List[Material]: Lista de materiales de la clase
        """
        pass

    @abstractmethod
    async def get_by_class_and_material_id(self, class_id: int, material_id: int) -> Optional[Material]:
        """
        Obtener un material específico de una clase específica

        Args:
            class_id: ID de la clase
            material_id: ID del material

        Returns:
            Optional[Material]: Material encontrado o None si no existe o no pertenece a la clase
        """
        pass

    @abstractmethod
    async def update(self, material_id: int, class_id: int, update_data: UpdateMaterialRequest) -> Optional[Material]:
        """
        Actualizar un material existente

        Args:
            material_id: ID del material a actualizar
            class_id: ID de la clase (para validar que el material pertenece a esa clase)
            update_data: Datos de actualización

        Returns:
            Optional[Material]: Material actualizado o None si no existe
        """
        pass

    @abstractmethod
    async def delete(self, material_id: int, class_id: int) -> bool:
        """from domain.models import Material, CreateMaterialRequest

        Eliminar un material

        Args:
            material_id: ID del material a eliminar
            class_id: ID de la clase (para validar que el material pertenece a esa clase)

        Returns:
            bool: True si se eliminó correctamente, False si no se encontró
        """
        pass

    @abstractmethod
    async def get_materials_by_asignature(self, asignature_id: int) -> List[Material]:
        """from domain.models import Material, CreateMaterialRequest

        Obtener todos los materiales de una asignatura (a través de sus clases)

        Args:
            asignature_id: ID de la asignatura

        Returns:
            List[Material]: Lista defrom domain.models import Material, CreateMaterialRequest
 materiales de todas las clases de la asignatura
        """
        pass
