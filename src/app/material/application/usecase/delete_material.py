from domain.repository import MaterialRepository

class DeleteMaterial:
    """
    Caso de uso para eliminar un material de una clase
    Solo profesores pueden eliminar materiales
    """
    
    def __init__(self, repository: MaterialRepository):
        self.repository = repository
    
    async def execute(self, material_id: int, class_id: int) -> bool:
        """
        Eliminar un material específico de una clase
        Solo se puede eliminar si el material pertenece a la clase especificada
        
        Args:
            material_id: ID del material a eliminar
            class_id: ID de la clase (para validar que el material pertenece a esa clase)
            
        Returns:
            bool: True si se eliminó correctamente, False si no se encontró
            
        Raises:
            ValueError: Si los IDs no son válidos
        """
        # Validaciones
        if material_id <= 0:
            raise ValueError("El ID del material debe ser un número positivo")
        
        if class_id <= 0:
            raise ValueError("El ID de la clase debe ser un número positivo")
        
        # Eliminar el material (solo si pertenece a la clase especificada)
        return await self.repository.delete(material_id, class_id)