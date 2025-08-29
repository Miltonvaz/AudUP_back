from typing import Optional
from src.app.material.domain.repository import MaterialRepository
from src.app.material.domain.models import Material

class GetMaterialById:
    """
    Caso de uso para obtener un material específico de una clase
    Tanto profesores como estudiantes pueden ver el material
    """
    
    def __init__(self, repository: MaterialRepository):
        self.repository = repository
    
    async def execute(self, material_id: int, class_id: int) -> Optional[Material]:
        """
        Obtener un material específico dentro del contexto de una clase
        Solo se puede acceder al material si pertenece a la clase especificada
        
        Args:
            material_id: ID del material
            class_id: ID de la clase (para validar que el material pertenece a esa clase)
            
        Returns:
            Optional[Material]: Material encontrado o None si no existe o no pertenece a la clase
            
        Raises:
            ValueError: Si los IDs no son válidos
        """
        # Validaciones
        if material_id <= 0:
            raise ValueError("El ID del material debe ser un número positivo")
        
        if class_id <= 0:
            raise ValueError("El ID de la clase debe ser un número positivo")
        
        # Obtener material específico solo si pertenece a la clase
        return await self.repository.get_by_class_and_material_id(class_id, material_id)