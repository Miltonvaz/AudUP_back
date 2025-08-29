from typing import Optional
from src.app.material.domain.repository import MaterialRepository
from src.app.material.domain.models import Material, UpdateMaterialRequest

class UpdateMaterial:
    """
    Caso de uso para actualizar un material existente dentro de una clase
    Solo profesores pueden actualizar materiales
    """
    
    def __init__(self, repository: MaterialRepository):
        self.repository = repository
    
    async def execute(self, material_id: int, class_id: int, update_data: UpdateMaterialRequest) -> Optional[Material]:
        """
        Actualizar un material existente dentro de una clase específica
        
        Args:
            material_id: ID del material a actualizar
            class_id: ID de la clase (para validar que el material pertenece a esa clase)
            update_data: Datos de actualización
            
        Returns:
            Optional[Material]: Material actualizado o None si no existe
            
        Raises:
            ValueError: Si los datos no son válidos
        """
        # Validaciones de IDs
        if material_id <= 0:
            raise ValueError("El ID del material debe ser un número positivo")
        
        if class_id <= 0:
            raise ValueError("El ID de la clase debe ser un número positivo")
        
        # Validaciones de datos de actualización
        self._validate_update_data(update_data)
        
        # Actualizar el material (solo si pertenece a la clase especificada)
        return await self.repository.update(material_id, class_id, update_data)
    
    def _validate_update_data(self, update_data: UpdateMaterialRequest) -> None:
        """Validar datos de actualización del material"""
        if update_data.title is not None:
            if not update_data.title.strip():
                raise ValueError("El título del material no puede estar vacío")
            if len(update_data.title.strip()) > 255:
                raise ValueError("El título del material no puede exceder 255 caracteres")
        
        if update_data.urlFile is not None:
            if not update_data.urlFile.strip():
                raise ValueError("La URL del archivo no puede estar vacía")
        
        if update_data.description is not None:
            if len(update_data.description) > 500:
                raise ValueError("La descripción no puede exceder 500 caracteres")