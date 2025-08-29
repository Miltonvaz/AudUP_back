from typing import List
from domain.repository import MaterialRepository
from domain.models import Material

class GetMaterialsByClass:
    """
    Caso de uso para obtener todos los materiales de una clase
    Tanto profesores como estudiantes pueden ver los materiales de la clase
    """
    
    def __init__(self, repository: MaterialRepository):
        self.repository = repository
    
    async def execute(self, class_id: int) -> List[Material]:
        """
        Obtener todos los materiales de una clase específica
        Los materiales solo son visibles dentro del contexto de su clase
        
        Args:
            class_id: ID de la clase
            
        Returns:
            List[Material]: Lista de materiales de la clase ordenados por ID
            
        Raises:
            ValueError: Si el ID de la clase no es válido
        """
        # Validaciones
        if class_id <= 0:
            raise ValueError("El ID de la clase debe ser un número positivo")
        
        # Obtener materiales de la clase
        return await self.repository.get_by_class_id(class_id)